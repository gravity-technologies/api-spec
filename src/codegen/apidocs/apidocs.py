import re

import inflection

from ..parse.parse import RPC, Enum, Gateway, SpecRoot, Struct
from .codegen_context import CodegenCtx
from .markdown_writer import MarkdownWriter


def generate(spec_root: SpecRoot) -> None:
    ctx = CodegenCtx(spec_root)
    for gateway in spec_root.gateways:
        write_gateway_rpcs(
            ctx,
            gateway,
            f"artifacts/apidocs/{inflection.underscore(gateway.name).lower()}_api.md",
        )


def write_gateway_rpcs(ctx: CodegenCtx, gateway: Gateway, artifact_path: str) -> None:
    with open(artifact_path, "w") as f:
        md = MarkdownWriter(f)
        md.writeln(f"# {gateway.name} APIs")
        md.writeln("All requests should be made using the `POST` HTTP method.")
        md.writeln("")

        last_namespace = ""
        for rpc in gateway.rpcs:
            if rpc.namespace != last_namespace:
                md.writeln(f"## {rpc.namespace}")
                last_namespace = rpc.namespace
            write_rpc(ctx, md, gateway, rpc)


def write_rpc(ctx: CodegenCtx, md: MarkdownWriter, gateway: Gateway, rpc: RPC) -> None:
    name = " ".join(re.split("(?<=.)(?=[A-Z])", rpc.name[3:-2]))
    md.writeln(f"### {name}")
    md.writeln("```")
    md.writeln(f"FULL ENDPOINT: full/v{rpc.version}{rpc.route}")
    md.writeln(f"LITE ENDPOINT: lite/v{rpc.version}{rpc.route}")
    md.writeln("```")
    md.writeln("")

    write_rpc_request(ctx, md, rpc)
    write_rpc_response(ctx, md, rpc)
    write_rpc_errors(ctx, md, rpc)
    write_rpc_try_it_out(ctx, md, gateway, rpc)
    md.writeln('<hr class="solid">')


def write_rpc_request(ctx: CodegenCtx, md: MarkdownWriter, rpc: RPC) -> None:
    # Header
    md.writeln('=== "Request"')
    md.indent()

    # Left Section
    write_left_section(md)
    write_struct_schema(ctx, md, ctx.struct_map[rpc.request], True)
    write_section_end(md)

    # Right Section
    write_right_section(md)
    md.writeln("!!! example")
    md.indent()
    md.writeln("```json")
    write_struct_example(ctx, md, ctx.struct_map[rpc.request], True, True)
    md.writeln("```")
    md.writeln("```json")
    write_struct_example(ctx, md, ctx.struct_map[rpc.request], True, False)
    md.writeln("```")
    md.dedent()
    write_section_end(md)

    # Footer
    md.dedent()


def write_rpc_response(ctx: CodegenCtx, md: MarkdownWriter, rpc: RPC) -> None:
    # Header
    md.writeln('=== "Response"')
    md.indent()

    # Left Section
    write_left_section(md)
    write_struct_schema(ctx, md, ctx.struct_map[rpc.response], True)
    write_section_end(md)

    # Right Section
    write_right_section(md)
    md.writeln("!!! example")
    md.indent()
    md.writeln("```json")
    write_struct_example(ctx, md, ctx.struct_map[rpc.response], True)
    md.writeln("```")
    md.dedent()
    write_section_end(md)

    # Footer
    md.dedent()


def write_rpc_errors(ctx: CodegenCtx, md: MarkdownWriter, rpc: RPC) -> None:
    # Header
    md.writeln('=== "Errors"')
    md.indent()

    # Left Section
    write_left_section(md)
    md.writeln('!!! info "Error Codes"')
    md.indent()
    md.writeln("|Code|HttpStatus| Description |")
    md.writeln("|-|-|-|")
    for error in rpc.on_request_errors:
        md.writeln(f"|{error.code}|{error.status}|{error.message}|")
    md.dedent()
    write_section_end(md)

    # Right Section
    write_right_section(md)
    md.writeln("!!! example")
    md.indent()
    md.writeln("```json")
    for error in rpc.on_request_errors:
        md.writeln("{")
        md.indent()
        md.writeln(f'"code":{error.code},')
        md.writeln(f'"message":"{error.message}",')
        md.writeln(f'"status":{error.status}')
        md.dedent()
        md.writeln("}")
    md.writeln("```")
    md.dedent()
    write_section_end(md)

    # Footer
    md.dedent()


def write_rpc_try_it_out(
    ctx: CodegenCtx, md: MarkdownWriter, gateway: Gateway, rpc: RPC
) -> None:
    # Header
    md.writeln('=== "Try it out"')
    md.indent()

    # Main Section
    for endpoint in gateway.endpoints:
        md.writeln(f'!!! info "{endpoint.name}"')
        md.indent()
        md.writeln("```bash")
        md.writeln(
            f"curl --location 'https://{endpoint.url}/full/v{rpc.version}{rpc.route}' \\"
        )

        request_struct = ctx.struct_map[rpc.request]
        md.write("--data '")
        write_struct_example(ctx, md, request_struct, True)
        md.writeln("'")

        md.writeln("```")
        md.dedent()

    # Footer
    md.dedent()


######################
# SCHEMAS & EXAMPLES #
######################


def write_struct_example(
    ctx: CodegenCtx,
    md: MarkdownWriter,
    struct: Struct,
    is_root: bool,
    is_full: bool = True,
) -> None:
    md.writeln("{")
    md.indent()

    for i, field in enumerate(struct.fields):
        fn = field.name if is_full else field.lite_name
        if field.json_type in ctx.struct_map:
            md.write(f'"{fn}": ')
            write_struct_example(ctx, md, ctx.struct_map[field.json_type], False, is_full)
            md.writeln("," if i < len(struct.fields) - 1 else "")
        else:
            example_value = ""
            if field.example:
                example_value = field.example.replace("'", '"')
            elif field.json_type in ctx.enum_map:
                example_value = '"' + ctx.enum_map[field.json_type].values[0].name + '"'
            else:
                example_value = "null"
                print(f"No example value for field: {struct.name}.{field.name}")  # noqa: T201
            md.writeln(
                f'"{fn}": {example_value}' + ("," if i < len(struct.fields) - 1 else "")
            )

    md.dedent()

    if is_root:
        md.writeln("}")
    else:
        md.write("}")


def write_struct_schema(
    ctx: CodegenCtx, md: MarkdownWriter, struct: Struct, is_root: bool
) -> None:
    # Header
    if is_root:
        md.writeln(f'!!! info "{struct.name}"')
    else:
        md.writeln(f'??? info "{struct.name}"')
    md.indent()

    # Comment
    write_comment(md, struct.comment)

    # Field Table
    md.writeln("|Name|Lite|Type|Required| Description |")
    md.writeln("|-|-|-|-|-|")
    for field in struct.fields:
        md.writeln(
            f"|{field.name}|{field.lite_name}|{field.json_type}|"
            + f"{not field.optional}|{"<br>".join(field.comment)}|"
        )

    # Field Import Table
    for field in struct.fields:
        if field.json_type in ctx.enum_map:
            write_enum_schema(md, ctx.enum_map[field.json_type])
        elif field.json_type in ctx.struct_map:
            write_struct_schema(ctx, md, ctx.struct_map[field.json_type], False)
    md.dedent()


def write_enum_schema(md: MarkdownWriter, enum: Enum) -> None:
    md.writeln(f'??? info "{enum.name}"')
    md.indent()

    # Comment
    write_comment(md, enum.comment)

    # Value Table
    md.writeln("|Value| Description |")
    md.writeln("|-|-|")
    for value in enum.values:
        md.writeln(f"|`{value.name}` = {value.value}|{"<br>".join(value.comment)}|")
    md.dedent()


######################
# Formatting Helpers #
######################


def write_comment(md: MarkdownWriter, comment: list[str]) -> None:
    if len(comment) > 0:
        for i, line in enumerate(comment):
            if line.strip().endswith("|"):
                md.writeln(line)
            else:
                md.write(line + "<br>")
        md.writeln("\n")


def write_left_section(md: MarkdownWriter) -> None:
    md.writeln(
        '<section markdown="1" style="float: left; width: 70%;'
        + ' padding-right: 10px;">'
    )


def write_right_section(md: MarkdownWriter) -> None:
    md.writeln('<section markdown="1" style="float: right; width: 30%;">')


def write_section_end(md: MarkdownWriter) -> None:
    md.writeln("</section>")
