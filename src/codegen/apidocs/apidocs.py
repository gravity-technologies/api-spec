import re

import inflection

from ..parse.parse import RPC, Enum, Err, Field, Gateway, SpecRoot, Stream, Struct
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
        write_gateway_streams(
            ctx,
            gateway,
            f"artifacts/apidocs/{inflection.underscore(gateway.name).lower()}_streams.md",
        )
    write_structs_and_enums(ctx, spec_root)


def write_gateway_streams(ctx: CodegenCtx, gateway: Gateway, artifact_path: str) -> None:
    with open(artifact_path, "w") as f:
        md = MarkdownWriter(f)
        md.writeln(f"# {gateway.name} Websocket Streams")
        md.writeln("")

        last_namespace = ""
        for stream in gateway.streams:
            if stream.namespace != last_namespace:
                md.writeln(f"## {stream.namespace}")
                last_namespace = stream.namespace
            write_stream(ctx, md, gateway, stream)


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


def write_structs_and_enums(ctx: CodegenCtx, spec_root: SpecRoot) -> None:
    for struct in spec_root.structs:
        with open(
            "artifacts/apidocs/schemas/"
            + inflection.underscore(struct.name).lower()
            + ".md",
            "w",
        ) as f:
            md = MarkdownWriter(f)
            write_struct_schema(ctx, md, struct, True)
    for enum in spec_root.enums:
        with open(
            "artifacts/apidocs/schemas/"
            + inflection.underscore(enum.name).lower()
            + ".md",
            "w",
        ) as f:
            md = MarkdownWriter(f)
            write_enum_schema(md, enum, True)


###########
# STREAMS #
###########


def write_stream(
    ctx: CodegenCtx, md: MarkdownWriter, gateway: Gateway, stream: Stream
) -> None:
    name = " ".join(re.split("(?<=.)(?=[A-Z])", stream.name[6:-2]))
    md.writeln(f"### {name}")
    md.writeln("```")
    md.writeln(f"STREAM: {stream.channel}")
    md.writeln("```")
    md.writeln("")

    write_stream_feed_selector(ctx, md, stream)
    write_stream_feed_data(ctx, md, stream)
    write_errors(ctx, md, stream.on_subscribe_errors)
    write_stream_rpc_try_it_out(ctx, md, gateway, stream)
    md.writeln('<hr class="solid">')


def write_stream_feed_selector(
    ctx: CodegenCtx, md: MarkdownWriter, stream: Stream
) -> None:
    # Header
    md.writeln('=== "Feed Selector"')
    md.indent()

    # Left Section
    write_left_section(md)
    write_struct_schema(ctx, md, ctx.struct_map[stream.feed_selector], True)
    write_struct_schema(ctx, md, ctx.struct_map["WSRequestV1"], False)
    write_struct_schema(ctx, md, ctx.struct_map["WSResponseV1"], False)
    write_section_end(md)

    # Right Section
    selector = get_selector(ctx, ctx.struct_map[stream.feed_selector])
    write_right_section(md)
    md.writeln('!!! question "Query"')
    md.indent()
    md.writeln("**JSON RPC Request**")
    write_code_block(md, "json")
    write_stream_feed_request(md, stream, selector, True)
    md.writeln("```")
    write_code_block(md, "json")
    write_stream_feed_request(md, stream, selector, False)
    md.writeln("```")
    md.writeln("**JSON RPC Response**")
    write_stream_feed_response(md, stream, selector)
    md.dedent()
    write_section_end(md)

    # Footer
    md.dedent()


def get_selector(ctx: CodegenCtx, struct: Struct) -> str:
    selector_primary: list[str] = []
    selector_secondary: list[str] = []
    for i, field in enumerate(struct.fields):
        example = get_field_example(ctx, struct, field).strip('"')
        if field.selector == "primary":
            selector_primary.append(example)
        elif field.selector == "secondary":
            selector_secondary.append(example)
    selector_str = "-".join(selector_primary)
    if len(selector_secondary) > 0:
        selector_str = f"{selector_str}@{"-".join(selector_secondary)}"
    return selector_str


def write_stream_feed_request(
    md: MarkdownWriter, stream: Stream, selector: str, is_full: bool
) -> None:
    md.writeln("{")
    md.indent()
    md.writeln('"request_id":1,')
    md.writeln(f'"stream":"{stream.channel}",')
    md.writeln(f'"feed":["{selector}"],')
    md.writeln('"method":"subscribe",')
    md.writeln(f'"is_full":{str(is_full).lower()}')
    md.dedent()
    md.writeln("}")


def write_stream_feed_response(md: MarkdownWriter, stream: Stream, selector: str) -> None:
    write_code_block(md, "json")
    md.writeln("{")
    md.indent()
    md.writeln('"request_id":1,')
    md.writeln(f'"stream":"{stream.channel}",')
    md.writeln(f'"subs":["{selector}"],')
    md.writeln('"unsubs":[],')
    md.writeln('"num_snapshots":[1],')
    md.writeln('"first_sequence_number":[2813]')
    md.dedent()
    md.writeln("}")
    md.writeln("```")


def write_stream_feed_data(ctx: CodegenCtx, md: MarkdownWriter, stream: Stream) -> None:
    # Header
    md.writeln('=== "Feed Data"')
    md.indent()

    # Left Section
    write_left_section(md)
    write_struct_schema(ctx, md, ctx.struct_map[stream.feed], True)
    write_section_end(md)

    # Right Section
    write_right_section(md)
    md.writeln("!!! success")
    md.indent()
    write_code_block(md, "json")
    write_struct_example(ctx, md, ctx.struct_map[stream.feed], True, True)
    md.writeln("```")
    write_code_block(md, "json")
    write_struct_example(ctx, md, ctx.struct_map[stream.feed], True, False)
    md.writeln("```")
    md.dedent()
    write_section_end(md)

    # Footer
    md.dedent()


def write_stream_rpc_try_it_out(
    ctx: CodegenCtx, md: MarkdownWriter, gateway: Gateway, stream: Stream
) -> None:
    # Header
    md.writeln('=== "Try it out"')
    md.indent()

    # Auth Section
    if stream.auth_required:
        md.writeln('-8<- "sections/auth.md"')

    # Main Section (Full)
    write_left_section(md, "50%")
    for endpoint in gateway.endpoints:
        md.writeln(f'!!! example "Try {endpoint.name.upper()} Full"')
        md.indent()
        write_code_block(md, "bash")
        md.writeln(f'wscat -c "wss://{endpoint.url}/ws" \\')
        if stream.auth_required:
            md.writeln('-H "Cookie: $GRVT_COOKIE" \\')
        md.writeln("-x '")
        selector = get_selector(ctx, ctx.struct_map[stream.feed_selector])
        write_stream_feed_request(md, stream, selector, True)
        md.writeln("' -w 360")
        md.writeln("```")
        md.dedent()
    write_section_end(md)

    # Main Section (Lite)
    write_right_section(md, "50%")
    for endpoint in gateway.endpoints:
        md.writeln(f'!!! example "Try {endpoint.name.upper()} Lite"')
        md.indent()
        write_code_block(md, "bash")
        md.writeln(f'wscat -c "wss://{endpoint.url}/ws" \\')
        if stream.auth_required:
            md.writeln('-H "Cookie: $GRVT_COOKIE" \\')
        md.writeln("-x '")
        selector = get_selector(ctx, ctx.struct_map[stream.feed_selector])
        write_stream_feed_request(md, stream, selector, False)
        md.writeln("' -w 360")
        md.writeln("```")
        md.dedent()
    write_section_end(md)

    # Footer
    md.dedent()


########
# RPCS #
########


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
    write_errors(ctx, md, rpc.on_request_errors)
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
    md.writeln('!!! question "Query"')
    md.indent()
    write_code_block(md, "json")
    write_struct_example(ctx, md, ctx.struct_map[rpc.request], True, True)
    md.writeln("```")
    write_code_block(md, "json")
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
    md.writeln("!!! success")
    md.indent()
    write_code_block(md, "json")
    write_struct_example(ctx, md, ctx.struct_map[rpc.response], True)
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

    # Auth Section
    if rpc.auth_required:
        md.writeln('-8<- "sections/auth.md"')

    # Main Section (Full)
    write_left_section(md, "50%")
    for endpoint in gateway.endpoints:
        md.writeln(f'!!! example "Try {endpoint.name.upper()} Full"')
        md.indent()
        write_code_block(md, "bash")
        md.writeln(
            f"curl --location 'https://{endpoint.url}/full/v{rpc.version}{rpc.route}' \\"
        )
        if rpc.auth_required:
            md.writeln('--header "Cookie: $GRVT_COOKIE" \\')

        request_struct = ctx.struct_map[rpc.request]
        md.write("--data '")
        write_struct_example(ctx, md, request_struct, True)
        md.writeln("'")

        md.writeln("```")
        md.dedent()
    write_section_end(md)

    # Main Section (Lite)
    write_right_section(md, "50%")
    for endpoint in gateway.endpoints:
        md.writeln(f'!!! example "Try {endpoint.name.upper()} Lite"')
        md.indent()
        write_code_block(md, "bash")
        md.writeln(
            f"curl --location 'https://{endpoint.url}/lite/v{rpc.version}{rpc.route}' \\"
        )
        if rpc.auth_required:
            md.writeln('--header "Cookie: $GRVT_COOKIE" \\')

        request_struct = ctx.struct_map[rpc.request]
        md.write("--data '")
        write_struct_example(ctx, md, request_struct, True, False)
        md.writeln("'")

        md.writeln("```")
        md.dedent()
    write_section_end(md)

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
        comma = "," if i < len(struct.fields) - 1 else ""
        md.write(f'"{fn}": ')
        for _ in range(field.array_depth):
            md.write("[")
        if field.json_type in ctx.struct_map:
            write_struct_example(ctx, md, ctx.struct_map[field.json_type], False, is_full)
        else:
            md.write(get_field_example(ctx, struct, field))
        for _ in range(field.array_depth):
            md.write("]")
        md.writeln(comma)

    md.dedent()

    if is_root:
        md.writeln("}")
    else:
        md.write("}")


def write_struct_schema(
    ctx: CodegenCtx, md: MarkdownWriter, struct: Struct, is_root: bool
) -> None:
    # Header
    path = "/../../schemas/" + inflection.underscore(struct.name).lower()
    if is_root:
        md.writeln(f'!!! info "[{struct.name}]({path})"')
    else:
        md.writeln(f'??? info "[{struct.name}]({path})"')
    md.indent()

    # Comment
    write_comment(md, struct.comment)

    # Field Table
    md.writeln("|Name<br>`Lite`|Type|Required<br>`Default`| Description |")
    md.writeln("|-|-|-|-|")
    for field in struct.fields:
        json_type = field.json_type
        for _ in range(field.array_depth):
            json_type = f"[{json_type}]"
        md.writeln(
            f"|{field.name}<br>`{field.lite_name}` |{json_type}|"
            + f"{ f'False<br>`{field.default}`' if field.optional else 'True' }|"
            + f"{'<br>'.join(field.comment)}|"
        )

    # Field Import Table
    for field in struct.fields:
        if field.json_type in ctx.enum_map:
            write_enum_schema(md, ctx.enum_map[field.json_type])
        elif field.json_type in ctx.struct_map:
            write_struct_schema(ctx, md, ctx.struct_map[field.json_type], False)
    md.dedent()


def write_enum_schema(md: MarkdownWriter, enum: Enum, is_root: bool = False) -> None:
    # Header
    path = "/../../schemas/" + inflection.underscore(enum.name).lower()
    if is_root:
        md.writeln(f'!!! info "[{enum.name}]({path})"')
    else:
        md.writeln(f'??? info "[{enum.name}]({path})"')
    md.indent()

    # Comment
    write_comment(md, enum.comment)

    # Value Table
    md.writeln("|Value| Description |")
    md.writeln("|-|-|")
    for value in enum.values:
        md.writeln(f"|`{value.name}` = {value.value}|{"<br>".join(value.comment)}|")
    md.dedent()


def write_errors(ctx: CodegenCtx, md: MarkdownWriter, errors: list[Err]) -> None:
    # Header
    md.writeln('=== "Errors"')
    md.indent()

    # Left Section
    write_left_section(md)
    md.writeln('!!! info "Error Codes"')
    md.indent()
    md.writeln("|Code|HttpStatus| Description |")
    md.writeln("|-|-|-|")
    for error in errors:
        md.writeln(f"|{error.code}|{error.status}|{error.message}|")
    md.dedent()
    write_section_end(md)

    # Right Section
    write_right_section(md)
    md.writeln("!!! failure")
    md.indent()
    write_code_block(md, "json")
    for error in errors:
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


######################
# Formatting Helpers #
######################


def get_field_example(ctx: CodegenCtx, struct: Struct, field: Field) -> str:
    example_value = ""
    if field.example:
        example_value = field.example.replace("'", '"')
    elif field.json_type in ctx.enum_map:
        example_value = '"' + ctx.enum_map[field.json_type].values[0].name + '"'
    else:
        example_value = "null"
        print(f"No example value for field: {struct.name}.{field.name}")  # noqa: T201

    # To allow environment variable injection in the example
    if example_value.startswith('"$'):
        example_value = f"\"'{example_value[1:-1]}'\""

    # Handle lists
    return example_value.removeprefix("[").removesuffix("]")


def write_comment(md: MarkdownWriter, comment: list[str]) -> None:
    if len(comment) > 0:
        for i, line in enumerate(comment):
            if line.strip().endswith("|"):
                md.writeln(line)
            else:
                md.write(line + "<br>")
        md.writeln("\n")


def write_left_section(md: MarkdownWriter, width: str = "70%") -> None:
    md.writeln(
        f'<section markdown="1" style="float: left; width: {width};'
        + ' padding-right: 10px;">'
    )


def write_right_section(md: MarkdownWriter, width: str = "30%") -> None:
    md.writeln(f'<section markdown="1" style="float: right; width: {width};">')


def write_section_end(md: MarkdownWriter) -> None:
    md.writeln("</section>")


def write_code_block(md: MarkdownWriter, language: str) -> None:
    md.writeln(f"``` {{ .{language} .copy }}")
