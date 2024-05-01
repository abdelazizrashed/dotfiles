from .data_type import DataType

class DataClass:
    def __init__(self, data_type: DataType, name: str, value ):
        self.data_type = data_type
        self.name = name
        self.properties: list[DataClass] = []
        self.value = value

    def __str__(self) -> str:
        return f"DataClass(data_type={self.data_type}, name={self.name},  properties={[str(p) for p in self.properties]})"

    def copy(self):
         d_class = DataClass(data_type=self.data_type, name=self.name, value=self.value)
         d_class.properties = self.properties
         return d_class

    # def to_property(self) -> str:
    #      return f"final {self.data_type.dart_type} {self.name};"
    #
    # def to_json_row(self) -> str:
    #     return f"{self.name}: this.{self.name},"
    #
    # def from_json_row(self) -> str:
    #     return f"{self.name}: this.{self.name},"
