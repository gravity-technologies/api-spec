from ..parse.parse import Enum, SpecRoot, Struct


class CodegenCtx:
    def __init__(self, spec: SpecRoot):
        self.spec = spec
        self.enum_map: dict[str, Enum] = self._create_enum_map()
        self.struct_map: dict[str, Struct] = self._create_struct_map()

    def _create_enum_map(self) -> dict[str, Enum]:
        enum_map = {}
        for enum in self.spec.enums:
            enum_map[enum.name] = enum
        return enum_map

    def _create_struct_map(self) -> dict[str, Struct]:
        struct_map = {}
        for struct in self.spec.structs:
            struct_map[struct.name] = struct
        return struct_map
