from ..models import DataClass
from ..formatter import Formatter
from ..constants import DART_TYPES
from ..utils import Utils
from typing import List


class Generator:
    def __init__(self, root: DataClass) -> None:
        self.root = root
        self.imports = []

    def g_properties(self, props: List[DataClass], padding: int = 0) -> str:
        formatter = Formatter()
        formatter.add_padding(padding)
        for prop in props:
            if prop.data_type.dart_type not in DART_TYPES:
                if "List" not in prop.data_type.dart_type:
                    self.imports.append(
                        Utils.to_snake_case(prop.data_type.dart_type))
                else:
                    class_name = prop.data_type.dart_type.split("<")[
                        1].split(">")[0]
                    self.imports.append(Utils.to_snake_case(class_name))

            formatter.add_row(Generator.to_property(prop))
        return formatter.print()

    def g_constructor(self, props: List[DataClass], padding: int = 0) -> str:
        formatter = Formatter()
        formatter.add_padding(padding)
        formatter.add_row(f"{self.root.data_type.dart_type}({{")
        formatter.add_padding(1)
        for prop in props:
            formatter.add_row(f"required this.{prop.name},")
        formatter.remove_padding(1)
        formatter.add_row("});")
        return formatter.print()

    def g_from_json(self, props: List[DataClass], padding: int = 0) -> str:
        formatter = Formatter()
        formatter.add_padding(padding)
        formatter.add_row(f"factory {
                          self.root.data_type.dart_type}.fromJson(Map<String, dynamic> json) {{")
        formatter.add_padding(1)
        formatter.add_row(f"return {self.root.data_type.dart_type}(")
        formatter.add_padding(1)
        for prop in props:
            formatter.add_row(Generator.from_json_row(prop))
        formatter.remove_padding(1)
        formatter.add_row(");")
        formatter.remove_padding(1)
        formatter.add_row("}")
        return formatter.print()

    def g_to_json(self, props: List[DataClass], padding: int = 0) -> str:
        formatter = Formatter()
        formatter.add_padding(padding)
        formatter.add_row("Map<String, dynamic> toJson() {")
        formatter.add_padding(1)
        formatter.add_row("return {")
        formatter.add_padding(1)
        for prop in props:
            formatter.add_row(Generator.to_json_row(prop))
        formatter.remove_padding(1)
        formatter.add_row("};")
        formatter.remove_padding(1)
        formatter.add_row("}")
        return formatter.print()

    def g_imports(self) -> str:
        formatter = Formatter()
        formatter.add_row("// ignore_for_file: non_constant_identifier_names")

        for im in self.imports:
            formatter.add_row(f"import '{im}.dart';")
        return formatter.print()

    def generate_code(self):

        formatter = Formatter()
        formatter.add_row(f"class {self.root.data_type.dart_type} {{")
        formatter.add_row("")
        formatter.add_row(self.g_properties(self.root.properties, 1))
        formatter.add_start(self.g_imports())
        formatter.add_row(self.g_constructor(self.root.properties, 1))
        formatter.add_row(self.g_from_json(self.root.properties, 1))
        formatter.add_row(self.g_to_json(self.root.properties, 1))
        formatter.remove_padding(1)
        formatter.add_row("}")

        return formatter.print()

    @staticmethod
    def to_property(data_class: DataClass) -> str:
        return f"final {data_class.data_type.dart_type} {data_class.name};"

    @staticmethod
    def to_json_row(data_class: DataClass) -> str:
        return f"\"{data_class.name}\": {data_class.name},"

    @staticmethod
    def from_json_row(data_class: DataClass) -> str:
        if data_class.data_type.dart_type in DART_TYPES:
            return f"{data_class.name}: json[\"{data_class.name}\"] ?? {data_class.data_type.default_value},"
        if "List" in data_class.data_type.dart_type:
            class_name = data_class.data_type.dart_type.split("<")[
                1].split(">")[0]
            return f"{data_class.name}: {data_class.data_type.dart_type}.from((json[\"{data_class.name}\"] ?? []).map((x) => {class_name}.fromJson(x))),"
        return f"{data_class.name}: {data_class.data_type.dart_type}.fromJson(json[\"{data_class.name}\"]??{{}}),"
