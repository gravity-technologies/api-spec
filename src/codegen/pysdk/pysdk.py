from io import TextIOWrapper

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
            f.write(f"    {value.name} = {value.value}\n")
        elif len(value.comment) == 1:
            f.write(f"    {value.name} = {value.value}  # {value.comment[0]}\n")
        else:
            f.write(f"    {value.name} = {value.value}\n")
    f.write("\n")


def semantic_to_python_type(semantic_type: str) -> str:
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
        return type_mapping[semantic_type]

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
        py_type = semantic_to_python_type(field.semantic_type)
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
            f.write(f"    {field.name}: {py_type}  # {field.comment[0]}\n")
        else:
            f.write(f"    {field.name}: {py_type}\n")
    f.write("\n")


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
