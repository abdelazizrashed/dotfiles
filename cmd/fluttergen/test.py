# import unittest
#
# from app.test.test_parser import TestParser
#
# if __name__ == '__main__':
#     unittest.main()
#

import re

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

def to_snake_case(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower() 


# Examples
print(to_pascal_case("snake_case"))  # Output: SnakeCase
print(to_pascal_case("camelCase"))  # Output: CamelCase
print(to_pascal_case("PascalCase"))  # Output: PascalCase
print(to_snake_case("snake_case"))  # Output: SnakeCase
print(to_snake_case("camelCase"))  # Output: CamelCase
print(to_snake_case("PascalCase"))  # Output: PascalCase

