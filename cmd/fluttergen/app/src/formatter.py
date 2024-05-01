class Formatter:
    def __init__(self) -> None:
       self.rows = [] 
       self.padding = ""

    def add_row(self, row: str, no_new_line: bool = False):
        self.rows.append(self.padding + row + ("" if no_new_line else "\n"))

    def add_start(self, row: str, no_new_line: bool = False):
        self.rows.insert(0, self.padding + row + ("" if no_new_line else "\n"))

    def add_padding(self, padding: int):
        self.padding += "\t" * padding
    
    def remove_padding(self, padding: int):
        self.padding = self.padding[:-padding]

    def print(self) -> str:
        out = ""
        for row in self.rows:
            out += row
        return out
