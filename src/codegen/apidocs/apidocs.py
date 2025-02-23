from dataclasses import fields
import re
from copy import deepcopy
from typing import cast

import inflection

from ..parse.parse import RPC, Enum, Err, Field, Gateway, SpecRoot, Stream, Struct
from .codegen_context import CodegenCtx
from .markdown_writer import MarkdownWriter

# hacks to remove unused secondary selectors for a specific stream
IGNORE_SECONDARY_SELECTORS = {
    "StreamOrderbookDeltaV1": ["depth"],
}

# hacks to remove unused fields
IGNORE_FIELD_PATHS = [
    ["ApiCreateOrderRequest", "Order", "state"],
    ["ApiCreateOrderRequest", "Order", "order_id"],
    ["JSONRPCRequest", "ApiCreateOrderRequest", "Order", "state"],
    ["JSONRPCRequest", "ApiCreateOrderRequest", "Order", "order_id"],
]

IGNORE_STRUCTS = [
    "ApiDedustPositionRequest",
    "ApiDedustPositionResponse",
    "TriggerOrderMetadata",
    "TriggerType",
    "TriggerBy",
    "BrokerTag",
]

# skip these fields for all structs, at all levels of nesting
IGNORE_FIELDS_ANY_PATH = [
    "prev_sequence_number",
    "latest_sequence_number",
    "use_global_sequence_number",
    "trigger",
    "broker",
]

IGNORE_RPCS: list[str] = ["RPCDedustPositionV1"]

IGNORE_ENUM_VALUES: dict[str, list[str]] = {
    "Currency": [
        "XLM",
        "WLD",
        "WIF",
        "VIRTUAL",
        "KSHIB",
        "POPCAT",
        "PENGU",
        "LINK",
        "KBONK",
        "JUP",
        "ENA",
        "DOGE",
        "AIXBT",
        "AI_16_Z",
        "ADA",
        "AAVE",
        "VINE",
        "PENDLE",
        "UXLINK",
    ],
    "BrokerTag": ["*"],
}


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
            if rpc.name in IGNORE_RPCS:
                continue
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
    write_stream_errors(ctx, md, stream.on_subscribe_errors)
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
    import_struct_schema(md, ctx.struct_map[stream.feed_selector])
    md.writeln('??? info "JSONRPC Wrappers"')
    md.indent()
    import_struct_schema(md, ctx.struct_map["JSONRPCRequest"])
    import_struct_schema(md, ctx.struct_map["JSONRPCResponse"])
    import_struct_schema(md, ctx.struct_map["WSSubscribeParams"])
    import_struct_schema(md, ctx.struct_map["WSSubscribeResult"])
    import_struct_schema(md, ctx.struct_map["WSUnsubscribeParams"])
    import_struct_schema(md, ctx.struct_map["WSUnsubscribeResult"])
    import_struct_schema(md, ctx.struct_map["WSSubscribeRequestV1Legacy"])
    import_struct_schema(md, ctx.struct_map["WSSubscribeResponseV1Legacy"])
    md.dedent()
    write_section_end(md)

    # Right Section
    selector = get_selector(
        ctx,
        ctx.struct_map[stream.feed_selector],
        IGNORE_SECONDARY_SELECTORS.get(stream.name, []),
    )
    write_right_section(md)

    md.writeln('???+ question "Subscribe"')
    md.indent()
    md.writeln("**Full Subscribe Request**")
    write_code_block(md, "json")
    write_stream_subscribe_request(ctx, md, stream, selector, True)
    md.writeln("```")
    md.writeln("**Full Subscribe Response**")
    write_code_block(md, "json")
    write_stream_subscribe_response(ctx, md, stream, selector, True)
    md.writeln("```")
    md.dedent()

    md.writeln('??? question "Unsubscribe"')
    md.indent()
    md.writeln("**Full Unsubscribe Request**")
    write_code_block(md, "json")
    write_stream_unsubscribe_request(ctx, md, stream, selector, True)
    md.writeln("```")
    md.writeln("**Full Unsubscribe Response**")
    write_code_block(md, "json")
    write_stream_unsubscribe_response(ctx, md, stream, selector, True)
    md.writeln("```")
    md.dedent()

    md.writeln('??? question "Legacy Subscribe"')
    md.indent()
    md.writeln("**Full Subscribe Request**")
    write_code_block(md, "json")
    write_stream_legacy_feed_request(md, stream, selector, True)
    md.writeln("```")
    md.writeln("**Full Subscribe Response**")
    write_stream_legacy_feed_response(md, stream, selector)
    md.dedent()

    write_section_end(md)

    # Footer
    md.dedent()


def get_selector(
    ctx: CodegenCtx, struct: Struct, ignore_secondary_list: list[str] = []
) -> str:
    selector_primary: list[str] = []
    selector_secondary: list[str] = []
    for i, field in enumerate(struct.fields):
        example = get_field_example(ctx, struct, field).strip('"')
        if field.selector == "primary":
            selector_primary.append(example)
        elif field.selector == "secondary":
            if field.name in ignore_secondary_list:
                continue
            selector_secondary.append(example)
    selector_str = "-".join(selector_primary)
    if len(selector_secondary) > 0:
        selector_str = f"{selector_str}@{"-".join(selector_secondary)}"
    return selector_str


def write_stream_subscribe_request(
    ctx: CodegenCtx, md: MarkdownWriter, stream: Stream, selector: str, is_full: bool
) -> None:
    params = ctx.struct_map["WSSubscribeParams"]
    params.fields[0].example = f'"{stream.channel}"'
    params.fields[1].example = f'"{selector}"'
    req = ctx.struct_map["JSONRPCRequest"]
    req.fields[1].example = '"subscribe"'
    write_struct_example_with_generics(
        ctx,
        md,
        req,
        True,
        is_full,
        params,
    )


def write_stream_unsubscribe_request(
    ctx: CodegenCtx, md: MarkdownWriter, stream: Stream, selector: str, is_full: bool
) -> None:
    params = ctx.struct_map["WSUnsubscribeParams"]
    params.fields[0].example = f'"{stream.channel}"'
    params.fields[1].example = f'"{selector}"'
    req = ctx.struct_map["JSONRPCRequest"]
    req.fields[1].example = '"unsubscribe"'
    write_struct_example_with_generics(
        ctx,
        md,
        req,
        True,
        is_full,
        params,
    )


def write_stream_subscribe_response(
    ctx: CodegenCtx, md: MarkdownWriter, stream: Stream, selector: str, is_full: bool
) -> None:
    params = ctx.struct_map["WSSubscribeResult"]
    params.fields[0].example = f'"{stream.channel}"'
    params.fields[1].example = f'"{selector}"'
    params.fields[2].example = "[]"
    resp = ctx.struct_map["JSONRPCResponse"]
    errField = resp.fields.pop(2)  # Remove Error
    write_struct_example_with_generics(
        ctx,
        md,
        resp,
        True,
        is_full,
        params,
    )
    resp.fields.insert(2, errField)


def write_stream_unsubscribe_response(
    ctx: CodegenCtx, md: MarkdownWriter, stream: Stream, selector: str, is_full: bool
) -> None:
    params = ctx.struct_map["WSUnsubscribeResult"]
    params.fields[0].example = f'"{stream.channel}"'
    params.fields[1].example = f'"{selector}"'
    resp = ctx.struct_map["JSONRPCResponse"]
    errField = resp.fields.pop(2)  # Remove Error
    write_struct_example_with_generics(
        ctx,
        md,
        resp,
        True,
        is_full,
        params,
    )
    resp.fields.insert(2, errField)


def write_stream_legacy_feed_request(
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


def write_stream_legacy_feed_response(
    md: MarkdownWriter, stream: Stream, selector: str
) -> None:
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
    import_struct_schema(md, ctx.struct_map[stream.feed])
    write_section_end(md)

    # Right Section
    write_right_section(md)
    md.writeln("!!! success")
    md.indent()
    md.writeln("**Full Feed Response**")
    write_code_block(md, "json")
    resp_struct = deepcopy(ctx.struct_map[stream.feed])
    resp_struct.fields[0].example = f'"{stream.channel}"'  # put correct channel
    write_struct_example(ctx, md, resp_struct, True, True)
    md.writeln("```")
    md.writeln("**Lite Feed Response**")
    write_code_block(md, "json")
    write_struct_example(ctx, md, resp_struct, True, False)
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
        md.writeln('-8<- "sections/auth_closed.md"')

    for endpoint in gateway.endpoints:
        # Environment Tab
        md.writeln(f'=== "{endpoint.name.upper()}"')
        md.indent()

        for is_full in [True, False]:
            full_or_lite = "Full" if is_full else "Lite"
            url_suffix = "full" if is_full else "lite"
            if is_full:
                write_left_section(md, "50%")
            else:
                write_right_section(md, "50%")

            # Subscribe
            md.writeln(f'!!! example "Subscribe {full_or_lite}"')
            md.indent()
            write_code_block(md, "bash")
            md.writeln(f'wscat -c "wss://{endpoint.url}/ws/{url_suffix}" \\')
            if stream.auth_required:
                md.writeln('-H "Cookie: $GRVT_COOKIE" \\')
                md.writeln('-H "X-Grvt-Account-Id: $GRVT_ACCOUNT_ID" \\')
            md.writeln("-x '")
            selector = get_selector(
                ctx,
                ctx.struct_map[stream.feed_selector],
                IGNORE_SECONDARY_SELECTORS.get(stream.name, []),
            )
            write_stream_subscribe_request(ctx, md, stream, selector, is_full)
            md.writeln("' -w 360")
            md.writeln("```")
            md.dedent()

            # Unsubscribe
            md.writeln(f'!!! example "Unsubscribe {full_or_lite}"')
            md.indent()
            write_code_block(md, "bash")
            md.writeln(f'wscat -c "wss://{endpoint.url}/ws/{url_suffix}" \\')
            if stream.auth_required:
                md.writeln('-H "Cookie: $GRVT_COOKIE" \\')
                md.writeln('-H "X-Grvt-Account-Id: $GRVT_ACCOUNT_ID" \\')
            md.writeln("-x '")
            selector = get_selector(
                ctx,
                ctx.struct_map[stream.feed_selector],
                IGNORE_SECONDARY_SELECTORS.get(stream.name, []),
            )
            write_stream_unsubscribe_request(ctx, md, stream, selector, is_full)
            md.writeln("' -w 360")
            md.writeln("```")
            md.dedent()

            # Legacy Subscribe
            md.writeln(f'!!! example "Legacy Subscribe {full_or_lite}"')
            md.indent()
            write_code_block(md, "bash")
            md.writeln(f'wscat -c "wss://{endpoint.url}/ws" \\')
            if stream.auth_required:
                md.writeln('-H "Cookie: $GRVT_COOKIE" \\')
                md.writeln('-H "X-Grvt-Account-Id: $GRVT_ACCOUNT_ID" \\')
            md.writeln("-x '")
            selector = get_selector(
                ctx,
                ctx.struct_map[stream.feed_selector],
                IGNORE_SECONDARY_SELECTORS.get(stream.name, []),
            )
            write_stream_legacy_feed_request(md, stream, selector, is_full)
            md.writeln("' -w 360")
            md.writeln("```")
            md.dedent()

            write_section_end(md)

        md.dedent()

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
    import_struct_schema(md, ctx.struct_map[rpc.request])
    write_section_end(md)

    # Right Section
    write_right_section(md)
    md.writeln('!!! question "Query"')
    md.indent()
    md.writeln("**Full Request**")
    write_code_block(md, "json")
    write_struct_example(ctx, md, ctx.struct_map[rpc.request], True, True)
    md.writeln("```")
    md.writeln("**Lite Request**")
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
    import_struct_schema(md, ctx.struct_map[rpc.response])
    write_section_end(md)

    # Right Section
    write_right_section(md)
    md.writeln("!!! success")
    md.indent()
    md.writeln("**Full Response**")
    write_code_block(md, "json")
    write_struct_example(ctx, md, ctx.struct_map[rpc.response], True)
    md.writeln("```")
    md.writeln("**Lite Response**")
    write_code_block(md, "json")
    write_struct_example(ctx, md, ctx.struct_map[rpc.response], True, False)
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
        md.writeln('-8<- "sections/auth_closed.md"')

    for endpoint in gateway.endpoints:
        # Environment Tab
        md.writeln(f'=== "{endpoint.name.upper()}"')
        md.indent()

        for is_full in [True, False]:
            request_struct = ctx.struct_map[rpc.request]
            full_or_lite = "Full" if is_full else "Lite"
            url_suffix = "full" if is_full else "lite"
            if is_full:
                write_left_section(md, "50%")
            else:
                write_right_section(md, "50%")

            # REST Request
            md.writeln(f'!!! example "REST {full_or_lite}"')
            md.indent()
            write_code_block(md, "bash")
            md.writeln(
                f"curl --location 'https://{endpoint.url}/{url_suffix}/v{rpc.version}"
                f"{rpc.route}' \\"
            )
            if rpc.auth_required:
                md.writeln('--header "Cookie: $GRVT_COOKIE" \\')
                md.writeln('--header "X-Grvt-Account-Id: $GRVT_ACCOUNT_ID" \\')
            md.write("--data '")
            write_struct_example(ctx, md, request_struct, True, is_full)
            md.writeln("'")
            md.writeln("```")
            md.dedent()

            # JSONRPC Request
            md.writeln(f'!!! example "JSONRPC {full_or_lite}"')
            md.indent()
            write_code_block(md, "bash")
            md.writeln(f'wscat -c "wss://{endpoint.url}/ws/{url_suffix}" \\')
            if rpc.auth_required:
                md.writeln('-H "Cookie: $GRVT_COOKIE" \\')
                md.writeln('-H "X-Grvt-Account-Id: $GRVT_ACCOUNT_ID" \\')
            md.writeln("-x '")
            req = ctx.struct_map["JSONRPCRequest"]
            req.fields[1].example = f'"v{rpc.version}{rpc.route}"'
            write_struct_example_with_generics(
                ctx,
                md,
                req,
                True,
                is_full,
                request_struct,
            )
            md.writeln("' -w 360")
            md.writeln("```")
            md.dedent()

            write_section_end(md)

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
    write_struct_example_with_generics(ctx, md, struct, is_root, is_full)


def write_struct_example_with_generics(
    ctx: CodegenCtx,
    md: MarkdownWriter,
    struct: Struct,
    is_root: bool,
    is_full: bool = True,
    generic: Struct | None = None,
    field_path: list[str] = [],
) -> None:
    md.writeln("{")
    md.indent()

    field_path = field_path + [struct.name]

    fields_skipped = 0
    for i, field in enumerate(struct.fields):
        if (
            field.name in IGNORE_FIELDS_ANY_PATH
            or field_path + [field.name] in IGNORE_FIELD_PATHS
        ):
            fields_skipped += 1
    for i, field in enumerate(struct.fields):
        if (
            field.name in IGNORE_FIELDS_ANY_PATH
            or field_path + [field.name] in IGNORE_FIELD_PATHS
        ):
            continue
        fn = field.name if is_full else field.lite_name
        comma = "," if i < len(struct.fields) - fields_skipped - 1 else ""
        md.write(f'"{fn}": ')
        for _ in range(field.array_depth):
            md.write("[")
        if field.json_type == "object":
            write_struct_example_with_generics(
                ctx, md, cast(Struct, generic), False, is_full, generic, field_path
            )
        elif field.json_type in ctx.struct_map:
            write_struct_example_with_generics(
                ctx,
                md,
                ctx.struct_map[field.json_type],
                False,
                is_full,
                generic,
                field_path,
            )
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


def import_struct_schema(md: MarkdownWriter, struct: Struct) -> None:
    md.writeln(f'-8<- "docs/schemas/{inflection.underscore(struct.name).lower()}.md"')


def write_struct_schema(
    ctx: CodegenCtx, md: MarkdownWriter, struct: Struct, is_root: bool
) -> None:
    if struct.name in IGNORE_STRUCTS:
        return
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

    if enum.name in IGNORE_ENUM_VALUES:
        if (
            len(IGNORE_ENUM_VALUES[enum.name]) == 1
            and IGNORE_ENUM_VALUES[enum.name][0] == "*"
        ):
            return
        enum.values = [
            value
            for value in enum.values
            if value.name not in IGNORE_ENUM_VALUES[enum.name]
        ]

    # Value Table
    md.writeln("|Value| Description |")
    md.writeln("|-|-|")
    for value in enum.values:
        md.writeln(f"|`{value.name}` = {value.value}|{"<br>".join(value.comment)}|")
    md.dedent()


def write_stream_errors(ctx: CodegenCtx, md: MarkdownWriter, errors: list[Err]) -> None:
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
    import_struct_schema(md, ctx.struct_map["JSONRPCResponse"])
    write_section_end(md)

    # Right Section
    write_right_section(md)

    md.writeln('!!! failure "Error"')
    md.indent()

    md.writeln("**Full Error Response**")
    write_code_block(md, "json")
    resp = ctx.struct_map["JSONRPCResponse"]
    resultField = resp.fields.pop(1)  # Remove Result
    error = errors[0]
    params = ctx.struct_map["Error"]
    params.fields[0].example = f'"{error.code}"'
    params.fields[1].example = f'"{error.message}"'
    write_struct_example_with_generics(
        ctx,
        md,
        resp,
        True,
        True,
        params,
    )
    resp.fields.insert(1, resultField)
    md.writeln("```")

    md.writeln("**Lite Error Response**")
    write_code_block(md, "json")
    resp = ctx.struct_map["JSONRPCResponse"]
    resultField = resp.fields.pop(1)  # Remove Result
    error = errors[0]
    params = ctx.struct_map["Error"]
    params.fields[0].example = f'"{error.code}"'
    params.fields[1].example = f'"{error.message}"'
    write_struct_example_with_generics(
        ctx,
        md,
        resp,
        True,
        False,
        params,
    )
    resp.fields.insert(1, resultField)
    md.writeln("```")

    md.writeln("**Legacy Error Response**")
    write_code_block(md, "json")
    error = errors[0]
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
    error = errors[0]

    md.writeln("**Full Error Response**")
    write_code_block(md, "json")
    md.writeln("{")
    md.indent()
    md.writeln('"request_id":1,')
    md.writeln(f'"code":{error.code},')
    md.writeln(f'"message":"{error.message}",')
    md.writeln(f'"status":{error.status}')
    md.dedent()
    md.writeln("}")
    md.writeln("```")

    md.writeln("**Lite Error Response**")
    write_code_block(md, "json")
    md.writeln("{")
    md.indent()
    md.writeln('"ri":1,')
    md.writeln(f'"c":{error.code},')
    md.writeln(f'"m":"{error.message}",')
    md.writeln(f'"s":{error.status}')
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

    # To allow environment variable injection in the example
    if field.example and "$" in field.example:
        example_value = field.example
    elif field.example and field.json_type == "integer":
        example_value = field.example.replace("'", "")
        example_value = example_value.replace('"', "")
    elif field.example:
        example_value = field.example.replace("'", '"')
    elif field.json_type in ctx.enum_map:
        example_value = '"' + ctx.enum_map[field.json_type].values[0].name + '"'
    else:
        example_value = "null"
        print(f"No example value for field: {struct.name}.{field.name}")  # noqa: T201

    # To allow environment variable injection in the example
    if example_value.startswith("'$"):
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
