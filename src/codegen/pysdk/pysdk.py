from io import TextIOWrapper

import inflection

from ..parse.parse import Enum, SpecRoot, Struct


def write_enum(enum: Enum, f: TextIOWrapper) -> None:
    f.write(f"class {enum.name}(Enum):\n")
    if enum.comment and len(enum.comment) > 1:
        f.write('    """\n')
        for line in enum.comment:
            if len(line) > 0:
                f.write(f"    {line}\n")
            else:
                f.write("\n")
        f.write('    """\n\n')
    for value in enum.values:
        # If comment exists, write it inline with the field using hash comments
        # if the number of lines exceeds 1, write it as a docstring
        if len(value.comment) > 1:
            f.write('    """\n')
            for line in value.comment:
                if len(line) > 0:
                    f.write(f"    {line}\n")
                else:
                    f.write("\n")
            f.write('    """\n')
            f.write(f'    {value.name} = "{value.name}"\n')
        elif len(value.comment) == 1:
            f.write(f"    # {value.comment[0]}\n")
            f.write(f'    {value.name} = "{value.name}"\n')
        else:
            f.write(f'    {value.name} = "{value.name}"\n')
    f.write("\n")


def semantic_and_json_to_python_type(semantic_type: str, json_type: str) -> str:
    if semantic_type[0].isupper():
        return semantic_type

    type_mapping = {
        "string": "str",
        "int": "int",
        "int8": "int",
        "uint8": "int",
        "int32": "int",
        "uint32": "int",
        "int64": "int",
        "uint64": "int",
        "float32": "float",
        "float64": "float",
        "bool": "bool",
        "timestamp": "int",
        "asset": "str",
        "uint128": "str",
        "uint256": "str",
        "address": "str",
    }

    if semantic_type in type_mapping:
        t = type_mapping[semantic_type]
        if json_type == "string":
            t = "str"
        return t

    print(f"[Warning] Unmapped python type: {semantic_type}")  # noqa: T201
    return semantic_type


def write_struct(struct: Struct, f: TextIOWrapper) -> None:
    f.write("@dataclass\n")
    f.write(f"class {struct.name}:\n")
    if struct.comment and len(struct.comment) > 1:
        f.write('    """\n')
        for line in struct.comment:
            if len(line) > 0:
                f.write(f"    {line}\n")
            else:
                f.write("\n")
        f.write('    """\n\n')
    if len(struct.fields) == 0:
        f.write("    pass\n\n")
        return
    for field in struct.fields:
        py_type = semantic_and_json_to_python_type(field.semantic_type, field.json_type)
        for _ in range(field.array_depth):
            py_type = f"list[{py_type}]"
        if field.optional:
            py_type = f"{py_type} | None"
        # If comment exists, write it inline with the field using hash comments
        # if the number of lines exceeds 1, write it as a docstring
        if len(field.comment) > 1:
            f.write('    """\n')
            for line in field.comment:
                if len(line) > 0:
                    f.write(f"    {line}\n")
                else:
                    f.write("\n")
            f.write('    """\n')
            f.write(f"    {field.name}: {py_type}\n")
        elif len(field.comment) == 1:
            f.write(f"    # {field.comment[0]}\n")
            f.write(f"    {field.name}: {py_type}\n")
        else:
            f.write(f"    {field.name}: {py_type}\n")
    f.write("\n")


# from . import types
# from .grvt_api_base import GrvtApiAsyncBase, GrvtApiConfig, GrvtError


# class GrvtApiAsync(GrvtApiAsyncBase):
#     def __init__(self, config: GrvtApiConfig):
#         super().__init__(config)

#         self.md_rpc = self.env.market_data.rpc_endpoint
#         self.td_rpc = self.env.trade_data.rpc_endpoint

#     async def get_all_instruments(
#         self, req: types.ApiGetAllInstrumentsRequest
#     ) -> types.ApiGetAllInstrumentsResponse | GrvtError:
#         resp = await self._post(False, self.md_rpc + "/full/v1/all_instruments", req)
#         if resp.get("code"):
#             return GrvtError(**resp)
#         return types.ApiGetAllInstrumentsResponse(**resp)

#     async def get_open_orders(
#         self, req: types.ApiOpenOrdersRequest
#     ) -> types.ApiOpenOrdersResponse | GrvtError:
#         resp = await self._post(True, self.td_rpc + "/full/v1/open_orders", req)
#         if resp.get("code"):
#             return GrvtError(**resp)
#         return types.ApiOpenOrdersResponse(**resp)


def write_rpc_api(spec_root: SpecRoot, f: TextIOWrapper, is_async: bool) -> None:
    class_name = "GrvtApiAsync" if is_async else "GrvtApiSync"
    base_class = "GrvtApiAsyncBase" if is_async else "GrvtApiSyncBase"

    f.write("from . import types\n")
    f.write(f"from .grvt_api_base import {base_class}, GrvtApiConfig, GrvtError\n\n\n")

    f.write(f"class {class_name}({base_class}):\n")
    f.write("    def __init__(self, config: GrvtApiConfig):\n")
    f.write("        super().__init__(config)\n")
    f.write("        self.md_rpc = self.env.market_data.rpc_endpoint\n")
    f.write("        self.td_rpc = self.env.trade_data.rpc_endpoint\n")

    # Write methods for each RPC
    for gateway in spec_root.gateways:
        for rpc in gateway.rpcs:
            method_prefix = "async " if is_async else ""
            await_prefix = "await " if is_async else ""
            rpc_var = "md" if gateway.name == "MarketData" else "td"
            func_name = inflection.underscore(rpc.name[3:]).lower()

            f.write(f"    {method_prefix}def {func_name}(\n")
            f.write(f"        self, req: types.{rpc.request}\n")
            f.write(f"    ) -> types.{rpc.response} | GrvtError:\n")
            f.write(
                f"        resp = {await_prefix}self._post({rpc.auth_required},"
                + f' self.{rpc_var}_rpc + "/full/v{rpc.version}{rpc.route}", req)\n'
            )
            f.write('        if resp.get("code"):\n')
            f.write("            return GrvtError(**resp)\n")
            f.write(f"        return types.{rpc.response}(**resp)\n\n")


def generate(spec_root: SpecRoot) -> None:
    with open("artifacts/pysdk/types.py", "w") as f:
        f.write("# ruff: noqa: D200\n")
        f.write("# ruff: noqa: D204\n")
        f.write("# ruff: noqa: D205\n")
        f.write("# ruff: noqa: D404\n")
        f.write("# ruff: noqa: W291\n")
        f.write("# ruff: noqa: D400\n")
        f.write("# ruff: noqa: E501\n")
        f.write("from dataclasses import dataclass\n")
        f.write("from enum import Enum\n\n\n")
        for enum in spec_root.enums:
            write_enum(enum, f)
        for struct in spec_root.structs:
            write_struct(struct, f)

    with open("artifacts/pysdk/grvt_api_async.py", "w") as f:
        write_rpc_api(spec_root, f, is_async=True)

    with open("artifacts/pysdk/grvt_api_sync.py", "w") as f:
        write_rpc_api(spec_root, f, is_async=False)
