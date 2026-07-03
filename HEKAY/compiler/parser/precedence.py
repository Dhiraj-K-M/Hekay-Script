"""
Hekay Programming Language

Module:
Operator Precedence

Version:
3.1.0

Developer:
Dhiraj Kumar Mehangiya

License:
MIT License

Description:
Defines operator precedence and associativity used by the
Hekay Pratt Parser.

This module is shared by:

• Parser
• Expression Parser
• Semantic Analyzer
• Optimizer
• Bytecode Generator
• HKVM
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, Optional

from compiler.lexer.operators import (
    Operator,
    Associativity,
    get_operator,
)

# ==========================================================
# Module Information
# ==========================================================

MODULE_NAME = "Operator Precedence"

MODULE_VERSION = "3.1.0"

SUPPORTED_COMPILER = "Hekay Compiler v3"

# ==========================================================
# Precedence Levels
# ==========================================================


class Precedence(Enum):
    """
    Hekay operator precedence.
    """

    LOWEST = 0

    ASSIGNMENT = auto()

    LAMBDA = auto()

    PIPELINE = auto()

    LOGICAL_OR = auto()

    LOGICAL_AND = auto()

    NULL_COALESCING = auto()

    COMPARISON = auto()

    RANGE = auto()

    BITWISE = auto()

    ADDITIVE = auto()

    MULTIPLICATIVE = auto()

    EXPONENT = auto()

    PREFIX = auto()

    POSTFIX = auto()

    MEMBER = auto()

    PRIMARY = auto()


# ==========================================================
# Operator Rule
# ==========================================================

@dataclass(slots=True)
class OperatorRule:
    """
    Parser precedence rule.
    """

    symbol: str

    precedence: Precedence

    associativity: Associativity

    unary: bool

    binary: bool

    description: str = ""

# ==========================================================
# Precedence Table
# ==========================================================

PRECEDENCE_TABLE: Dict[str, OperatorRule] = {}


def register(rule: OperatorRule) -> None:
    """
    Register an operator precedence rule.
    """

    PRECEDENCE_TABLE[rule.symbol] = rule


# ==========================================================
# Load Rules From Operator Registry
# ==========================================================

def _load_rules() -> None:
    """
    Automatically build precedence rules from the
    lexer operator registry.
    """

    from compiler.lexer.operators import all_operators

    mapping = {
        0: Precedence.LOWEST,
        1: Precedence.ASSIGNMENT,
        2: Precedence.LAMBDA,
        3: Precedence.PIPELINE,
        4: Precedence.LOGICAL_OR,
        5: Precedence.LOGICAL_AND,
        6: Precedence.NULL_COALESCING,
        7: Precedence.COMPARISON,
        8: Precedence.BITWISE,
        9: Precedence.COMPARISON,
        10: Precedence.RANGE,
        11: Precedence.ADDITIVE,
        12: Precedence.ADDITIVE,
        13: Precedence.MULTIPLICATIVE,
        14: Precedence.EXPONENT,
        15: Precedence.PREFIX,
        16: Precedence.POSTFIX,
        17: Precedence.MEMBER,
        18: Precedence.MEMBER,
    }

    for operator in all_operators():

        register(

            OperatorRule(

                symbol=operator.symbol,

                precedence=mapping.get(

                    operator.precedence,

                    Precedence.LOWEST,

                ),

                associativity=operator.associativity,

                unary=operator.unary,

                binary=operator.binary,

                description=operator.description,

            )

        )


_load_rules()


# ==========================================================
# Lookup Helpers
# ==========================================================

def get_rule(
    symbol: str,
) -> Optional[OperatorRule]:
    """
    Return precedence rule for an operator.
    """

    return PRECEDENCE_TABLE.get(symbol)


def has_rule(
    symbol: str,
) -> bool:
    """
    Check whether an operator has a rule.
    """

    return symbol in PRECEDENCE_TABLE


def precedence_of(
    symbol: str,
) -> Precedence:
    """
    Return precedence level.
    """

    rule = get_rule(symbol)

    if rule is None:

        return Precedence.LOWEST

    return rule.precedence


def associativity_of(
    symbol: str,
) -> Associativity:
    """
    Return associativity.
    """

    rule = get_rule(symbol)

    if rule is None:

        return Associativity.NONE

    return rule.associativity

# ==========================================================
# Parser Helpers
# ==========================================================

def is_prefix(
    symbol: str,
) -> bool:
    """
    Returns True if operator can be used as prefix.
    """

    rule = get_rule(symbol)

    return rule is not None and rule.unary


def is_binary(
    symbol: str,
) -> bool:
    """
    Returns True if operator is binary.
    """

    rule = get_rule(symbol)

    return rule is not None and rule.binary


def is_postfix(
    symbol: str,
) -> bool:
    """
    Returns True if operator is postfix.
    """

    return symbol in {

        "++",

        "--",

    }


def is_assignment(
    symbol: str,
) -> bool:
    """
    Returns True if assignment operator.
    """

    return symbol in {

        "=",

        "+=",

        "-=",

        "*=",

        "/=",

        "%=",

        "**=",

        "//=",

    }


# ==========================================================
# Validation
# ==========================================================

def validate_precedence_table() -> bool:
    """
    Validate precedence table.
    """

    for symbol, rule in PRECEDENCE_TABLE.items():

        if not isinstance(symbol, str):

            return False

        if not isinstance(rule, OperatorRule):

            return False

    return True


# ==========================================================
# Statistics
# ==========================================================

TOTAL_RULES = len(PRECEDENCE_TABLE)


def precedence_statistics() -> Dict[str, int]:
    """
    Returns precedence statistics.
    """

    prefix = 0

    binary = 0

    postfix = 0

    assignment = 0

    for symbol, rule in PRECEDENCE_TABLE.items():

        if rule.unary:

            prefix += 1

        if rule.binary:

            binary += 1

        if is_postfix(symbol):

            postfix += 1

        if is_assignment(symbol):

            assignment += 1

    return {

        "total_rules": TOTAL_RULES,

        "prefix": prefix,

        "binary": binary,

        "postfix": postfix,

        "assignment": assignment,

    }


# ==========================================================
# Future Parser Hooks
# ==========================================================

FUTURE_PRECEDENCE_FEATURES = {

    "TERNARY_OPERATOR": True,

    "PATTERN_MATCHING": True,

    "PIPELINE_OPERATOR": True,

    "NULL_PROPAGATION": True,

    "GENERIC_TYPES": True,

    "ASYNC_AWAIT": True,

    "COROUTINES": True,

    "CUSTOM_OPERATORS": False,

    "MACROS": False,

}


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    "Precedence",

    "OperatorRule",

    "PRECEDENCE_TABLE",

    "register",

    "get_rule",

    "has_rule",

    "precedence_of",

    "associativity_of",

    "is_prefix",

    "is_binary",

    "is_postfix",

    "is_assignment",

    "validate_precedence_table",

    "precedence_statistics",

]


# ==========================================================
# Self Test
# ==========================================================

if __name__ == "__main__":

    print("=" * 70)

    print("Hekay Operator Precedence")

    print("=" * 70)

    print()

    print("Validation")

    print(validate_precedence_table())

    print()

    print("Statistics")

    print(precedence_statistics())

    print()

    print("Registered Rules")

    for symbol in sorted(PRECEDENCE_TABLE):

        rule = PRECEDENCE_TABLE[symbol]

        print(

            f"{symbol:<6}"

            f"{rule.precedence.name:<20}"

            f"{rule.associativity.name}"

        )

    print()

    print("Future Features")

    for feature, enabled in FUTURE_PRECEDENCE_FEATURES.items():

        print(

            f"{feature:<25}: {enabled}"

        )

    print()

    print("Operator Precedence Loaded Successfully.")

    print("=" * 70)