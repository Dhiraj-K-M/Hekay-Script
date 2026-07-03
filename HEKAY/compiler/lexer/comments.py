"""
Hekay Programming Language

Module:
Comment Parser

Version:
3.1.0

Developer:
Dhiraj Kumar Mehangiya

Description:
Official Comment Parser for the Hekay Lexer.

Supports:

• Single Line Comments
• Multi Line Comments
• Nested Comments
• Documentation Comments
• TODO Extraction
• FIXME Extraction
• Future Annotation Support
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import List

from compiler.lexer.scanner import Scanner


# ==========================================================
# Module Information
# ==========================================================

MODULE_NAME = "Comment Parser"

MODULE_VERSION = "3.1.0"

SUPPORTED_COMPILER = "Hekay Compiler v3"


# ==========================================================
# Comment Types
# ==========================================================

class CommentType(Enum):

    SINGLE_LINE = auto()

    MULTI_LINE = auto()

    DOC_LINE = auto()

    DOC_BLOCK = auto()


# ==========================================================
# Comment Token
# ==========================================================

@dataclass(slots=True)
class CommentValue:

    text: str

    comment_type: CommentType

    line: int

    column: int


# ==========================================================
# Comment Parser
# ==========================================================

class CommentParser:

    """
    Production Comment Parser.
    """

    def __init__(

        self,

        scanner: Scanner,

    ):

        self.scanner = scanner

    # ------------------------------------------------------

    def parse(self) -> CommentValue:

        line, column = self.scanner.location()

        if self.scanner.current() == "#":

            return self.read_hash_comment(

                line,

                column,

            )

        if (

            self.scanner.current() == "/"

            and self.scanner.peek() == "/"

        ):

            return self.read_slash_comment(

                line,

                column,

            )

        if (

            self.scanner.current() == "/"

            and self.scanner.peek() == "*"

        ):

            return self.read_block_comment(

                line,

                column,

            )

        raise ValueError(

            "Expected comment."

        )

    # ------------------------------------------------------

    def create(

        self,

        text: str,

        comment_type: CommentType,

        line: int,

        column: int,

    ) -> CommentValue:

        return CommentValue(

            text=text,

            comment_type=comment_type,

            line=line,

            column=column,

        )
        # ------------------------------------------------------
    # Hash Comment (# ...)
    # ------------------------------------------------------

    def read_hash_comment(
        self,
        line: int,
        column: int,
    ) -> CommentValue:
        """
        Read Python-style hash comment.
        """

        self.scanner.advance()  # Skip #

        text = []

        while (
            not self.scanner.eof()
            and self.scanner.current() != "\n"
        ):
            text.append(
                self.scanner.advance()
            )

        return self.create(
            "".join(text).strip(),
            CommentType.SINGLE_LINE,
            line,
            column,
        )

    # ------------------------------------------------------
    # Slash Comment (// ...)
    # ------------------------------------------------------

    def read_slash_comment(
        self,
        line: int,
        column: int,
    ) -> CommentValue:
        """
        Read C/Java style line comment.
        """

        self.scanner.advance()   # /
        self.scanner.advance()   # /

        doc = False

        if self.scanner.current() == "/":

            doc = True

            self.scanner.advance()

        text = []

        while (
            not self.scanner.eof()
            and self.scanner.current() != "\n"
        ):
            text.append(
                self.scanner.advance()
            )

        return self.create(

            "".join(text).strip(),

            CommentType.DOC_LINE if doc else CommentType.SINGLE_LINE,

            line,

            column,

        )

    # ------------------------------------------------------
    # Block Comment
    # ------------------------------------------------------

    def read_block_comment(
        self,
        line: int,
        column: int,
    ) -> CommentValue:
        """
        Read block comment.
        Supports nested comments.
        """

        self.scanner.advance()   # /
        self.scanner.advance()   # *

        doc = False

        if self.scanner.current() == "*":

            doc = True

            self.scanner.advance()

        level = 1

        text = []

        while not self.scanner.eof():

            # Nested /*
            if (
                self.scanner.current() == "/"
                and self.scanner.peek() == "*"
            ):

                level += 1

                text.append(
                    self.scanner.advance()
                )

                text.append(
                    self.scanner.advance()
                )

                continue

            # End */
            if (
                self.scanner.current() == "*"
                and self.scanner.peek() == "/"
            ):

                level -= 1

                self.scanner.advance()
                self.scanner.advance()

                if level == 0:

                    break

                continue

            text.append(
                self.scanner.advance()
            )

        return self.create(

            "".join(text).strip(),

            CommentType.DOC_BLOCK if doc else CommentType.MULTI_LINE,

            line,

            column,

        )

    # ------------------------------------------------------
    # TODO / FIXME Extraction
    # ------------------------------------------------------

    @staticmethod
    def extract_tasks(
        comment: CommentValue,
    ) -> List[str]:
        """
        Extract TODO / FIXME notes.
        """

        tasks = []

        for line in comment.text.splitlines():

            text = line.strip()

            upper = text.upper()

            if upper.startswith("TODO"):

                tasks.append(text)

            elif upper.startswith("FIXME"):

                tasks.append(text)

            elif upper.startswith("BUG"):

                tasks.append(text)

            elif upper.startswith("NOTE"):

                tasks.append(text)

        return tasks

        # ------------------------------------------------------
    # Validation Helpers
    # ------------------------------------------------------

    @staticmethod
    def is_single_line(comment: CommentValue) -> bool:
        """
        Check whether the comment is a single-line comment.
        """
        return comment.comment_type == CommentType.SINGLE_LINE

    @staticmethod
    def is_multi_line(comment: CommentValue) -> bool:
        """
        Check whether the comment is a multi-line comment.
        """
        return comment.comment_type == CommentType.MULTI_LINE

    @staticmethod
    def is_doc_comment(comment: CommentValue) -> bool:
        """
        Check whether the comment is a documentation comment.
        """
        return comment.comment_type in (
            CommentType.DOC_LINE,
            CommentType.DOC_BLOCK,
        )

    @staticmethod
    def has_tasks(comment: CommentValue) -> bool:
        """
        Check if TODO/FIXME exists.
        """
        return len(
            CommentParser.extract_tasks(comment)
        ) > 0

    # ------------------------------------------------------
    # Annotation Extraction
    # ------------------------------------------------------

    @staticmethod
    def extract_annotations(
        comment: CommentValue,
    ) -> List[str]:
        """
        Extract @annotations from comments.
        """

        annotations: List[str] = []

        for line in comment.text.splitlines():

            line = line.strip()

            if line.startswith("@"):

                annotations.append(line)

        return annotations

    # ------------------------------------------------------
    # Statistics
    # ------------------------------------------------------

    @staticmethod
    def supported_types() -> tuple[CommentType, ...]:
        """
        Return all supported comment types.
        """
        return tuple(CommentType)

    @staticmethod
    def statistics() -> dict:
        """
        Return module statistics.
        """

        return {

            "module": MODULE_NAME,

            "version": MODULE_VERSION,

            "supported_comment_types": len(CommentType),

            "nested_comments": True,

            "documentation_comments": True,

            "todo_support": True,

            "fixme_support": True,

            "annotation_support": True,

        }

    # ------------------------------------------------------
    # Magic Methods
    # ------------------------------------------------------

    def __repr__(self) -> str:

        return (

            f"CommentParser("

            f"version={MODULE_VERSION!r}, "

            f"compiler={SUPPORTED_COMPILER!r}"

            f")"

        )


# ==========================================================
# Future Features
# ==========================================================

FUTURE_COMMENT_FEATURES = {

    "MARKDOWN_DOCS": False,

    "JAVADOC_STYLE": True,

    "XML_DOCS": False,

    "AUTO_DOCUMENTATION": False,

    "LINT_HINTS": True,

    "REGION_SUPPORT": True,

    "CODE_FOLDING": True,

    "ANNOTATIONS": True,

}


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    "CommentType",

    "CommentValue",

    "CommentParser",

]


# ==========================================================
# Self Test
# ==========================================================

if __name__ == "__main__":

    print("=" * 70)

    print("Hekay Comment Parser v3.1")

    print("=" * 70)

    print()

    print("Supported Comment Types:")

    for item in CommentParser.supported_types():

        print(" -", item.name)

    print()

    print("Statistics")

    print(CommentParser.statistics())

    print()

    print("Future Features")

    for key, value in FUTURE_COMMENT_FEATURES.items():

        print(f"{key:<25}: {value}")

    print()

    sample = CommentValue(

        text="""
TODO: Improve parser
FIXME: Handle nested comments
@author Dhiraj
@since 3.1
@version 3.1
""",

        comment_type=CommentType.DOC_BLOCK,

        line=1,

        column=1,

    )

    print("Detected Tasks:")

    for task in CommentParser.extract_tasks(sample):

        print(" -", task)

    print()

    print("Detected Annotations:")

    for annotation in CommentParser.extract_annotations(sample):

        print(" -", annotation)

    print()

    print("Comment Parser Loaded Successfully.")

    print("=" * 70)
    