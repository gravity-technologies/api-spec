from io import TextIOWrapper


class MarkdownWriter:
    def __init__(self, f: TextIOWrapper) -> None:
        self.f = f
        self.indentation = 0
        self.prefixed = False

    def write(self, s: str) -> None:
        if self.prefixed:
            self.f.write(s)
        else:
            self.f.write("    " * self.indentation + s)
        self.prefixed = True

    def writeln(self, s: str) -> None:
        if self.prefixed:
            self.f.write(s + "\n")
        else:
            self.f.write("    " * self.indentation + s + "\n")
        self.prefixed = False

    def indent(self) -> None:
        self.indentation += 1

    def dedent(self) -> None:
        self.indentation -= 1
