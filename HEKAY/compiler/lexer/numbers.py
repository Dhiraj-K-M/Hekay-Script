"""
Hekay Programming Language

Module:
Number Parser

Version:
3.1.0

Developer:
Dhiraj Kumar Mehangiya

Description:
Official Number Parser for the Hekay Lexer.

Supports:

• Decimal
• Float
• Binary
• Octal
• Hexadecimal
• Scientific Notation
• Digit Separators
• Big Integers
• Future Decimal Numbers
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from enum import Enum, auto
from typing import Optional

from compiler.lexer.scanner import Scanner


# ==========================================================
# Module Information
# ==========================================================

MODULE_NAME = "Number Parser"

MODULE_VERSION = "3.1.0"

SUPPORTED_COMPILER = "Hekay Compiler v3"


# ==========================================================
# Number Types
# ==========================================================

class NumberType(Enum):

    INTEGER = auto()

    FLOAT = auto()

    BINARY = auto()

    OCTAL = auto()

    HEXADECIMAL = auto()

    SCIENTIFIC = auto()

    BIG_INTEGER = auto()

    DECIMAL = auto()


# ==========================================================
# Number Token
# ==========================================================

@dataclass(slots=True)
class NumberValue:

    text: str

    value: object

    number_type: NumberType

    line: int

    column: int


# ==========================================================
# Number Parser
# ==========================================================

class NumberParser:

    """
    Production Number Parser.
    """

    BIG_INTEGER_LIMIT = 18

    def __init__(

        self,

        scanner: Scanner,

    ):

        self.scanner = scanner

    # ------------------------------------------------------

    def parse(self) -> NumberValue:

        ch = self.scanner.current()

        if ch == "0":

            nxt = self.scanner.peek().lower()

            if nxt == "b":

                return self.read_binary()

            if nxt == "o":

                return self.read_octal()

            if nxt == "x":

                return self.read_hexadecimal()

        return self.read_decimal()

    # ------------------------------------------------------

    def create(

        self,

        text: str,

        value,

        number_type: NumberType,

        line: int,

        column: int,

    ) -> NumberValue:

        return NumberValue(

            text=text,

            value=value,

            number_type=number_type,

            line=line,

            column=column,

        )

    # ------------------------------------------------------

    @staticmethod

    def remove_separators(

        text: str,

    ) -> str:

        return text.replace("_", "")

        # ------------------------------------------------------
    # Decimal / Float / Scientific
    # ------------------------------------------------------

    def read_decimal(self) -> NumberValue:
        """
        Read decimal, float or scientific notation.
        """

        line, column = self.scanner.location()

        text = []

        has_dot = False
        has_exponent = False

        while not self.scanner.eof():

            ch = self.scanner.current()

            if ch.isdigit():

                text.append(self.scanner.advance())

                continue

            if ch == "_":

                text.append(self.scanner.advance())

                continue

            if ch == "." and not has_dot:

                has_dot = True

                text.append(self.scanner.advance())

                continue

            if ch in ("e", "E") and not has_exponent:

                has_exponent = True

                text.append(self.scanner.advance())

                if self.scanner.current() in ("+", "-"):

                    text.append(self.scanner.advance())

                continue

            break

        source = "".join(text)

        cleaned = self.remove_separators(source)

        if has_exponent:

            return self.create(

                source,

                float(cleaned),

                NumberType.SCIENTIFIC,

                line,

                column,

            )

        if has_dot:

            return self.create(

                source,

                float(cleaned),

                NumberType.FLOAT,

                line,

                column,

            )

        value = int(cleaned)

        number_type = (

            NumberType.BIG_INTEGER

            if len(cleaned) > self.BIG_INTEGER_LIMIT

            else NumberType.INTEGER

        )

        return self.create(

            source,

            value,

            number_type,

            line,

            column,

        )

    # ------------------------------------------------------
    # Binary
    # ------------------------------------------------------

    def read_binary(self) -> NumberValue:

        line, column = self.scanner.location()

        self.scanner.advance()  # 0
        self.scanner.advance()  # b

        digits = []

        while not self.scanner.eof():

            ch = self.scanner.current()

            if ch in ("0", "1", "_"):

                digits.append(self.scanner.advance())

                continue

            break

        source = "0b" + "".join(digits)

        cleaned = "".join(digits).replace("_", "")

        return self.create(

            source,

            int(cleaned, 2),

            NumberType.BINARY,

            line,

            column,

        )

    # ------------------------------------------------------
    # Octal
    # ------------------------------------------------------

    def read_octal(self) -> NumberValue:

        line, column = self.scanner.location()

        self.scanner.advance()
        self.scanner.advance()

        digits = []

        while not self.scanner.eof():

            ch = self.scanner.current()

            if ch in "01234567_":

                digits.append(self.scanner.advance())

                continue

            break

        source = "0o" + "".join(digits)

        cleaned = "".join(digits).replace("_", "")

        return self.create(

            source,

            int(cleaned, 8),

            NumberType.OCTAL,

            line,

            column,

        )

    # ------------------------------------------------------
    # Hexadecimal
    # ------------------------------------------------------

    def read_hexadecimal(self) -> NumberValue:

        line, column = self.scanner.location()

        self.scanner.advance()
        self.scanner.advance()

        digits = []

        while not self.scanner.eof():

            ch = self.scanner.current()

            if ch.lower() in "0123456789abcdef_":

                digits.append(self.scanner.advance())

                continue

            break

        source = "0x" + "".join(digits)

        cleaned = "".join(digits).replace("_", "")

        return self.create(

            source,

            int(cleaned, 16),

            NumberType.HEXADECIMAL,

            line,

            column,

        )

    # ------------------------------------------------------
    # Decimal (Future)
    # ------------------------------------------------------

    def read_decimal128(
        self,
        text: str,
    ) -> Decimal:
        """
        Future high-precision decimal support.
        """

        return Decimal(

            self.remove_separators(text)

        )
        # ------------------------------------------------------
    # Validation Helpers
    # ------------------------------------------------------

    @staticmethod
    def is_integer(value: NumberValue) -> bool:
        return value.number_type in (
            NumberType.INTEGER,
            NumberType.BIG_INTEGER,
        )

    @staticmethod
    def is_float(value: NumberValue) -> bool:
        return value.number_type == NumberType.FLOAT

    @staticmethod
    def is_scientific(value: NumberValue) -> bool:
        return value.number_type == NumberType.SCIENTIFIC

    @staticmethod
    def is_binary(value: NumberValue) -> bool:
        return value.number_type == NumberType.BINARY

    @staticmethod
    def is_octal(value: NumberValue) -> bool:
        return value.number_type == NumberType.OCTAL

    @staticmethod
    def is_hexadecimal(value: NumberValue) -> bool:
        return value.number_type == NumberType.HEXADECIMAL

    @staticmethod
    def is_decimal(value: NumberValue) -> bool:
        return value.number_type == NumberType.DECIMAL

    # ------------------------------------------------------
    # Statistics
    # ------------------------------------------------------

    @staticmethod
    def supported_types() -> tuple[NumberType, ...]:

        return tuple(NumberType)

    @staticmethod
    def statistics() -> dict:

        return {

            "module": MODULE_NAME,

            "version": MODULE_VERSION,

            "supported_formats": len(NumberType),

            "supports_decimal": True,

            "supports_float": True,

            "supports_binary": True,

            "supports_octal": True,

            "supports_hexadecimal": True,

            "supports_scientific": True,

            "supports_big_integer": True,

        }

    # ------------------------------------------------------
    # Magic Methods
    # ------------------------------------------------------

    def __repr__(self) -> str:

        return (

            f"NumberParser("

            f"version={MODULE_VERSION!r}, "

            f"compiler={SUPPORTED_COMPILER!r}"

            f")"

        )


# ==========================================================
# Future Hooks
# ==========================================================

FUTURE_NUMBER_FEATURES = {

    "BIG_FLOAT": False,

    "ARBITRARY_PRECISION": False,

    "COMPLEX_NUMBER": False,

    "RATIONAL_NUMBER": False,

    "UNSIGNED_INTEGER": False,

    "DECIMAL128": True,

    "DECIMAL256": False,

}


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    "NumberType",

    "NumberValue",

    "NumberParser",

]


# ==========================================================
# Self Test
# ==========================================================

if __name__ == "__main__":

    samples = [

        "123",

        "3.14159",

        "0b101011",

        "0o755",

        "0xFF",

        "1.5e10",

        "1_000_000",

        "999999999999999999999999",

    ]

    print("=" * 70)

    print("Hekay Number Parser v3.1")

    print("=" * 70)

    print()

    for sample in samples:

        parser = NumberParser(

            Scanner(sample)

        )

        number = parser.parse()

        print(

            f"{sample:<28}"

            f"{number.number_type.name:<16}"

            f"{number.value}"

        )

    print()

    print("Supported Types")

    for item in NumberParser.supported_types():

        print("-", item.name)

    print()

    print("Statistics")

    print(

        NumberParser.statistics()

    )

    print()

    print("Future Features")

    print(FUTURE_NUMBER_FEATURES)

    print()

    print("Number Parser Loaded Successfully.")

    print("=" * 70)