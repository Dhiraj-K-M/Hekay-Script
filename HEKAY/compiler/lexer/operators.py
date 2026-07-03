"""
Hekay Programming Language

Module: Operator Registry

Version: 3.1.0

Developer:
Dhiraj Kumar Mehangiya

Copyright:
(c) Hekay Foundation

License:
MIT

Description:
Official operator registry used by the Hekay Compiler,
Interpreter, HKVM, Optimizer, IDE and future SDKs.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict
from typing import List
from typing import Optional
from typing import Set

from compiler.common.registry import Registry

# ==========================================================
# Module Information
# ==========================================================

MODULE_NAME = "Operator Registry"

MODULE_VERSION = "3.1.0"

SUPPORTED_COMPILER = "Hekay Compiler v3"

# ==========================================================
# Operator Categories
# ==========================================================


class OperatorCategory(Enum):
    """Official Hekay operator categories."""

    ARITHMETIC = auto()

    ASSIGNMENT = auto()

    COMPARISON = auto()

    LOGICAL = auto()

    BITWISE = auto()

    UNARY = auto()

    INCREMENT = auto()

    MEMBER = auto()

    RANGE = auto()

    PIPELINE = auto()

    LAMBDA = auto()

    NULL_SAFE = auto()

    FUTURE = auto()


# ==========================================================
# Associativity
# ==========================================================


class Associativity(Enum):

    LEFT = auto()

    RIGHT = auto()

    NONE = auto()


# ==========================================================
# Operator Definition
# ==========================================================


@dataclass(slots=True)
class Operator:

    symbol: str

    name: str

    category: OperatorCategory

    precedence: int

    associativity: Associativity

    unary: bool = False

    binary: bool = True

    future: bool = False

    description: str = ""

    supported_in: Set[str] | None = None

    experimental: bool = False

    deprecated: bool = False

    def __post_init__(self):

        if self.supported_in is None:

            self.supported_in = {

                "compiler",

                "lexer",

                "parser",

                "interpreter",

                "optimizer",

                "hkvm",

                "ide",

            }


# ==========================================================
# Registry
# ==========================================================

OPERATORS = Registry[Operator]("Operator Registry")


# ==========================================================
# Registration API
# ==========================================================

def register(operator: Operator) -> None:
    """
    Register a new operator.
    """

    OPERATORS.register(

        operator.symbol,

        operator,

    )


def get_operator(symbol: str) -> Optional[Operator]:

    return OPERATORS.get(symbol)


def has_operator(symbol: str) -> bool:

    return OPERATORS.exists(symbol)


def all_operators() -> List[Operator]:

    return OPERATORS.values()

# ==========================================================
# Arithmetic Operators
# ==========================================================

register(
    Operator(
        symbol="+",
        name="Addition",
        category=OperatorCategory.ARITHMETIC,
        precedence=12,
        associativity=Associativity.LEFT,
        description="Adds two values.",
    )
)

register(
    Operator(
        symbol="-",
        name="Subtraction",
        category=OperatorCategory.ARITHMETIC,
        precedence=12,
        associativity=Associativity.LEFT,
        unary=True,
        description="Subtracts two values.",
    )
)

register(
    Operator(
        symbol="*",
        name="Multiplication",
        category=OperatorCategory.ARITHMETIC,
        precedence=13,
        associativity=Associativity.LEFT,
        description="Multiplies two values.",
    )
)

register(
    Operator(
        symbol="/",
        name="Division",
        category=OperatorCategory.ARITHMETIC,
        precedence=13,
        associativity=Associativity.LEFT,
        description="Divides two values.",
    )
)

register(
    Operator(
        symbol="%",
        name="Modulo",
        category=OperatorCategory.ARITHMETIC,
        precedence=13,
        associativity=Associativity.LEFT,
        description="Modulo operation.",
    )
)

register(
    Operator(
        symbol="**",
        name="Power",
        category=OperatorCategory.ARITHMETIC,
        precedence=14,
        associativity=Associativity.RIGHT,
        description="Exponentiation.",
    )
)

register(
    Operator(
        symbol="//",
        name="Floor Division",
        category=OperatorCategory.ARITHMETIC,
        precedence=13,
        associativity=Associativity.LEFT,
        description="Integer division.",
    )
)

# ==========================================================
# Assignment Operators
# ==========================================================

for symbol, name in [

    ("=", "Assign"),

    ("+=", "Add Assign"),

    ("-=", "Subtract Assign"),

    ("*=", "Multiply Assign"),

    ("/=", "Divide Assign"),

    ("%=", "Modulo Assign"),

    ("**=", "Power Assign"),

    ("//=", "Floor Divide Assign"),

]:

    register(

        Operator(

            symbol=symbol,

            name=name,

            category=OperatorCategory.ASSIGNMENT,

            precedence=2,

            associativity=Associativity.RIGHT,

            description=name,

        )

    )

# ==========================================================
# Comparison Operators
# ==========================================================

for symbol, name in [

    ("==", "Equal"),

    ("!=", "Not Equal"),

    (">", "Greater Than"),

    ("<", "Less Than"),

    (">=", "Greater Than Or Equal"),

    ("<=", "Less Than Or Equal"),

]:

    register(

        Operator(

            symbol=symbol,

            name=name,

            category=OperatorCategory.COMPARISON,

            precedence=9,

            associativity=Associativity.LEFT,

            description=name,

        )

    )

# ==========================================================
# Logical Operators
# ==========================================================

register(
    Operator(
        symbol="and",
        name="Logical And",
        category=OperatorCategory.LOGICAL,
        precedence=4,
        associativity=Associativity.LEFT,
        description="Logical AND operation.",
    )
)

register(
    Operator(
        symbol="or",
        name="Logical Or",
        category=OperatorCategory.LOGICAL,
        precedence=3,
        associativity=Associativity.LEFT,
        description="Logical OR operation.",
    )
)

register(
    Operator(
        symbol="not",
        name="Logical Not",
        category=OperatorCategory.LOGICAL,
        precedence=15,
        associativity=Associativity.RIGHT,
        unary=True,
        binary=False,
        description="Logical NOT operation.",
    )
)

register(
    Operator(
        symbol="xor",
        name="Logical XOR",
        category=OperatorCategory.LOGICAL,
        precedence=4,
        associativity=Associativity.LEFT,
        description="Logical XOR operation.",
    )
)

# ==========================================================
# Bitwise Operators
# ==========================================================

for symbol, name in [

    ("&", "Bitwise And"),

    ("|", "Bitwise Or"),

    ("^", "Bitwise XOR"),

    ("<<", "Left Shift"),

    (">>", "Right Shift"),

]:

    register(

        Operator(

            symbol=symbol,

            name=name,

            category=OperatorCategory.BITWISE,

            precedence=8,

            associativity=Associativity.LEFT,

            description=name,

        )

    )

register(
    Operator(
        symbol="~",
        name="Bitwise Not",
        category=OperatorCategory.BITWISE,
        precedence=15,
        associativity=Associativity.RIGHT,
        unary=True,
        binary=False,
        description="Bitwise NOT.",
    )
)

# ==========================================================
# Increment / Decrement
# ==========================================================

register(
    Operator(
        symbol="++",
        name="Increment",
        category=OperatorCategory.INCREMENT,
        precedence=16,
        associativity=Associativity.RIGHT,
        unary=True,
        binary=False,
        description="Increment value.",
    )
)

register(
    Operator(
        symbol="--",
        name="Decrement",
        category=OperatorCategory.INCREMENT,
        precedence=16,
        associativity=Associativity.RIGHT,
        unary=True,
        binary=False,
        description="Decrement value.",
    )
)

# ==========================================================
# Member Operators
# ==========================================================

register(
    Operator(
        symbol=".",
        name="Member Access",
        category=OperatorCategory.MEMBER,
        precedence=18,
        associativity=Associativity.LEFT,
        description="Object member access.",
    )
)

register(
    Operator(
        symbol="?.",
        name="Safe Member Access",
        category=OperatorCategory.NULL_SAFE,
        precedence=18,
        associativity=Associativity.LEFT,
        description="Null-safe member access.",
    )
)

register(
    Operator(
        symbol="??",
        name="Null Coalescing",
        category=OperatorCategory.NULL_SAFE,
        precedence=4,
        associativity=Associativity.LEFT,
        description="Return first non-null value.",
    )
)

# ==========================================================
# Range
# ==========================================================

register(
    Operator(
        symbol="..",
        name="Range",
        category=OperatorCategory.RANGE,
        precedence=6,
        associativity=Associativity.LEFT,
        description="Create range.",
    )
)

# ==========================================================
# Pipeline
# ==========================================================

register(
    Operator(
        symbol="|>",
        name="Pipeline",
        category=OperatorCategory.PIPELINE,
        precedence=5,
        associativity=Associativity.LEFT,
        description="Pipeline operator.",
    )
)

# ==========================================================
# Lambda
# ==========================================================

register(
    Operator(
        symbol="=>",
        name="Lambda",
        category=OperatorCategory.LAMBDA,
        precedence=2,
        associativity=Associativity.RIGHT,
        description="Lambda expression.",
    )
)

# ==========================================================
# Future Reserved Operators
# ==========================================================

for symbol, name in [

    ("<-", "Receive"),

    ("->", "Send"),

    ("::", "Namespace"),

    ("...", "Spread"),

    ("???", "Reserved"),

]:

    register(

        Operator(

            symbol=symbol,

            name=name,

            category=OperatorCategory.FUTURE,

            precedence=1,

            associativity=Associativity.NONE,

            future=True,

            description="Reserved for future versions.",

        )

    )

    # ==========================================================
# Validation Helpers
# ==========================================================

def validate_operator(symbol: str) -> bool:
    """
    Check whether the given symbol is a valid operator.
    """
    return OPERATORS.exists(symbol)


def validate_category(category: OperatorCategory) -> bool:
    """
    Validate an operator category.
    """
    return isinstance(category, OperatorCategory)


def reserved_operators() -> List[Operator]:
    """
    Return all reserved operators.
    """
    return [
        operator
        for operator in OPERATORS.values()
        if operator.future
    ]


# ==========================================================
# Statistics
# ==========================================================

TOTAL_OPERATORS: int = OPERATORS.count

CATEGORY_COUNT: Dict[OperatorCategory, int] = {}

for operator in OPERATORS.values():

    CATEGORY_COUNT.setdefault(operator.category, 0)

    CATEGORY_COUNT[operator.category] += 1


def operator_statistics() -> Dict[str, int]:
    """
    Return registry statistics.
    """

    return {

        "total": TOTAL_OPERATORS,

        "arithmetic": CATEGORY_COUNT.get(
            OperatorCategory.ARITHMETIC, 0
        ),

        "assignment": CATEGORY_COUNT.get(
            OperatorCategory.ASSIGNMENT, 0
        ),

        "comparison": CATEGORY_COUNT.get(
            OperatorCategory.COMPARISON, 0
        ),

        "logical": CATEGORY_COUNT.get(
            OperatorCategory.LOGICAL, 0
        ),

        "bitwise": CATEGORY_COUNT.get(
            OperatorCategory.BITWISE, 0
        ),

        "increment": CATEGORY_COUNT.get(
            OperatorCategory.INCREMENT, 0
        ),

        "member": CATEGORY_COUNT.get(
            OperatorCategory.MEMBER, 0
        ),

        "range": CATEGORY_COUNT.get(
            OperatorCategory.RANGE, 0
        ),

        "pipeline": CATEGORY_COUNT.get(
            OperatorCategory.PIPELINE, 0
        ),

        "lambda": CATEGORY_COUNT.get(
            OperatorCategory.LAMBDA, 0
        ),

        "null_safe": CATEGORY_COUNT.get(
            OperatorCategory.NULL_SAFE, 0
        ),

        "future": CATEGORY_COUNT.get(
            OperatorCategory.FUTURE, 0
        ),

    }


# ==========================================================
# Future SDK Reserved Operators
# ==========================================================

FUTURE_OPERATOR_GROUPS = {

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
# Export Public API
# ==========================================================

__all__ = [

    "Operator",

    "OperatorCategory",

    "Associativity",

    "OPERATORS",

    "register",

    "get_operator",

    "has_operator",

    "all_operators",

    "operators_by_category",

    "reserved_operators",

    "validate_operator",

    "validate_category",

    "operator_statistics",

]


# ==========================================================
# Self Test
# ==========================================================

if __name__ == "__main__":

    print("=" * 70)

    print("Hekay Operator Registry v3.1")

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

    print("Total Operators")

    print(TOTAL_OPERATORS)

    print()

    print("Registered Operators")

    print("-" * 70)

    for operator in all_operators():

        print(

            f"{operator.symbol:<6}"

            f"{operator.name:<28}"

            f"{operator.category.name}"

        )

    print()

    print("Statistics")

    print(operator_statistics())

    print()

    print("Reserved Operators")

    for operator in reserved_operators():

        print(

            operator.symbol,

            "-",

            operator.name,

        )

    print()

    print("Registry Information")

    print(OPERATORS.statistics())

    print()

    print("Registry Loaded Successfully.")

    print("=" * 70)