"""
Hekay Programming Language

Module:
AST Nodes

Version:
3.1.0

Developer:
Dhiraj Kumar Mehangiya

Description:
Official AST Node definitions for the Hekay Parser.

This module defines every node used by the parser,
semantic analyzer, optimizer, bytecode generator,
HKVM and future compiler stages.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from compiler.parser.ast import ASTNode


# ==========================================================
# Module Information
# ==========================================================

MODULE_NAME = "AST Nodes"

MODULE_VERSION = "3.1.0"

SUPPORTED_COMPILER = "Hekay Compiler v3"


# ==========================================================
# Base Declaration Node
# ==========================================================

@dataclass(slots=True)
class DeclarationNode(ASTNode):
    """
    Base class for declarations.
    """

    name: str = ""


# ==========================================================
# Base Statement Node
# ==========================================================

@dataclass(slots=True)
class StatementNode(ASTNode):
    """
    Base class for statements.
    """

    pass


# ==========================================================
# Base Expression Node
# ==========================================================

@dataclass(slots=True)
class ExpressionNode(ASTNode):
    """
    Base class for expressions.
    """

    pass


# ==========================================================
# Base Literal Node
# ==========================================================

@dataclass(slots=True)
class LiteralNode(ExpressionNode):
    """
    Base class for literals.
    """

    value: object = None


# ==========================================================
# Variable Declaration
# ==========================================================

@dataclass(slots=True)
class VariableDeclarationNode(DeclarationNode):

    mutable: bool = True

    initializer: Optional[ExpressionNode] = None


# ==========================================================
# Constant Declaration
# ==========================================================

@dataclass(slots=True)
class ConstantDeclarationNode(DeclarationNode):

    initializer: Optional[ExpressionNode] = None


# ==========================================================
# Parameter Node
# ==========================================================

@dataclass(slots=True)
class ParameterNode(ASTNode):

    name: str

    type_name: Optional[str] = None

    default_value: Optional[ExpressionNode] = None


# ==========================================================
# Function Declaration
# ==========================================================

@dataclass(slots=True)
class FunctionDeclarationNode(DeclarationNode):

    parameters: List[ParameterNode] = field(default_factory=list)

    body: List[StatementNode] = field(default_factory=list)

    return_type: Optional[str] = None

    async_function: bool = False

# ==========================================================
# Class Declaration
# ==========================================================

@dataclass(slots=True)
class ClassDeclarationNode(DeclarationNode):
    """
    Represents a class declaration.
    """

    base_class: Optional[str] = None

    interfaces: List[str] = field(default_factory=list)

    members: List[ASTNode] = field(default_factory=list)

    is_abstract: bool = False

    is_final: bool = False


# ==========================================================
# Constructor Node
# ==========================================================

@dataclass(slots=True)
class ConstructorNode(ASTNode):
    """
    Represents a class constructor.
    """

    parameters: List[ParameterNode] = field(default_factory=list)

    body: List[StatementNode] = field(default_factory=list)


# ==========================================================
# Method Declaration
# ==========================================================

@dataclass(slots=True)
class MethodNode(DeclarationNode):
    """
    Represents a class method.
    """

    parameters: List[ParameterNode] = field(default_factory=list)

    body: List[StatementNode] = field(default_factory=list)

    return_type: Optional[str] = None

    is_static: bool = False

    is_virtual: bool = False

    is_override: bool = False

    is_async: bool = False


# ==========================================================
# Property Declaration
# ==========================================================

@dataclass(slots=True)
class PropertyNode(DeclarationNode):
    """
    Represents a class property.
    """

    type_name: Optional[str] = None

    initializer: Optional[ExpressionNode] = None

    readable: bool = True

    writable: bool = True


# ==========================================================
# Import Statement
# ==========================================================

@dataclass(slots=True)
class ImportNode(StatementNode):
    """
    Represents an import statement.
    """

    module: str = ""

    alias: Optional[str] = None


# ==========================================================
# Export Statement
# ==========================================================

@dataclass(slots=True)
class ExportNode(StatementNode):
    """
    Represents an export statement.
    """

    name: str = ""


# ==========================================================
# Namespace Declaration
# ==========================================================

@dataclass(slots=True)
class NamespaceNode(DeclarationNode):
    """
    Represents a namespace.
    """

    members: List[ASTNode] = field(default_factory=list)


# ==========================================================
# Module Node
# ==========================================================

@dataclass(slots=True)
class ModuleNode(ASTNode):
    """
    Represents a source module.
    """

    name: str = ""

    imports: List[ImportNode] = field(default_factory=list)

    exports: List[ExportNode] = field(default_factory=list)

    declarations: List[DeclarationNode] = field(default_factory=list)

    namespaces: List[NamespaceNode] = field(default_factory=list)

    body: List[StatementNode] = field(default_factory=list)

# ==========================================================
# Block Statement
# ==========================================================

@dataclass(slots=True)
class BlockStatementNode(StatementNode):
    """
    Represents a block of statements.
    """

    statements: List[StatementNode] = field(default_factory=list)


# ==========================================================
# Expression Statement
# ==========================================================

@dataclass(slots=True)
class ExpressionStatementNode(StatementNode):
    """
    Represents an expression used as a statement.
    """

    expression: Optional[ExpressionNode] = None


# ==========================================================
# If Statement
# ==========================================================

@dataclass(slots=True)
class IfStatementNode(StatementNode):
    """
    Represents an if statement.
    """

    condition: Optional[ExpressionNode] = None

    then_branch: Optional[BlockStatementNode] = None

    else_branch: Optional[BlockStatementNode] = None


# ==========================================================
# While Statement
# ==========================================================

@dataclass(slots=True)
class WhileStatementNode(StatementNode):
    """
    Represents a while loop.
    """

    condition: Optional[ExpressionNode] = None

    body: Optional[BlockStatementNode] = None


# ==========================================================
# For Statement
# ==========================================================

@dataclass(slots=True)
class ForStatementNode(StatementNode):
    """
    Represents a for loop.
    """

    initializer: Optional[StatementNode] = None

    condition: Optional[ExpressionNode] = None

    update: Optional[ExpressionNode] = None

    body: Optional[BlockStatementNode] = None


# ==========================================================
# Infinite Loop
# ==========================================================

@dataclass(slots=True)
class LoopStatementNode(StatementNode):
    """
    Represents an infinite loop.
    """

    body: Optional[BlockStatementNode] = None


# ==========================================================
# Break Statement
# ==========================================================

@dataclass(slots=True)
class BreakStatementNode(StatementNode):
    """
    Break current loop.
    """

    pass


# ==========================================================
# Continue Statement
# ==========================================================

@dataclass(slots=True)
class ContinueStatementNode(StatementNode):
    """
    Continue current loop.
    """

    pass


# ==========================================================
# Return Statement
# ==========================================================

@dataclass(slots=True)
class ReturnStatementNode(StatementNode):
    """
    Represents a return statement.
    """

    value: Optional[ExpressionNode] = None


# ==========================================================
# Throw Statement
# ==========================================================

@dataclass(slots=True)
class ThrowStatementNode(StatementNode):
    """
    Represents a throw statement.
    """

    exception: Optional[ExpressionNode] = None


# ==========================================================
# Try Statement
# ==========================================================

@dataclass(slots=True)
class TryStatementNode(StatementNode):
    """
    Represents a try statement.
    """

    body: Optional[BlockStatementNode] = None

    catches: List["CatchStatementNode"] = field(default_factory=list)

    finally_block: Optional["FinallyStatementNode"] = None


# ==========================================================
# Catch Statement
# ==========================================================

@dataclass(slots=True)
class CatchStatementNode(StatementNode):
    """
    Represents a catch statement.
    """

    exception_name: str = ""

    body: Optional[BlockStatementNode] = None


# ==========================================================
# Finally Statement
# ==========================================================

@dataclass(slots=True)
class FinallyStatementNode(StatementNode):
    """
    Represents a finally block.
    """

    body: Optional[BlockStatementNode] = None


# ==========================================================
# Match Statement
# ==========================================================

@dataclass(slots=True)
class MatchStatementNode(StatementNode):
    """
    Represents a match statement.
    """

    expression: Optional[ExpressionNode] = None

    cases: List["CaseStatementNode"] = field(default_factory=list)


# ==========================================================
# Case Statement
# ==========================================================

@dataclass(slots=True)
class CaseStatementNode(StatementNode):
    """
    Represents a match case.
    """

    pattern: Optional[ExpressionNode] = None

    body: Optional[BlockStatementNode] = None

# ==========================================================
# Binary Expression
# ==========================================================

@dataclass(slots=True)
class BinaryExpressionNode(ExpressionNode):
    """
    Represents a binary expression.
    """

    left: Optional[ExpressionNode] = None

    operator: str = ""

    right: Optional[ExpressionNode] = None


# ==========================================================
# Unary Expression
# ==========================================================

@dataclass(slots=True)
class UnaryExpressionNode(ExpressionNode):
    """
    Represents a unary expression.
    """

    operator: str = ""

    operand: Optional[ExpressionNode] = None


# ==========================================================
# Assignment Expression
# ==========================================================

@dataclass(slots=True)
class AssignmentExpressionNode(ExpressionNode):
    """
    Represents an assignment.
    """

    target: Optional[ExpressionNode] = None

    operator: str = "="

    value: Optional[ExpressionNode] = None


# ==========================================================
# Function Call
# ==========================================================

@dataclass(slots=True)
class CallExpressionNode(ExpressionNode):
    """
    Represents a function call.
    """

    callee: Optional[ExpressionNode] = None

    arguments: List[ExpressionNode] = field(default_factory=list)


# ==========================================================
# Member Access
# ==========================================================

@dataclass(slots=True)
class MemberAccessNode(ExpressionNode):
    """
    Represents object member access.
    """

    object: Optional[ExpressionNode] = None

    member: str = ""


# ==========================================================
# Index Expression
# ==========================================================

@dataclass(slots=True)
class IndexExpressionNode(ExpressionNode):
    """
    Represents array indexing.
    """

    collection: Optional[ExpressionNode] = None

    index: Optional[ExpressionNode] = None


# ==========================================================
# Lambda Expression
# ==========================================================

@dataclass(slots=True)
class LambdaExpressionNode(ExpressionNode):
    """
    Represents a lambda expression.
    """

    parameters: List[ParameterNode] = field(default_factory=list)

    body: Optional[ExpressionNode] = None


# ==========================================================
# Range Expression
# ==========================================================

@dataclass(slots=True)
class RangeExpressionNode(ExpressionNode):
    """
    Represents a range expression.
    """

    start: Optional[ExpressionNode] = None

    end: Optional[ExpressionNode] = None

    inclusive: bool = True


# ==========================================================
# Object Creation
# ==========================================================

@dataclass(slots=True)
class NewExpressionNode(ExpressionNode):
    """
    Represents object creation.
    """

    class_name: str = ""

    arguments: List[ExpressionNode] = field(default_factory=list)


# ==========================================================
# Await Expression
# ==========================================================

@dataclass(slots=True)
class AwaitExpressionNode(ExpressionNode):
    """
    Represents an await expression.
    """

    expression: Optional[ExpressionNode] = None


# ==========================================================
# Cast Expression
# ==========================================================

@dataclass(slots=True)
class CastExpressionNode(ExpressionNode):
    """
    Represents a type cast.
    """

    expression: Optional[ExpressionNode] = None

    target_type: str = ""


# ==========================================================
# Ternary Expression
# ==========================================================

@dataclass(slots=True)
class TernaryExpressionNode(ExpressionNode):
    """
    Represents a ternary expression.
    """

    condition: Optional[ExpressionNode] = None

    true_expression: Optional[ExpressionNode] = None

    false_expression: Optional[ExpressionNode] = None


# ==========================================================
# Tuple Expression
# ==========================================================

@dataclass(slots=True)
class TupleExpressionNode(ExpressionNode):
    """
    Represents a tuple expression.
    """

    values: List[ExpressionNode] = field(default_factory=list)


# ==========================================================
# Array Expression
# ==========================================================

@dataclass(slots=True)
class ArrayExpressionNode(ExpressionNode):
    """
    Represents an array expression.
    """

    elements: List[ExpressionNode] = field(default_factory=list)


# ==========================================================
# Object Expression
# ==========================================================

@dataclass(slots=True)
class ObjectExpressionNode(ExpressionNode):
    """
    Represents an object literal.
    """

    properties: dict[str, ExpressionNode] = field(default_factory=dict)

# ==========================================================
# Literal Nodes
# ==========================================================

@dataclass(slots=True)
class NumberLiteralNode(LiteralNode):
    """
    Represents a numeric literal.
    """
    value: int | float = 0


@dataclass(slots=True)
class StringLiteralNode(LiteralNode):
    """
    Represents a string literal.
    """
    value: str = ""


@dataclass(slots=True)
class BooleanLiteralNode(LiteralNode):
    """
    Represents a boolean literal.
    """
    value: bool = False


@dataclass(slots=True)
class CharacterLiteralNode(LiteralNode):
    """
    Represents a character literal.
    """
    value: str = ""


@dataclass(slots=True)
class NullLiteralNode(LiteralNode):
    """
    Represents a null literal.
    """
    value = None


# ==========================================================
# Identifier Node
# ==========================================================

@dataclass(slots=True)
class IdentifierNode(ExpressionNode):
    """
    Represents an identifier.
    """

    name: str = ""


# ==========================================================
# Special Nodes
# ==========================================================

@dataclass(slots=True)
class ThisNode(ExpressionNode):
    """
    Represents 'this'.
    """
    pass


@dataclass(slots=True)
class SuperNode(ExpressionNode):
    """
    Represents 'super'.
    """
    pass


# ==========================================================
# Future Type Nodes
# ==========================================================

@dataclass(slots=True)
class GenericTypeNode(ASTNode):
    """
    Generic type support.
    """

    name: str = ""

    parameters: List[str] = field(default_factory=list)


@dataclass(slots=True)
class AnnotationNode(ASTNode):
    """
    Future annotations.
    """

    name: str = ""

    arguments: List[ExpressionNode] = field(default_factory=list)


@dataclass(slots=True)
class DecoratorNode(ASTNode):
    """
    Future decorators.
    """

    name: str = ""

    arguments: List[ExpressionNode] = field(default_factory=list)


# ==========================================================
# Future Features
# ==========================================================

FUTURE_AST_NODES = {

    "PATTERN_MATCHING": True,

    "COROUTINES": True,

    "ASYNC_AWAIT": True,

    "GENERICS": True,

    "DECORATORS": True,

    "ANNOTATIONS": True,

    "MACROS": False,

    "REFLECTION": False,

    "COMPILER_ATTRIBUTES": True,

    "METAPROGRAMMING": False,

}


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    name

    for name in globals()

    if name.endswith("Node")

] + [

    "FUTURE_AST_NODES",

]


# ==========================================================
# Self Test
# ==========================================================

if __name__ == "__main__":

    print("=" * 70)

    print("Hekay AST Nodes")

    print("=" * 70)

    print()

    print("Registered AST Nodes")

    node_count = 0

    for name in sorted(__all__):

        print(name)

        node_count += 1

    print()

    print(f"Total AST Types : {node_count}")

    print()

    print("Future Features")

    for feature, enabled in FUTURE_AST_NODES.items():

        print(f"{feature:<25}: {enabled}")

    print()

    print("AST Node Library Loaded Successfully.")

    print("=" * 70)