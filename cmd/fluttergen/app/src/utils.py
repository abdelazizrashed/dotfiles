import re

class Utils:
    
    @staticmethod
    def to_pascal_case(name):
      """Converts a string to PascalCase.

      Args:
        name: The string to convert.

      Returns:
        The string in PascalCase.
      """

      name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower() 

      words = name.split("_")
      words = [word.capitalize() for word in words]
      return "".join(words)

    @staticmethod
    def to_snake_case(name):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower() 
