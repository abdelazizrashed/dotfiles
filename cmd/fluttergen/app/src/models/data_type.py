class DataType:

    def __init__(self, dart_type, python_type) -> None:
        self.dart_type = dart_type
        self.python_type = python_type


    def __str__(self) -> str:
        return f"DataType(dart_type={self.dart_type}, python_type={self.python_type})"




