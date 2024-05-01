class PrintStack:

    def __init__(self) -> None:
       self.stack = []

    def push(self, name: str):
        self.stack.append(name)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def __str__(self) -> str:
        return str(self.stack)

    def print(self)-> str:
        out = ""
        while len(self.stack) > 0:
            row = self.pop()
            if row:
                out += row
        return out
