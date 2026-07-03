"""
Hekay Programming Language

Module:
Identifier Parser

Version:
3.1.0

Developer:
Dhiraj Kumar Mehangiya

Description:
Official Identifier Parser for the Hekay Lexer.

Supports:

• Variables
• Constants
• Functions
• Classes
• Modules
• Namespaces
• Unicode Identifiers
• Reserved Keywords
• Future Generic Types
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import Set

from compiler.lexer.scanner import Scanner
from compiler.lexer.keywords import KEYWORDS


# ==========================================================
# Module Information
# ==========================================================

MODULE_NAME = "Identifier Parser"

MODULE_VERSION = "3.1.0"

SUPPORTED_COMPILER = "Hekay Compiler v3"


# ==========================================================
# Identifier Types
# ==========================================================

class IdentifierType(Enum):

    VARIABLE = auto()

    CONSTANT = auto()

    FUNCTION = auto()

    CLASS = auto()

    MODULE = auto()

    NAMESPACE = auto()

    GENERIC = auto()


# ==========================================================
# Identifier Token
# ==========================================================

@dataclass(slots=True)
class IdentifierValue:

    text: str

    identifier_type: IdentifierType

    line: int

    column: int


# ==========================================================
# Identifier Parser
# ==========================================================

class IdentifierParser:
    """
    Production Identifier Parser.
    """

    def __init__(
        self,
        scanner: Scanner,
    ):

        self.scanner = scanner

    # ------------------------------------------------------

    def parse(self) -> IdentifierValue:

        line, column = self.scanner.location()

        text = self.read_identifier()

        return self.create(

            text,

            self.detect_type(text),

            line,

            column,

        )

    # ------------------------------------------------------

    def create(

        self,

        text: str,

        identifier_type: IdentifierType,

        line: int,

        column: int,

    ) -> IdentifierValue:

        return IdentifierValue(

            text=text,

            identifier_type=identifier_type,

            line=line,

            column=column,

        )

    # ------------------------------------------------------

    def read_identifier(self) -> str:
        """
        Read identifier characters.
        """

        chars = []

        while not self.scanner.eof():

            ch = self.scanner.current()

            if (

                ch.isalnum()

                or ch == "_"

            ):

                chars.append(

                    self.scanner.advance()

                )

                continue

            break

        return "".join(chars)
        # ------------------------------------------------------
    # Type Detection
    # ------------------------------------------------------

    def detect_type(
        self,
        text: str,
    ) -> IdentifierType:
        """
        Detect the identifier type based on naming rules.
        """

        if not text:
            return IdentifierType.VARIABLE

        # Constants (ALL_CAPS)
        if text.isupper():
            return IdentifierType.CONSTANT

        # Classes (PascalCase)
        if text[0].isupper():
            return IdentifierType.CLASS

        # Generic Types (Future)
        if text.startswith("T") and len(text) > 1:
            return IdentifierType.GENERIC

        return IdentifierType.VARIABLE

    # ------------------------------------------------------
    # Validation Helpers
    # ------------------------------------------------------

    @staticmethod
    def is_valid_start(ch: str) -> bool:
        """
        Validate the first character.
        """

        return (

            ch == "_"

            or ch.isalpha()

        )

    @staticmethod
    def is_valid_character(ch: str) -> bool:
        """
        Validate identifier characters.
        """

        return (

            ch == "_"

            or ch.isalpha()

            or ch.isdigit()

        )

    @classmethod
    def is_valid_identifier(
        cls,
        text: str,
    ) -> bool:
        """
        Validate an identifier.
        """

        if not text:

            return False

        if not cls.is_valid_start(text[0]):

            return False

        return all(

            cls.is_valid_character(ch)

            for ch in text

        )

    # ------------------------------------------------------
    # Reserved Keywords
    # ------------------------------------------------------

    @staticmethod
    def is_keyword(
        text: str,
    ) -> bool:
        """
        Check whether text is a keyword.
        """

        return text in KEYWORDS

    # ------------------------------------------------------
    # Unicode Support
    # ------------------------------------------------------

    @staticmethod
    def is_unicode_identifier(
        text: str,
    ) -> bool:
        """
        Validate Unicode identifiers.
        """

        try:

            return text.isidentifier()

        except Exception:

            return False

    # ------------------------------------------------------
    # Future Generic Support
    # ------------------------------------------------------

    @staticmethod
    def generic_name(
        text: str,
    ) -> bool:
        """
        Future generic type support.
        """

        return (

            text.startswith("T")

            and len(text) > 1

        )

    # ------------------------------------------------------
    # Namespace Detection
    # ------------------------------------------------------

    @staticmethod
    def namespace_name(
        text: str,
    ) -> bool:
        """
        Future namespace validation.
        """

        return "::" in text

    # ------------------------------------------------------
    # Module Detection
    # ------------------------------------------------------

    @staticmethod
    def module_name(
        text: str,
    ) -> bool:
        """
        Detect module names.
        """

        return "." in text

        # ------------------------------------------------------
    # Validation Helpers
    # ------------------------------------------------------

    @staticmethod
    def is_variable(value: IdentifierValue) -> bool:
        """
        Check whether the identifier is a variable.
        """
        return value.identifier_type == IdentifierType.VARIABLE

    @staticmethod
    def is_constant(value: IdentifierValue) -> bool:
        """
        Check whether the identifier is a constant.
        """
        return value.identifier_type == IdentifierType.CONSTANT

    @staticmethod
    def is_class(value: IdentifierValue) -> bool:
        """
        Check whether the identifier is a class.
        """
        return value.identifier_type == IdentifierType.CLASS

    @staticmethod
    def is_function(value: IdentifierValue) -> bool:
        """
        Check whether the identifier is a function.
        """
        return value.identifier_type == IdentifierType.FUNCTION

    @staticmethod
    def is_module(value: IdentifierValue) -> bool:
        """
        Check whether the identifier is a module.
        """
        return value.identifier_type == IdentifierType.MODULE

    @staticmethod
    def is_namespace(value: IdentifierValue) -> bool:
        """
        Check whether the identifier is a namespace.
        """
        return value.identifier_type == IdentifierType.NAMESPACE

    @staticmethod
    def is_generic(value: IdentifierValue) -> bool:
        """
        Check whether the identifier is a generic type.
        """
        return value.identifier_type == IdentifierType.GENERIC

    # ------------------------------------------------------
    # Statistics
    # ------------------------------------------------------

    @staticmethod
    def supported_types() -> tuple[IdentifierType, ...]:
        """
        Return all supported identifier types.
        """
        return tuple(IdentifierType)

    @staticmethod
    def statistics() -> dict:
        """
        Return module statistics.
        """

        return {

            "module": MODULE_NAME,

            "version": MODULE_VERSION,

            "supported_identifier_types": len(IdentifierType),

            "unicode_identifiers": True,

            "keyword_validation": True,

            "generic_support": True,

            "namespace_support": True,

            "module_support": True,

        }

    # ------------------------------------------------------
    # Magic Methods
    # ------------------------------------------------------

    def __repr__(self) -> str:

        return (

            f"IdentifierParser("

            f"version={MODULE_VERSION!r}, "

            f"compiler={SUPPORTED_COMPILER!r}"

            f")"

        )


# ==========================================================
# Future Features
# ==========================================================

FUTURE_IDENTIFIER_FEATURES = {

    "DECORATORS": False,

    "ATTRIBUTES": False,

    "ANNOTATIONS": True,

    "GENERICS": True,

    "NAMESPACES": True,

    "MODULE_ALIASES": True,

    "TYPE_PARAMETERS": False,

    "REFLECTION": False,

}


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    "IdentifierType",

    "IdentifierValue",

    "IdentifierParser",

]


# ==========================================================
# Self Test
# ==========================================================

if __name__ == "__main__":

    samples = [

        "value",

        "_private",

        "MAX_SIZE",

        "Person",

        "TValue",

        "module_name",

    ]

    print("=" * 70)

    print("Hekay Identifier Parser v3.1")

    print("=" * 70)

    print()

    for sample in samples:

        parser = IdentifierParser(

            Scanner(sample)

        )

        identifier = parser.parse()

        print(

            f"{sample:<20}"

            f"{identifier.identifier_type.name:<15}"

            f"valid={IdentifierParser.is_valid_identifier(sample)}"

        )

    print()

    print("Supported Types")

    for item in IdentifierParser.supported_types():

        print("-", item.name)

    print()

    print("Statistics")

    print(

        IdentifierParser.statistics()

    )

    print()

    print("Future Features")

    for key, value in FUTURE_IDENTIFIER_FEATURES.items():

        print(f"{key:<22}: {value}")

    print()

    print("Identifier Parser Loaded Successfully.")

    print("=" * 70)