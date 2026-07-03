"""
Hekay Programming Language

Module:
Lexer Engine

Version:
3.1.0

Developer:
Dhiraj Kumar Mehangiya

Description:
Official Production Lexer Engine for the Hekay Compiler.

Responsibilities:

• Source Code Scanning
• Token Generation
• Keyword Detection
• Identifier Parsing
• Number Parsing
• String Parsing
• Comment Handling
• Operator Recognition
• Symbol Recognition
• EOF Token Generation
• Error Reporting
• Future Incremental Lexing
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from compiler.lexer.scanner import Scanner
from HEKAY.compiler.lexer.tokens import Token, TokenType
from compiler.lexer.keywords import KEYWORDS

from compiler.lexer.identifier import IdentifierParser
from compiler.lexer.numbers import NumberParser
from compiler.lexer.strings import StringParser
from compiler.lexer.comments import CommentParser

from compiler.lexer.operators import (
    has_operator,
)

from compiler.lexer.symbols import (
    has_symbol,
)


# ==========================================================
# Module Information
# ==========================================================

MODULE_NAME = "Lexer Engine"

MODULE_VERSION = "3.1.0"

SUPPORTED_COMPILER = "Hekay Compiler v3"


# ==========================================================
# Lexer Result
# ==========================================================

@dataclass(slots=True)
class LexerResult:

    tokens: List[Token] = field(default_factory=list)

    errors: List[str] = field(default_factory=list)


# ==========================================================
# Lexer Engine
# ==========================================================

class Lexer:
    """
    Production Lexer Engine.
    """

    def __init__(
        self,
        source: str,
    ):

        self.source = source

        self.scanner = Scanner(source)

        self.result = LexerResult()

    # ------------------------------------------------------

    def tokenize(self) -> LexerResult:
        """
        Convert source code into tokens.
        """

        while not self.scanner.eof():

            self.skip_whitespace()

            if self.scanner.eof():

                break

            self.scan_next()

        self.result.tokens.append(

            Token(
                TokenType.EOF,
                "EOF",
            )
        )

        return self.result

    # ------------------------------------------------------
    # Scan Next Token
    # ------------------------------------------------------

    def scan_next(self) -> None:
        """
        Scan the next token from the source.
        """

        ch = self.scanner.current()

        # --------------------------------------------------
        # Identifier / Keyword
        # --------------------------------------------------

        if ch.isalpha() or ch == "_":

            identifier = IdentifierParser(
                self.scanner
            ).parse()

            token_type = (
                TokenType.KEYWORD
                if identifier.text in KEYWORDS
                else TokenType.IDENTIFIER
            )

            self.result.tokens.append(
                Token(
                    token_type,
                    identifier.text,
                )
            )

            return

        # --------------------------------------------------
        # Number
        # --------------------------------------------------

        if ch.isdigit():

            number = NumberParser(
                self.scanner
            ).parse()

            self.result.tokens.append(
                Token(
                    TokenType.NUMBER,
                    number.value,
                )
            )

            return

        # --------------------------------------------------
        # String
        # --------------------------------------------------

        if ch in ("'", '"'):

            string = StringParser(
                self.scanner
            ).parse()

            self.result.tokens.append(
                Token(
                    TokenType.STRING,
                    string.value,
                )
            )

            return

        # --------------------------------------------------
        # Comments
        # --------------------------------------------------

        if (
            ch == "#"
            or (
                ch == "/"
                and self.scanner.peek() in (
                    "/",
                    "*",
                )
            )
        ):

            CommentParser(
                self.scanner
            ).parse()

            return

        # --------------------------------------------------
        # Operators
        # --------------------------------------------------

        for length in (3, 2, 1):

            text = self.scanner.peek_string(length)

            if has_operator(text):

                self.result.tokens.append(

                    Token(

                        TokenType.OPERATOR,

                        text,

                    )

                )

                for _ in range(length):

                    self.scanner.advance()

                return

        # --------------------------------------------------
        # Symbols
        # --------------------------------------------------

        if has_symbol(ch):

            self.result.tokens.append(

                Token(

                    TokenType.SYMBOL,

                    ch,

                )

            )

            self.scanner.advance()

            return

        # --------------------------------------------------
        # Unknown Character
        # --------------------------------------------------

        self.result.errors.append(

            f"Unknown character '{ch}' "

            f"at line {self.scanner.line}, "

            f"column {self.scanner.column}"

        )

        self.scanner.advance()


    # ------------------------------------------------------
    # Skip Whitespace
    # ------------------------------------------------------

    def skip_whitespace(self) -> None:
        """
        Skip whitespace characters.
        """

        while (
            not self.scanner.eof()
            and self.scanner.current().isspace()
        ):

            self.scanner.advance()

    # ------------------------------------------------------
    # Statistics
    # ------------------------------------------------------

    def token_count(self) -> int:
        """
        Return total generated tokens.
        """
        return len(self.result.tokens)

    def error_count(self) -> int:
        """
        Return total lexer errors.
        """
        return len(self.result.errors)

    def statistics(self) -> dict:
        """
        Return lexer statistics.
        """

        return {

            "module": MODULE_NAME,

            "version": MODULE_VERSION,

            "tokens": self.token_count(),

            "errors": self.error_count(),

            "source_length": len(self.source),

            "success": self.error_count() == 0,

        }

    # ------------------------------------------------------
    # Reset Lexer
    # ------------------------------------------------------

    def reset(self) -> None:
        """
        Reset lexer state.
        """

        self.scanner = Scanner(self.source)

        self.result = LexerResult()

    # ------------------------------------------------------
    # Future Hooks
    # ------------------------------------------------------

    def incremental_tokenize(self):
        """
        Future IDE incremental lexer.
        """
        raise NotImplementedError

    def tokenize_async(self):
        """
        Future async lexer.
        """
        raise NotImplementedError

    # ------------------------------------------------------
    # Magic Methods
    # ------------------------------------------------------

    def __repr__(self) -> str:

        return (

            f"Lexer("

            f"version={MODULE_VERSION!r}, "

            f"tokens={self.token_count()}, "

            f"errors={self.error_count()}"

            f")"

        )


# ==========================================================
# Future Features
# ==========================================================

FUTURE_LEXER_FEATURES = {

    "INCREMENTAL_LEXING": False,

    "ASYNC_LEXER": False,

    "PARALLEL_LEXER": False,

    "UNICODE_FULL_SUPPORT": True,

    "ERROR_RECOVERY": True,

    "IDE_SUPPORT": True,

    "SYNTAX_HIGHLIGHTING": True,

    "LIVE_ANALYSIS": True,

    "TOKEN_CACHE": False,

}


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    "Lexer",

    "LexerResult",

]


# ==========================================================
# Self Test
# ==========================================================

if __name__ == "__main__":

    source = """

het age = 18

hook pi = 3.14

show("Hello Hekay")

if age >= 18 {

    show("Adult")

}

"""

    lexer = Lexer(source)

    result = lexer.tokenize()

    print("=" * 70)

    print("Hekay Lexer Engine v3.1")

    print("=" * 70)

    print()

    print("Generated Tokens")

    for token in result.tokens:

        print(token)

    print()

    print("Errors")

    if result.errors:

        for error in result.errors:

            print(error)

    else:

        print("No Lexer Errors.")

    print()

    print("Statistics")

    print(

        lexer.statistics()

    )

    print()

    print("Future Features")

    for key, value in FUTURE_LEXER_FEATURES.items():

        print(f"{key:<25}: {value}")

    print()

    print("Lexer Loaded Successfully.")

    print("=" * 70)

