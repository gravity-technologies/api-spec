import json
from dataclasses import dataclass
from typing import cast

from dataclasses_json import dataclass_json

###########################
# Types (Structs & Enums) #
###########################


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
    selector: str | None


@dataclass_json
@dataclass
class Struct:
    name: str
    is_root: bool
    fields: list[Field]
    comment: list[str]


##########################
# Types (RPCs & Streams) #
##########################


@dataclass_json
@dataclass
class Endpoint:
    name: str
    url: str


@dataclass_json
@dataclass
class Err:
    code: int
    message: str
    status: int


@dataclass_json
@dataclass
class RPC:
    namespace: str
    name: str
    version: int
    route: str
    auth_required: bool
    request: str
    response: str
    on_request_errors: list[Err]


@dataclass_json
@dataclass
class Stream:
    namespace: str
    name: str
    channel: str
    auth_required: bool
    feed_selector: str
    feed: str
    on_subscribe_errors: list[Err]


@dataclass_json
@dataclass
class Gateway:
    name: str
    endpoints: list[Endpoint]
    rpcs: list[RPC]
    streams: list[Stream]


@dataclass_json
@dataclass
class SpecRoot:
    gateways: list[Gateway]
    structs: list[Struct]
    enums: list[Enum]


def parse_spec() -> SpecRoot:
    with open("./src/codegen/apispec.json") as spec_str:
        spec_json = json.load(spec_str)
        return cast(SpecRoot, SpecRoot.from_dict(spec_json, infer_missing=True))  # type: ignore[attr-defined]
