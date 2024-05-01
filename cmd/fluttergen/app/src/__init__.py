import json
from .parsers import Parser
from .generators import Generator, JsonAnnotationGenerator

def generate_data_classes(file: str, is_json_serializer: bool = False):
    module_name = file.split(".json")[0]
    data:dict = json.load(open(file))
    parser = Parser(module_name, data, module_name)
    res = parser.parse_data()
    for r in res:
        generator = Generator(r)
        if is_json_serializer:
            generator = JsonAnnotationGenerator(r)
        code = generator.generate_code()
        file_name = ""
        if module_name == r.name:
            file_name = f"{module_name}_model.dart"
        else:
            file_name = f"{module_name}_{r.name}_model.dart"
        with open (file_name, "w") as f:
            f.write(code)
