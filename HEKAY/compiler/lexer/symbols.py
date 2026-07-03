"""
Hekay Programming Language

Module:
Symbol Registry

Version:
3.1.0

Developer:
Dhiraj Kumar Mehangiya

Description:
Official symbol registry for Hekay Compiler.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional

from compiler.common.registry import Registry

# ==========================================================
# Module Information
# ==========================================================

MODULE_NAME = "Symbol Registry"

MODULE_VERSION = "3.1.0"

SUPPORTED_COMPILER = "Hekay Compiler v3"

# ==========================================================
# Symbol Categories
# ==========================================================

class SymbolCategory(Enum):

    BRACKET = auto()

    DELIMITER = auto()

    TERMINATOR = auto()

    ACCESS = auto()

    FUTURE = auto()


# ==========================================================
# Symbol Definition
# ==========================================================

@dataclass(slots=True)
class Symbol:

    symbol: str

    name: str

    category: SymbolCategory

    description: str = ""

    future: bool = False


# ==========================================================
# Registry
# ==========================================================

SYMBOLS = Registry[Symbol]("Symbol Registry")


# ==========================================================
# Registration API
# ==========================================================

def register(symbol: Symbol):

    SYMBOLS.register(

        symbol.symbol,

        symbol,

    )


def get_symbol(symbol: str) -> Optional[Symbol]:

    return SYMBOLS.get(symbol)


def has_symbol(symbol: str) -> bool:

    return SYMBOLS.exists(symbol)


def all_symbols() -> List[Symbol]:

    return SYMBOLS.values()

# ==========================================================
# Brackets
# ==========================================================

for symbol, name in [

    ("(", "Left Parenthesis"),
    (")", "Right Parenthesis"),

    ("{", "Left Brace"),
    ("}", "Right Brace"),

    ("[", "Left Bracket"),
    ("]", "Right Bracket"),

]:

    register(

        Symbol(

            symbol=symbol,

            name=name,

            category=SymbolCategory.BRACKET,

            description=name,

        )

    )

# ==========================================================
# Delimiters
# ==========================================================

for symbol, name in [

    (",", "Comma"),

    (":", "Colon"),

    (";", "Semicolon"),

]:

    register(

        Symbol(

            symbol=symbol,

            name=name,

            category=SymbolCategory.DELIMITER,

            description=name,

        )

    )

# ==========================================================
# Terminators
# ==========================================================

register(

    Symbol(

        symbol="\n",

        name="New Line",

        category=SymbolCategory.TERMINATOR,

        description="Line Terminator",

    )

)

register(

    Symbol(

        symbol="\t",

        name="Tab",

        category=SymbolCategory.TERMINATOR,

        description="Tab Character",

    )

)

# ==========================================================
# Access Symbols
# ==========================================================

for symbol, name in [

    ("@", "Decorator"),

    ("#", "Comment"),

    ("$", "Dollar"),

    ("`", "Back Tick"),

    ("\\", "Escape"),

]:

    register(

        Symbol(

            symbol=symbol,

            name=name,

            category=SymbolCategory.ACCESS,

            description=name,

        )

    )

# ==========================================================
# Future Reserved Symbols
# ==========================================================

for symbol, name in [

    ("§", "Section"),

    ("¤", "Currency"),

    ("©", "Copyright"),

    ("®", "Registered"),

    ("™", "Trademark"),

]:

    register(

        Symbol(

            symbol=symbol,

            name=name,

            category=SymbolCategory.FUTURE,

            future=True,

            description="Reserved For Future Versions",

        )

    )

# ==========================================================
# Lookup Helpers
# ==========================================================

def symbols_by_category(

    category: SymbolCategory,

) -> List[Symbol]:

    return [

        symbol

        for symbol in SYMBOLS.values()

        if symbol.category == category

    ]

# ==========================================================
# Validation Helpers
# ==========================================================

def validate_symbol(symbol: str) -> bool:
    """
    Check whether a symbol exists.
    """
    return SYMBOLS.exists(symbol)


def validate_category(category: SymbolCategory) -> bool:
    """
    Validate a symbol category.
    """
    return isinstance(category, SymbolCategory)


def reserved_symbols() -> List[Symbol]:
    """
    Return all reserved future symbols.
    """
    return [
        symbol
        for symbol in SYMBOLS.values()
        if symbol.future
    ]


# ==========================================================
# Statistics
# ==========================================================

TOTAL_SYMBOLS: int = SYMBOLS.count

CATEGORY_COUNT: Dict[SymbolCategory, int] = {}

for symbol in SYMBOLS.values():

    CATEGORY_COUNT.setdefault(symbol.category, 0)

    CATEGORY_COUNT[symbol.category] += 1


def symbol_statistics() -> Dict[str, int]:
    """
    Return registry statistics.
    """

    return {

        "total": TOTAL_SYMBOLS,

        "brackets": CATEGORY_COUNT.get(
            SymbolCategory.BRACKET, 0
        ),

        "delimiters": CATEGORY_COUNT.get(
            SymbolCategory.DELIMITER, 0
        ),

        "terminators": CATEGORY_COUNT.get(
            SymbolCategory.TERMINATOR, 0
        ),

        "access": CATEGORY_COUNT.get(
            SymbolCategory.ACCESS, 0
        ),

        "future": CATEGORY_COUNT.get(
            SymbolCategory.FUTURE, 0
        ),

    }


# ==========================================================
# Future Reserved Groups
# ==========================================================

FUTURE_SYMBOL_GROUPS = {

    "AI": [],

    "ROBOTICS": [],

    "GAME": [],

    "WEB": [],

    "ANDROID": [],

    "DATABASE": [],

    "NETWORK": [],

    "GRAPHICS": [],

    "VOICE": [],

    "CAMERA": [],

    "DRONE": [],

    "SPACE": [],

    "CLOUD": [],

}


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    "Symbol",

    "SymbolCategory",

    "SYMBOLS",

    "register",

    "get_symbol",

    "has_symbol",

    "all_symbols",

    "symbols_by_category",

    "reserved_symbols",

    "validate_symbol",

    "validate_category",

    "symbol_statistics",

]


# ==========================================================
# Self Test
# ==========================================================

if __name__ == "__main__":

    print("=" * 70)

    print("Hekay Symbol Registry v3.1")

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

    print("Total Symbols")

    print(TOTAL_SYMBOLS)

    print()

    print("Registered Symbols")

    print("-" * 70)

    for symbol in all_symbols():

        print(

            f"{symbol.symbol:<6}"

            f"{symbol.name:<28}"

            f"{symbol.category.name}"

        )

    print()

    print("Statistics")

    print(symbol_statistics())

    print()

    print("Reserved Symbols")

    for symbol in reserved_symbols():

        print(

            symbol.symbol,

            "-",

            symbol.name,

        )

    print()

    print("Registry Information")

    print(SYMBOLS.statistics())

    print()

    print("Symbol Registry Loaded Successfully.")

    print("=" * 70)