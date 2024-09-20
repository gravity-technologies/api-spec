import json
from dataclasses import dataclass
from typing import cast

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Value:
    name: str
    value: int
    comment: list[str]


@dataclass_json
@dataclass
class Enum:
    name: str
    values: list[Value]
    comment: list[str]


@dataclass_json
@dataclass
class Field:
    name: str
    lite_name: str
    semantic_type: str
    json_type: str
    index: int
    array_depth: int
    optional: bool
    example: str | None
    comment: list[str]


@dataclass_json
@dataclass
class Struct:
    name: str
    is_root: bool
    fields: list[Field]
    comment: list[str]


@dataclass_json
@dataclass
class SpecRoot:
    structs: list[Struct]
    enums: list[Enum]


def parse_spec() -> SpecRoot:
    with open("./src/codegen/apispec.json") as spec_str:
        spec_json = json.load(spec_str)
        return cast(SpecRoot, SpecRoot.from_dict(spec_json, infer_missing=True))  # type: ignore[attr-defined]
