"""
Hekay Programming Language

Module:
AST Infrastructure

Version:
3.1.0

Developer:
Dhiraj Kumar Mehangiya

Description:
Base Abstract Syntax Tree (AST) infrastructure used by
the Hekay Parser.

Responsibilities:

• Base AST Node
• Source Location
• Tree Traversal
• Visitor Support
• Serialization
• Future Optimization Hooks
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


# ==========================================================
# Module Information
# ==========================================================

MODULE_NAME = "AST Infrastructure"

MODULE_VERSION = "3.1.0"

SUPPORTED_COMPILER = "Hekay Compiler v3"


# ==========================================================
# Source Position
# ==========================================================

@dataclass(slots=True)
class SourcePosition:
    """
    Represents a location in source code.
    """

    line: int
    column: int
    filename: str = "<memory>"


# ==========================================================
# Base AST Node
# ==========================================================

@dataclass(slots=True)
class ASTNode:
    """
    Base class for all AST nodes.
    """

    position: Optional[SourcePosition] = None

    children: List["ASTNode"] = field(default_factory=list)

    metadata: Dict[str, Any] = field(default_factory=dict)

    def add_child(
        self,
        node: "ASTNode",
    ) -> None:

        self.children.append(node)

    def child_count(self) -> int:

        return len(self.children)

    def is_leaf(self) -> bool:

        return len(self.children) == 0

    def accept(self, visitor):

        method = getattr(

            visitor,

            f"visit_{self.__class__.__name__}",

            visitor.generic_visit,

        )

        return method(self)

# ==========================================================
# Program Node
# ==========================================================

@dataclass(slots=True)
class ProgramNode(ASTNode):
    """
    Root node of every Hekay program.
    """

    body: List[ASTNode] = field(default_factory=list)

    def add_statement(
        self,
        node: ASTNode,
    ) -> None:

        self.body.append(node)

        self.add_child(node)

    def statement_count(self) -> int:

        return len(self.body)


# ==========================================================
# AST Visitor
# ==========================================================

class ASTVisitor:
    """
    Base visitor class.
    """

    def visit(
        self,
        node: ASTNode,
    ):

        return node.accept(self)

    def generic_visit(
        self,
        node: ASTNode,
    ):

        for child in node.children:

            self.visit(child)


# ==========================================================
# AST Walker
# ==========================================================

class ASTWalker:
    """
    Depth-first tree traversal.
    """

    @staticmethod
    def walk(
        node: ASTNode,
    ):

        yield node

        for child in node.children:

            yield from ASTWalker.walk(child)


# ==========================================================
# AST Statistics
# ==========================================================

class ASTStatistics:

    @staticmethod
    def total_nodes(
        root: ASTNode,
    ) -> int:

        return sum(

            1

            for _ in ASTWalker.walk(root)

        )

    @staticmethod
    def leaf_nodes(
        root: ASTNode,
    ) -> int:

        return sum(

            1

            for node in ASTWalker.walk(root)

            if node.is_leaf()

        )

    @staticmethod
    def max_depth(
        node: ASTNode,
    ) -> int:

        if node.is_leaf():

            return 1

        return 1 + max(

            ASTStatistics.max_depth(child)

            for child in node.children

        )


# ==========================================================
# Serialization
# ==========================================================

class ASTSerializer:

    @staticmethod
    def to_dict(
        node: ASTNode,
    ) -> dict:

        return {

            "type": node.__class__.__name__,

            "children": [

                ASTSerializer.to_dict(child)

                for child in node.children

            ],

            "metadata": node.metadata,

        }

# ==========================================================
# JSON Export
# ==========================================================

import json


class ASTExporter:
    """
    Export AST into different formats.
    """

    @staticmethod
    def to_json(
        node: ASTNode,
        indent: int = 4,
    ) -> str:

        return json.dumps(

            ASTSerializer.to_dict(node),

            indent=indent,

        )


# ==========================================================
# Pretty Printer
# ==========================================================

class ASTPrettyPrinter:

    @staticmethod
    def print(
        node: ASTNode,
        indent: int = 0,
    ) -> None:

        print(

            " " * indent

            + node.__class__.__name__

        )

        for child in node.children:

            ASTPrettyPrinter.print(

                child,

                indent + 4,

            )


# ==========================================================
# AST Validator
# ==========================================================

class ASTValidator:

    @staticmethod
    def validate(
        root: ASTNode,
    ) -> bool:

        if not isinstance(root, ASTNode):

            return False

        for child in root.children:

            if not ASTValidator.validate(child):

                return False

        return True


# ==========================================================
# Future Extension Hooks
# ==========================================================

FUTURE_AST_FEATURES = {

    "PATTERN_MATCHING": True,

    "GENERIC_TYPES": True,

    "TYPE_INFERENCE": True,

    "ASYNC_NODES": True,

    "COROUTINES": True,

    "DECORATORS": True,

    "ATTRIBUTES": True,

    "MACROS": False,

    "OPTIMIZER_HINTS": True,

    "REFLECTION": False,

}


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    "SourcePosition",

    "ASTNode",

    "ProgramNode",

    "ASTVisitor",

    "ASTWalker",

    "ASTStatistics",

    "ASTSerializer",

    "ASTExporter",

    "ASTPrettyPrinter",

    "ASTValidator",

]


# ==========================================================
# Self Test
# ==========================================================

if __name__ == "__main__":

    root = ProgramNode()

    child1 = ASTNode()

    child2 = ASTNode()

    child3 = ASTNode()

    root.add_statement(child1)

    root.add_statement(child2)

    child2.add_child(child3)

    print("=" * 70)

    print("Hekay AST Infrastructure")

    print("=" * 70)

    print()

    print("Pretty Print")

    ASTPrettyPrinter.print(root)

    print()

    print("Statistics")

    print(

        "Total Nodes :",

        ASTStatistics.total_nodes(root),

    )

    print(

        "Leaf Nodes :",

        ASTStatistics.leaf_nodes(root),

    )

    print(

        "Max Depth :",

        ASTStatistics.max_depth(root),

    )

    print()

    print("Validation")

    print(

        ASTValidator.validate(root)

    )

    print()

    print("JSON")

    print(

        ASTExporter.to_json(root)

    )

    print()

    print("Future Features")

    for key, value in FUTURE_AST_FEATURES.items():

        print(

            f"{key:<25}: {value}"

        )

    print()

    print("AST Infrastructure Loaded Successfully.")

    print("=" * 70)