"""
Hekay Programming Language

Token System

Version:
3.1.0

Developer:
Dhiraj Kumar Mehangiya

License:
MIT License

Description:
Official token definitions for the Hekay compiler.

Shared by:

• Scanner
• Lexer
• Parser
• Semantic Analyzer
• Optimizer
• Bytecode Generator
• HKVM
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional


# ==========================================================
# Module Information
# ==========================================================

MODULE_NAME = "Token System"

MODULE_VERSION = "3.1.0"

SUPPORTED_COMPILER = "Hekay Compiler v3"


# ==========================================================
# Token Types
# ==========================================================

class TokenType(Enum):
    """
    Token categories.
    """

    KEYWORD = auto()

    IDENTIFIER = auto()

    NUMBER = auto()

    STRING = auto()

    CHARACTER = auto()

    COMMENT = auto()

    OPERATOR = auto()

    SYMBOL = auto()

    NEWLINE = auto()

    INDENT = auto()

    DEDENT = auto()

    EOF = auto()

    ERROR = auto()


# ==========================================================
# Token Position
# ==========================================================

@dataclass(slots=True)
class TokenPosition:
    """
    Source position of a token.
    """

    line: int = 1

    column: int = 1

    index: int = 0

    filename: str = "<memory>"


# ==========================================================
# Token
# ==========================================================

@dataclass(slots=True)
class Token:
    """
    Represents a lexer token.
    """

    token_type: TokenType

    value: str

    position: TokenPosition

    literal: Optional[object] = None

# ==========================================================
# Token Helper Methods
# ==========================================================

    def is_keyword(self) -> bool:
        """
        Returns True if this token is a keyword.
        """
        return self.token_type == TokenType.KEYWORD

    def is_identifier(self) -> bool:
        """
        Returns True if this token is an identifier.
        """
        return self.token_type == TokenType.IDENTIFIER

    def is_number(self) -> bool:
        """
        Returns True if this token is a number.
        """
        return self.token_type == TokenType.NUMBER

    def is_string(self) -> bool:
        """
        Returns True if this token is a string.
        """
        return self.token_type == TokenType.STRING

    def is_character(self) -> bool:
        """
        Returns True if this token is a character.
        """
        return self.token_type == TokenType.CHARACTER

    def is_comment(self) -> bool:
        """
        Returns True if this token is a comment.
        """
        return self.token_type == TokenType.COMMENT

    def is_operator(self) -> bool:
        """
        Returns True if this token is an operator.
        """
        return self.token_type == TokenType.OPERATOR

    def is_symbol(self) -> bool:
        """
        Returns True if this token is a symbol.
        """
        return self.token_type == TokenType.SYMBOL

    def is_newline(self) -> bool:
        """
        Returns True if this token is a newline.
        """
        return self.token_type == TokenType.NEWLINE

    def is_eof(self) -> bool:
        """
        Returns True if this token is EOF.
        """
        return self.token_type == TokenType.EOF

    def is_error(self) -> bool:
        """
        Returns True if this token is an error.
        """
        return self.token_type == TokenType.ERROR

    def is_literal(self) -> bool:
        """
        Returns True if this token is a literal.
        """

        return self.token_type in {

            TokenType.NUMBER,

            TokenType.STRING,

            TokenType.CHARACTER,

        }

    def copy(self) -> "Token":
        """
        Creates a copy of this token.
        """

        return Token(

            token_type=self.token_type,

            value=self.value,

            position=TokenPosition(

                line=self.position.line,

                column=self.position.column,

                index=self.position.index,

                filename=self.position.filename,

            ),

            literal=self.literal,

        )

    def __str__(self) -> str:

        return self.value

    def __repr__(self) -> str:

        return (

            f"Token("

            f"type={self.token_type.name}, "

            f"value={self.value!r}, "

            f"line={self.position.line}, "

            f"column={self.position.column}"

            f")"

        )
    # ==========================================================
# Validation
# ==========================================================

def validate_token(token: Token) -> bool:
    """
    Validate a token instance.
    """

    if not isinstance(token, Token):
        return False

    if not isinstance(token.token_type, TokenType):
        return False

    if not isinstance(token.value, str):
        return False

    if not isinstance(token.position, TokenPosition):
        return False

    return True


# ==========================================================
# Factory Functions
# ==========================================================

def create_token(
    token_type: TokenType,
    value: str,
    line: int = 1,
    column: int = 1,
    index: int = 0,
    filename: str = "<memory>",
    literal: object | None = None,
) -> Token:
    """
    Create a new token.
    """

    return Token(
        token_type=token_type,
        value=value,
        position=TokenPosition(
            line=line,
            column=column,
            index=index,
            filename=filename,
        ),
        literal=literal,
    )


# ==========================================================
# Statistics
# ==========================================================

TOKEN_TYPE_COUNT = len(TokenType)


def token_statistics() -> dict[str, int]:
    """
    Return token system statistics.
    """

    return {
        "token_types": TOKEN_TYPE_COUNT,
    }


# ==========================================================
# Future Token Features
# ==========================================================

FUTURE_TOKEN_FEATURES = {

    "DOC_COMMENT": True,

    "ATTRIBUTE": True,

    "ANNOTATION": True,

    "INTERPOLATED_STRING": True,

    "RAW_STRING": True,

    "MULTILINE_STRING": True,

    "HEX_FLOAT": True,

    "BIG_INTEGER": True,

    "BIG_DECIMAL": True,

    "CUSTOM_LITERAL": False,

}


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    "TokenType",

    "TokenPosition",

    "Token",

    "create_token",

    "validate_token",

    "token_statistics",

    "FUTURE_TOKEN_FEATURES",

]


# ==========================================================
# Self Test
# ==========================================================

if __name__ == "__main__":

    print("=" * 70)

    print("Hekay Token System")

    print("=" * 70)

    print()

    token = create_token(

        TokenType.IDENTIFIER,

        "example",

    )

    print("Created Token")

    print(token)

    print()

    print("Validation")

    print(validate_token(token))

    print()

    print("Statistics")

    print(token_statistics())

    print()

    print("Future Features")

    for feature, enabled in FUTURE_TOKEN_FEATURES.items():

        print(f"{feature:<25}: {enabled}")

    print()

    print("Token System Loaded Successfully.")

    print("=" * 70)

    