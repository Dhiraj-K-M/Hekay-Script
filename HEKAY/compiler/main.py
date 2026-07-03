"""
Hekay Programming Language

Main Entry

Developer: Dhiraj Kumar Mehangiya
"""

import sys

from compiler.lexer.lexer import Lexer
from compiler.parser.parser import Parser
from compiler.interpreter.interpreter import Interpreter


def main():

    if len(sys.argv) < 2:
        print("Usage: python compiler/main.py <file.hky>")
        return

    filename = sys.argv[1]

    with open(filename, "r", encoding="utf-8") as file:
        source = file.read()

    lexer = Lexer(source)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    program = parser.parse()

    interpreter = Interpreter()
    interpreter.execute(program)


if __name__ == "__main__":
    main()