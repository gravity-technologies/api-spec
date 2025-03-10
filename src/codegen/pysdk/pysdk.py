from io import TextIOWrapper

import inflection

from ..parse.parse import Enum, Field, SpecRoot, Struct


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
    f.write("\n\n")


def semantic_and_json_to_python_type(semantic_type: str, json_type: str) -> str:
    if semantic_type[0].isupper():
        return semantic_type

    type_mapping = {
        "string": "str",
        "int": "int",
        "int8": "int",
        "uint8": "int",
        "int16": "int",
        "uint16": "int",
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
        "any": "Any",
        "[]byte": "bytes",
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

    mandatory = []
    optional = []
    for field in struct.fields:
        if field.optional:
            optional.append(field)
        else:
            mandatory.append(field)
    for field in mandatory:
        write_field(field, f)
    for field in optional:
        write_field(field, f)
    f.write("\n\n")


def write_field(field: Field, f: TextIOWrapper) -> None:
    py_type = semantic_and_json_to_python_type(field.semantic_type, field.json_type)
    for _ in range(field.array_depth):
        py_type = f"list[{py_type}]"
    if field.optional:
        py_type = f"{py_type} | None = None"
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


def write_rpc_api(spec_root: SpecRoot, f: TextIOWrapper, is_async: bool) -> None:
    class_name = "GrvtRawAsync" if is_async else "GrvtRawSync"
    base_class = "GrvtRawAsyncBase" if is_async else "GrvtRawSyncBase"

    f.write("from enum import Enum\n\n")
    f.write("from dacite import Config, from_dict\n\n")
    f.write("from . import grvt_raw_types as types\n")
    f.write(f"from .grvt_raw_base import GrvtApiConfig, GrvtError, {base_class}\n\n")
    f.write('# mypy: disable-error-code="no-any-return"\n\n')
    f.write(f"class {class_name}({base_class}):\n")
    f.write("    def __init__(self, config: GrvtApiConfig):\n")
    f.write("        super().__init__(config)\n")
    f.write("        self.md_rpc = self.env.market_data.rpc_endpoint\n")
    f.write("        self.td_rpc = self.env.trade_data.rpc_endpoint\n\n")

    # Write methods for each RPC
    for i, gateway in enumerate(spec_root.gateways):
        for j, rpc in enumerate(gateway.rpcs):
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
            f.write(
                f"        return from_dict(types.{rpc.response},"
                + " resp, Config(cast=[Enum]))\n"
            )
            if i < len(spec_root.gateways) - 1 or j < len(gateway.rpcs) - 1:
                f.write("\n")


def generate(spec_root: SpecRoot) -> None:
    with open("artifacts/pysdk/grvt_raw_types.py", "w") as f:
        f.write("# ruff: noqa: D200\n")
        f.write("# ruff: noqa: D204\n")
        f.write("# ruff: noqa: D205\n")
        f.write("# ruff: noqa: D404\n")
        f.write("# ruff: noqa: W291\n")
        f.write("# ruff: noqa: D400\n")
        f.write("# ruff: noqa: E501\n")
        f.write("from dataclasses import dataclass\n")
        f.write("from enum import Enum\n")
        f.write("from typing import Any\n\n\n")

        for enum in spec_root.enums:
            write_enum(enum, f)
        for struct in spec_root.structs:
            write_struct(struct, f)

    with open("artifacts/pysdk/grvt_raw_async.py", "w") as f:
        write_rpc_api(spec_root, f, is_async=True)

    with open("artifacts/pysdk/grvt_raw_sync.py", "w") as f:
        write_rpc_api(spec_root, f, is_async=False)
