"""
Hekay Programming Language

Module:
Scanner

Version:
3.1.0

Developer:
Dhiraj Kumar Mehangiya

Description:
Production Scanner Engine for Hekay Compiler.
Reads source code character by character and
provides utilities for the Lexer.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional


# ==========================================================
# Module Information
# ==========================================================

MODULE_NAME = "Scanner"

MODULE_VERSION = "3.1.0"

SUPPORTED_COMPILER = "Hekay Compiler v3"


# ==========================================================
# Scanner
# ==========================================================

class Scanner:
    """
    Reads Hekay source code character by character.
    """

    def __init__(
        self,
        source: str,
        filename: str = "<memory>",
    ):

        self.source = source

        self.filename = filename

        self.length = len(source)

        self.position = 0

        self.line = 1

        self.column = 1

    # ------------------------------------------------------

    def eof(self) -> bool:
        """
        End of file?
        """
        return self.position >= self.length

    # ------------------------------------------------------

    def current(self) -> str:
        """
        Current character.
        """

        if self.eof():

            return "\0"

        return self.source[self.position]

    # ------------------------------------------------------

    def peek(
        self,
        offset: int = 1,
    ) -> str:
        """
        Look ahead.
        """

        pos = self.position + offset

        if pos >= self.length:

            return "\0"

        return self.source[pos]

    # ------------------------------------------------------

    def previous(self) -> str:

        if self.position == 0:

            return "\0"

        return self.source[self.position - 1]

    # ------------------------------------------------------

    def advance(self) -> str:
        """
        Move forward.
        """

        ch = self.current()

        self.position += 1

        if ch == "\n":

            self.line += 1

            self.column = 1

        else:

            self.column += 1

        return ch

    # ------------------------------------------------------

    def match(
        self,
        expected: str,
    ) -> bool:
        """
        Match expected character.
        """

        if self.current() != expected:

            return False

        self.advance()

        return True

    # ------------------------------------------------------

    def remaining(self) -> str:
        """
        Remaining source.
        """

        return self.source[self.position:]

    # ------------------------------------------------------

    def reset(self):

        self.position = 0

        self.line = 1

        self.column = 1

    # ------------------------------------------------------

    def location(self) -> tuple[int, int]:

        return (

            self.line,

            self.column,

        )

    # ------------------------------------------------------

    @classmethod
    def from_file(
        cls,
        path: str,
    ) -> "Scanner":

        text = Path(path).read_text(
            encoding="utf-8"
        )

        return cls(

            text,

            filename=path,

        )
        # ------------------------------------------------------
    # Skip Whitespace
    # ------------------------------------------------------

    def skip_whitespace(self) -> None:
        """
        Skip spaces, tabs and newlines.
        """

        while not self.eof():

            if self.current() in (" ", "\t", "\r", "\n"):

                self.advance()

            else:

                break

    # ------------------------------------------------------
    # Skip Line
    # ------------------------------------------------------

    def skip_line(self) -> None:
        """
        Skip current line.
        """

        while not self.eof():

            if self.advance() == "\n":

                break

    # ------------------------------------------------------
    # Skip Single Line Comment
    # ------------------------------------------------------

    def skip_comment(self) -> None:
        """
        Skip single-line comment starting with '#'.
        """

        if self.current() == "#":

            self.skip_line()

    # ------------------------------------------------------
    # Skip Multi Line Comment
    # ------------------------------------------------------

    def skip_multiline_comment(self) -> None:
        """
        Skip /* ... */ comments.
        """

        if self.current() != "/" or self.peek() != "*":

            return

        self.advance()
        self.advance()

        while not self.eof():

            if self.current() == "*" and self.peek() == "/":

                self.advance()
                self.advance()

                return

            self.advance()

    # ------------------------------------------------------
    # Read While
    # ------------------------------------------------------

    def read_while(self, condition) -> str:
        """
        Read characters while condition is True.
        """

        result = []

        while not self.eof() and condition(self.current()):

            result.append(self.advance())

        return "".join(result)

    # ------------------------------------------------------
    # Read Identifier
    # ------------------------------------------------------

    def read_identifier(self) -> str:
        """
        Read variable/function/class names.
        """

        return self.read_while(

            lambda c: c.isalnum() or c == "_"

        )

    # ------------------------------------------------------
    # Read Number
    # ------------------------------------------------------

    def read_number(self) -> str:
        """
        Read integer or float number.
        """

        decimal_found = False

        number = []

        while not self.eof():

            ch = self.current()

            if ch.isdigit():

                number.append(self.advance())

                continue

            if ch == "." and not decimal_found:

                decimal_found = True

                number.append(self.advance())

                continue

            break

        return "".join(number)

    # ------------------------------------------------------
    # Read String
    # ------------------------------------------------------

    def read_string(self) -> str:
        """
        Read quoted string.
        """

        quote = self.current()

        self.advance()

        text = []

        while not self.eof():

            ch = self.current()

            if ch == quote:

                self.advance()

                break

            if ch == "\\":

                self.advance()

                if not self.eof():

                    text.append(self.advance())

                continue

            text.append(self.advance())

        return "".join(text)

    # ------------------------------------------------------
    # Read Until
    # ------------------------------------------------------

    def read_until(
        self,
        stop: str,
    ) -> str:
        """
        Read until stop character.
        """

        data = []

        while not self.eof():

            if self.current() == stop:

                break

            data.append(

                self.advance()

            )

        return "".join(data)

    # ------------------------------------------------------
    # Read Exact Characters
    # ------------------------------------------------------

    def read(self, count: int) -> str:
        """
        Read fixed number of characters.
        """

        data = []

        for _ in range(count):

            if self.eof():

                break

            data.append(

                self.advance()

            )

        return "".join(data)

        # ------------------------------------------------------
    # Save Scanner State
    # ------------------------------------------------------

    def save_state(self) -> tuple[int, int, int]:
        """
        Save current scanner state.
        """

        return (
            self.position,
            self.line,
            self.column,
        )

    # ------------------------------------------------------
    # Restore Scanner State
    # ------------------------------------------------------

    def restore_state(
        self,
        state: tuple[int, int, int],
    ) -> None:
        """
        Restore scanner state.
        """

        self.position, self.line, self.column = state

    # ------------------------------------------------------
    # Character Classification
    # ------------------------------------------------------

    def is_identifier_start(self) -> bool:
        ch = self.current()
        return ch.isalpha() or ch == "_"

    def is_identifier_part(self) -> bool:
        ch = self.current()
        return ch.isalnum() or ch == "_"

    def is_digit(self) -> bool:
        return self.current().isdigit()

    def is_hex_digit(self) -> bool:
        return self.current().lower() in "0123456789abcdef"

    def is_binary_digit(self) -> bool:
        return self.current() in ("0", "1")

    # ------------------------------------------------------
    # Position Information
    # ------------------------------------------------------

    def position_info(self) -> dict:
        """
        Return scanner position information.
        """

        return {

            "file": self.filename,

            "line": self.line,

            "column": self.column,

            "position": self.position,

            "remaining": self.length - self.position,

        }

    # ------------------------------------------------------
    # Scanner Statistics
    # ------------------------------------------------------

    @property
    def scanned_characters(self) -> int:
        return self.position

    @property
    def remaining_characters(self) -> int:
        return self.length - self.position

    @property
    def progress(self) -> float:

        if self.length == 0:

            return 100.0

        return round(

            (self.position / self.length) * 100,

            2,

        )

    # ------------------------------------------------------
    # Magic Methods
    # ------------------------------------------------------

    def __len__(self) -> int:

        return self.length

    def __repr__(self) -> str:

        return (

            f"Scanner("

            f"file={self.filename!r}, "

            f"line={self.line}, "

            f"column={self.column}, "

            f"position={self.position}"

            f")"

        )


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    "Scanner",

]

# ==========================================================
# Self Test
# ==========================================================

if __name__ == "__main__":

    demo = """

het x = 10

show(x)

# comment

"""

    scanner = Scanner(demo)

    print("=" * 70)

    print("Hekay Scanner v3.1")

    print("=" * 70)

    print()

    print("Module")

    print(MODULE_NAME)

    print()

    print("Version")

    print(MODULE_VERSION)

    print()

    print("Compiler")

    print(SUPPORTED_COMPILER)

    print()

    print("Scanner Information")

    print(scanner)

    print()

    print("Characters")

    while not scanner.eof():

        print(

            repr(scanner.advance()),

            scanner.location(),

        )

    print()

    print("Progress")

    print(scanner.progress, "%")

    print()

    print("Position Info")

    print(scanner.position_info())

    print()

    print("Scanner Loaded Successfully.")

    print("=" * 70)

    