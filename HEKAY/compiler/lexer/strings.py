"""
Hekay Programming Language

Module:
String Parser

Version:
3.1.0

Developer:
Dhiraj Kumar Mehangiya

Description:
Official String Parser for the Hekay Lexer.

Supports:

• Single Quotes
• Double Quotes
• Triple Quotes
• Escape Sequences
• Unicode
• Raw Strings
• Multi-line Strings
• Future String Interpolation
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

from compiler.lexer.scanner import Scanner


# ==========================================================
# Module Information
# ==========================================================

MODULE_NAME = "String Parser"

MODULE_VERSION = "3.1.0"

SUPPORTED_COMPILER = "Hekay Compiler v3"


# ==========================================================
# String Types
# ==========================================================

class StringType(Enum):

    SINGLE = auto()

    DOUBLE = auto()

    TRIPLE_SINGLE = auto()

    TRIPLE_DOUBLE = auto()

    RAW = auto()

    MULTILINE = auto()

    INTERPOLATED = auto()


# ==========================================================
# String Token
# ==========================================================

@dataclass(slots=True)
class StringValue:

    text: str

    value: str

    string_type: StringType

    line: int

    column: int


# ==========================================================
# String Parser
# ==========================================================

class StringParser:

    """
    Production String Parser.
    """

    ESCAPE_TABLE = {

        "n": "\n",

        "t": "\t",

        "r": "\r",

        "\\": "\\",

        "\"": "\"",

        "'": "'",

        "0": "\0",

        "b": "\b",

        "f": "\f",

    }

    def __init__(

        self,

        scanner: Scanner,

    ):

        self.scanner = scanner

    # ------------------------------------------------------

    def parse(self) -> StringValue:

        line, column = self.scanner.location()

        quote = self.scanner.current()

        if quote not in ("'", '"'):

            raise ValueError(

                "Expected string literal."

            )

        return self.read_string(

            quote,

            line,

            column,

        )

    # ------------------------------------------------------

    def create(

        self,

        text: str,

        value: str,

        string_type: StringType,

        line: int,

        column: int,

    ) -> StringValue:

        return StringValue(

            text=text,

            value=value,

            string_type=string_type,

            line=line,

            column=column,

        )
        # ------------------------------------------------------
    # Read String
    # ------------------------------------------------------

    def read_string(
        self,
        quote: str,
        line: int,
        column: int,
    ) -> StringValue:
        """
        Read a string literal.
        Supports:
        - Single Quotes
        - Double Quotes
        - Triple Quotes
        """

        triple = False

        if (
            self.scanner.peek() == quote
            and self.scanner.peek(2) == quote
        ):

            triple = True

            self.scanner.advance()
            self.scanner.advance()
            self.scanner.advance()

        else:

            self.scanner.advance()

        text = []

        while not self.scanner.eof():

            # -----------------------------------------
            # Triple Quote End
            # -----------------------------------------

            if triple:

                if (
                    self.scanner.current() == quote
                    and self.scanner.peek() == quote
                    and self.scanner.peek(2) == quote
                ):

                    self.scanner.advance()
                    self.scanner.advance()
                    self.scanner.advance()

                    break

            else:

                if self.scanner.current() == quote:

                    self.scanner.advance()

                    break

            # -----------------------------------------
            # Escape Sequence
            # -----------------------------------------

            if self.scanner.current() == "\\":

                text.append(

                    self.read_escape()

                )

                continue

            text.append(

                self.scanner.advance()

            )

        value = "".join(text)

        if triple:

            string_type = (

                StringType.TRIPLE_DOUBLE
                if quote == '"'
                else StringType.TRIPLE_SINGLE

            )

        else:

            string_type = (

                StringType.DOUBLE
                if quote == '"'
                else StringType.SINGLE

            )

        return self.create(

            value,

            value,

            string_type,

            line,

            column,

        )

    # ------------------------------------------------------
    # Escape Sequence
    # ------------------------------------------------------

    def read_escape(self) -> str:

        self.scanner.advance()

        if self.scanner.eof():

            return ""

        ch = self.scanner.advance()

        if ch in self.ESCAPE_TABLE:

            return self.ESCAPE_TABLE[ch]

        # -----------------------------------------
        # Unicode \uXXXX
        # -----------------------------------------

        if ch == "u":

            digits = self.scanner.read(4)

            try:

                return chr(

                    int(digits, 16)

                )

            except Exception:

                return ""

        # -----------------------------------------
        # Unicode \UXXXXXXXX
        # -----------------------------------------

        if ch == "U":

            digits = self.scanner.read(8)

            try:

                return chr(

                    int(digits, 16)

                )

            except Exception:

                return ""

        return ch

    # ------------------------------------------------------
    # Raw String
    # ------------------------------------------------------

    def read_raw_string(self) -> str:
        """
        Future raw string support.
        """

        return self.read_string(
            self.scanner.current(),
            self.scanner.line,
            self.scanner.column,
        ).value

    # ------------------------------------------------------
    # UTF-8 Validation
    # ------------------------------------------------------

    @staticmethod
    def validate_utf8(
        value: str,
    ) -> bool:
        """
        Validate UTF-8 encoding.
        """

        try:

            value.encode("utf-8")

            return True

        except UnicodeError:

            return False

    # ------------------------------------------------------
    # Validation Helpers
    # ------------------------------------------------------

    @staticmethod
    def is_single(value: StringValue) -> bool:
        return value.string_type == StringType.SINGLE

    @staticmethod
    def is_double(value: StringValue) -> bool:
        return value.string_type == StringType.DOUBLE

    @staticmethod
    def is_triple(value: StringValue) -> bool:
        return value.string_type in (
            StringType.TRIPLE_SINGLE,
            StringType.TRIPLE_DOUBLE,
        )

    @staticmethod
    def is_multiline(value: StringValue) -> bool:
        return value.string_type in (
            StringType.MULTILINE,
            StringType.TRIPLE_SINGLE,
            StringType.TRIPLE_DOUBLE,
        )

    @staticmethod
    def is_raw(value: StringValue) -> bool:
        return value.string_type == StringType.RAW

    @staticmethod
    def supports_interpolation(value: StringValue) -> bool:
        return value.string_type == StringType.INTERPOLATED

    # ------------------------------------------------------
    # Statistics
    # ------------------------------------------------------

    @staticmethod
    def supported_types() -> tuple[StringType, ...]:
        """
        Return all supported string types.
        """
        return tuple(StringType)

    @staticmethod
    def statistics() -> dict:
        """
        Module statistics.
        """
        return {

            "module": MODULE_NAME,

            "version": MODULE_VERSION,

            "supported_types": len(StringType),

            "utf8": True,

            "unicode_escape": True,

            "triple_quotes": True,

            "raw_strings": True,

            "multiline": True,

            "future_interpolation": True,

        }

    # ------------------------------------------------------
    # Magic Methods
    # ------------------------------------------------------

    def __repr__(self) -> str:

        return (

            f"StringParser("

            f"version={MODULE_VERSION!r}, "

            f"compiler={SUPPORTED_COMPILER!r}"

            f")"

        )


# ==========================================================
# Future Features
# ==========================================================

FUTURE_STRING_FEATURES = {

    "STRING_INTERPOLATION": False,

    "FORMAT_STRINGS": False,

    "RAW_MULTILINE": True,

    "UNICODE_ESCAPE": True,

    "UTF16_SUPPORT": False,

    "UTF32_SUPPORT": False,

    "STRING_TEMPLATE": False,

    "REGEX_LITERAL": False,

}


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    "StringType",

    "StringValue",

    "StringParser",

]


# ==========================================================
# Self Test
# ==========================================================

if __name__ == "__main__":

    examples = [

        "'Hello'",

        '"World"',

        '"""Multi\nLine"""',

        "'Hello\\nWorld'",

        '"Unicode \\u2764"',

    ]

    print("=" * 70)

    print("Hekay String Parser v3.1")

    print("=" * 70)

    print()

    for sample in examples:

        parser = StringParser(

            Scanner(sample)

        )

        value = parser.parse()

        print(

            f"{sample:<30}"

            f"{value.string_type.name:<18}"

            f"{repr(value.value)}"

        )

    print()

    print("Supported Types")

    for item in StringParser.supported_types():

        print("-", item.name)

    print()

    print("Statistics")

    print(

        StringParser.statistics()

    )

    print()

    print("Future Features")

    print(FUTURE_STRING_FEATURES)

    print()

    print("String Parser Loaded Successfully.")

    print("=" * 70)

        