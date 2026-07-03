"""
Hekay Programming Language

Official Keyword Registry

Version:
3.1.0

Developer:
Dhiraj Kumar Mehangiya

License:
MIT License

Description:
Official keyword registry for the Hekay Programming Language.

This module is shared by:

• Lexer
• Parser
• Semantic Analyzer
• IDE
• Syntax Highlighter
• Formatter
• Language Server
"""

from __future__ import annotations

from enum import Enum, auto
from dataclasses import dataclass
from typing import Dict, List, Set


# ==========================================================
# Keyword Categories
# ==========================================================

class KeywordCategory(Enum):
    """
    Categories of Hekay keywords.
    """

    VARIABLE = auto()

    IO = auto()

    CONDITION = auto()

    LOOP = auto()

    FUNCTION = auto()

    CLASS = auto()

    MODULE = auto()

    ERROR = auto()

    BOOLEAN = auto()

    RESERVED = auto()


# ==========================================================
# Keyword Definition
# ==========================================================

@dataclass(slots=True)
class Keyword:

    text: str

    category: KeywordCategory

    description: str = ""

    reserved: bool = False


# ==========================================================
# Registry
# ==========================================================

KEYWORDS: Dict[str, Keyword] = {}

RESERVED_KEYWORDS: Set[str] = {

    # OOP
    "interface",
    "abstract",
    "static",
    "private",
    "public",
    "protected",

    # Async
    "async",
    "await",

    # Type System
    "is",
    "as",
    "typeof",

    # Future AI
    "ai",
    "model",
    "train",

    # Robotics
    "robot",
    "sensor",
    "motor",

    # Game
    "entity",
    "scene",

    # Cloud
    "cloud",

}


def register(
    text: str,
    category: KeywordCategory,
    description: str = "",
) -> None:
    """
    Register an active keyword.
    """

    KEYWORDS[text] = Keyword(
        text=text,
        category=category,
        description=description,
    )

# ==========================================================
# Variable Keywords
# ==========================================================

register(
    "het",
    KeywordCategory.VARIABLE,
    "Declare a mutable variable.",
)

register(
    "hook",
    KeywordCategory.VARIABLE,
    "Declare an immutable constant.",
)

# ==========================================================
# Input / Output
# ==========================================================

register(
    "show",
    KeywordCategory.IO,
    "Display output.",
)

register(
    "input",
    KeywordCategory.IO,
    "Read user input.",
)

# ==========================================================
# Conditional Statements
# ==========================================================

register(
    "if",
    KeywordCategory.CONDITION,
    "If statement.",
)

register(
    "elif",
    KeywordCategory.CONDITION,
    "Else if statement.",
)

register(
    "else",
    KeywordCategory.CONDITION,
    "Else statement.",
)

register(
    "match",
    KeywordCategory.CONDITION,
    "Pattern matching.",
)

register(
    "case",
    KeywordCategory.CONDITION,
    "Pattern case.",
)

register(
    "default",
    KeywordCategory.CONDITION,
    "Default match case.",
)

# ==========================================================
# Loop Keywords
# ==========================================================

register(
    "loop",
    KeywordCategory.LOOP,
    "Infinite loop.",
)

register(
    "while",
    KeywordCategory.LOOP,
    "While loop.",
)

register(
    "for",
    KeywordCategory.LOOP,
    "For loop.",
)

register(
    "break",
    KeywordCategory.LOOP,
    "Break current loop.",
)

register(
    "continue",
    KeywordCategory.LOOP,
    "Continue loop execution.",
)

# ==========================================================
# Function Keywords
# ==========================================================

register(
    "func",
    KeywordCategory.FUNCTION,
    "Function declaration.",
)

register(
    "return",
    KeywordCategory.FUNCTION,
    "Return from function.",
)

# ==========================================================
# Class Keywords
# ==========================================================

register(
    "class",
    KeywordCategory.CLASS,
    "Class declaration.",
)

register(
    "new",
    KeywordCategory.CLASS,
    "Create object instance.",
)

register(
    "this",
    KeywordCategory.CLASS,
    "Current object reference.",
)

register(
    "super",
    KeywordCategory.CLASS,
    "Parent class reference.",
)

register(
    "extends",
    KeywordCategory.CLASS,
    "Inheritance keyword.",
)

# ==========================================================
# Module Keywords
# ==========================================================

register(
    "inport",
    KeywordCategory.MODULE,
    "Import module.",
)

register(
    "outport",
    KeywordCategory.MODULE,
    "Export module.",
)

# ==========================================================
# Error Handling
# ==========================================================

register(
    "try",
    KeywordCategory.ERROR,
    "Begin exception block.",
)

register(
    "catch",
    KeywordCategory.ERROR,
    "Catch exception.",
)

register(
    "throw",
    KeywordCategory.ERROR,
    "Throw exception.",
)

register(
    "finally",
    KeywordCategory.ERROR,
    "Finally block.",
)

# ==========================================================
# Boolean Keywords
# ==========================================================

register(
    "true",
    KeywordCategory.BOOLEAN,
    "Boolean true.",
)

register(
    "false",
    KeywordCategory.BOOLEAN,
    "Boolean false.",
)

register(
    "null",
    KeywordCategory.BOOLEAN,
    "Null value.",
)

# ==========================================================
# Lookup API
# ==========================================================

def is_keyword(text: str) -> bool:
    """
    Returns True if the text is an active keyword.
    """
    return text in KEYWORDS


def is_reserved_keyword(text: str) -> bool:
    """
    Returns True if the text is reserved.
    """
    return text in RESERVED_KEYWORDS


def get_keyword(text: str) -> Keyword | None:
    """
    Returns keyword information.
    """
    return KEYWORDS.get(text)


def all_keywords() -> List[Keyword]:
    """
    Returns all registered keywords.
    """
    return list(KEYWORDS.values())


def keywords_by_category(
    category: KeywordCategory,
) -> List[Keyword]:
    """
    Returns keywords belonging to a category.
    """

    return [
        keyword
        for keyword in KEYWORDS.values()
        if keyword.category == category
    ]


# ==========================================================
# Validation
# ==========================================================

def validate_keyword_registry() -> bool:
    """
    Validate keyword registry.
    """

    if not KEYWORDS:
        return False

    for name, keyword in KEYWORDS.items():

        if not isinstance(name, str):
            return False

        if not isinstance(keyword, Keyword):
            return False

    return True


# ==========================================================
# Statistics
# ==========================================================

TOTAL_KEYWORDS = len(KEYWORDS)

TOTAL_RESERVED = len(RESERVED_KEYWORDS)


def keyword_statistics() -> Dict[str, int]:
    """
    Returns keyword statistics.
    """

    statistics = {
        "total_keywords": TOTAL_KEYWORDS,
        "reserved_keywords": TOTAL_RESERVED,
    }

    for category in KeywordCategory:

        statistics[
            category.name.lower()
        ] = len(
            keywords_by_category(category)
        )

    return statistics


# ==========================================================
# Future Keyword Groups
# ==========================================================

FUTURE_KEYWORD_GROUPS = {

    "AI": [

        "ai",
        "model",
        "train",

    ],

    "ROBOTICS": [

        "robot",
        "sensor",
        "motor",

    ],

    "GAME": [

        "entity",
        "scene",

    ],

    "CLOUD": [

        "cloud",

    ],

    "ASYNC": [

        "async",
        "await",

    ],

}


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    "Keyword",

    "KeywordCategory",

    "KEYWORDS",

    "RESERVED_KEYWORDS",

    "register",

    "is_keyword",

    "is_reserved_keyword",

    "get_keyword",

    "all_keywords",

    "keywords_by_category",

    "validate_keyword_registry",

    "keyword_statistics",

    "FUTURE_KEYWORD_GROUPS",

]


# ==========================================================
# Self Test
# ==========================================================

if __name__ == "__main__":

    print("=" * 70)

    print("Hekay Keyword Registry")

    print("=" * 70)

    print()

    print("Registry Valid:")

    print(validate_keyword_registry())

    print()

    print("Statistics")

    print(keyword_statistics())

    print()

    print("Registered Keywords")

    for keyword in all_keywords():

        print(
            f"{keyword.text:<12}"
            f"{keyword.category.name}"
        )

    print()

    print("Reserved Keywords")

    for keyword in sorted(RESERVED_KEYWORDS):

        print(keyword)

    print()

    print("Keyword Registry Loaded Successfully.")

    print("=" * 70)