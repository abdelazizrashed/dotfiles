from ..models import DataClass, DataType
from typing import List
from ..utils import Utils


class Parser:

    def __init__(self, name: str, value, module_prefix: str, add_module_prefix: bool = False) -> None:
        self.name = name
        self.value = value
        self.module_prefix = module_prefix
        self.add_module_prefix = add_module_prefix
        if not add_module_prefix:
            self.module_name = name
        else:
            self.module_name = module_prefix + "_" + name
        self.data_type = self.parse_type(value, name, add_module_prefix)

    def parse_data(self) -> List[DataClass]:
        root = DataClass(
            data_type=self.data_type,
            name=self.name,
            value=self.value,
        )
        data_classes = [root]
        for key, value in self.value.items():
            d_type = self.parse_type(value, key, True)
            d_class = DataClass(data_type=d_type, name=key, value=value)
            default_type, default_val = self.type_parser(value)
            if len(default_type) == 0 and (type(value) == list or type(value) == dict):
                if type(value) == dict:
                    parser = Parser(key, value, self.module_prefix, True)
                    data_classes.extend(parser.parse_data())
                elif len(value) > 0 and type(value[0]) == dict:
                    parser = Parser(key, value[0], self.module_prefix, True)
                    data_classes.extend(parser.parse_data())

            root.properties.append(d_class)
        return data_classes

    # def format_class_name(self, name: str, add_module_prefix: bool = False) -> str:
    #     out = ""
    #     if add_module_prefix:
    #         out += self.module_prefix + "_"
    #     out += name
    #     out += "_model"
    #     print(out)
    #     return self.to_pascal_case(out)

    # def to_pascal_case(self, name: str) -> str:
    #     return "".join([n.capitalize() for n in name.split("_")])

    def parse_type(self, value, name: str, add_module_prefix: bool = False) -> DataType:
        p_type = type(value).__name__
        d_type, default_val = self.type_parser(value)
        if len(d_type) == 0:
            if p_type == "list":
                d_type = self.list_parser(value, name)
                default_val = "[]"
            else:
                class_name = ""
                if add_module_prefix:
                    class_name = self.module_prefix + "_"
                class_name += name + "_model"
                d_type = Utils.to_pascal_case(class_name)
                default_val = "{}"
        return DataType(d_type, p_type, default_val)

    def list_parser(self, value, name: str) -> str:
        if len(value) == 0:
            return "List<dynamic>"
        first = value[0]
        f_type, _ = self.type_parser(first)
        if len(f_type) != 0:
            return f"List<{f_type}>"
        child_type = Utils.to_pascal_case(
            self.module_prefix + "_" + name + "_model")
        return f"List<{child_type}>"

    def type_parser(self, value) -> str:
        d_type = type(value).__name__
        if not value:
            return "dynamic", "\"\""
        if d_type == "str":
            return "String",  "\"\""
        elif d_type == "int":
            return "int", "0"
        elif d_type == "float":
            return "double", "0.0"
        elif d_type == "bool":
            return "bool", "false"
        else:
            return "", ""

    @staticmethod
    def to_property(data_class: DataClass) -> str:
        return f"final {data_class.data_type.dart_type} {data_class.name};"

    @staticmethod
    def to_json_row(data_class: DataClass) -> str:
        return f"{data_class.name}: this.{data_class.name},"

    @staticmethod
    def from_json_row(data_class: DataClass) -> str:
        return f"{data_class.name}: this.{data_class.name},"
