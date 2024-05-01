from . import Generator
from ..models import DataClass
from ..formatter import Formatter
from typing import List
from ..utils import Utils

class JsonAnnotationGenerator(Generator):

    def __init__(self, root: DataClass) -> None:
        super().__init__(root)


    def g_imports(self) ->str:
        formatter = Formatter()
        for im in self.imports:
            formatter.add_row(f"import '{im}.dart';")
        formatter.add_row("")
        formatter.add_row("import 'package:json_annotation/json_annotation.dart';")
        formatter.add_row("")
        formatter.add_row(f"part '{Utils.to_snake_case(self.root.data_type.dart_type)}.g.dart';")
        formatter.add_row("")
        formatter.add_row("@JsonSerializable()")
        return formatter.print()


    def g_from_json(self, props: List[DataClass], padding: int = 0)-> str:
        formatter = Formatter()
        formatter.add_padding(padding)
        formatter.add_row( f"factory {self.root.data_type.dart_type}.fromJson(Map<String, dynamic> json) =>")

        formatter.add_padding(1)
        formatter.add_row( f"_${self.root.data_type.dart_type}FromJson(json);")
        return formatter.print()


    def g_to_json(self, props: List[DataClass], padding: int = 0)-> str:
        formatter = Formatter()
        formatter.add_padding(padding)
        formatter.add_row( f"Map<String, dynamic> toJson() => _${self.root.data_type.dart_type}ToJson(this);")
        return formatter.print()

