"""
Hekay Programming Language

Common Definitions

Developer: Dhiraj Kumar Mehangiya

Version: 3.0

License: MIT
"""

from enum import Enum
from typing import Final


# ==========================================================
# Language Information
# ==========================================================

LANGUAGE_NAME: Final[str] = "Hekay"

LANGUAGE_VERSION: Final[str] = "3.0"

LANGUAGE_EXTENSION: Final[str] = ".hky"

LANGUAGE_ENCODING: Final[str] = "utf-8"


# ==========================================================
# Compiler Information
# ==========================================================

COMPILER_NAME: Final[str] = "Hekay Compiler"

COMPILER_SHORT_NAME: Final[str] = "hkc"

INTERPRETER_NAME: Final[str] = "Hekay Interpreter"

INTERPRETER_SHORT_NAME: Final[str] = "hki"

PACKAGE_MANAGER: Final[str] = "hk"

VM_NAME: Final[str] = "HKVM"


# ==========================================================
# Official Project Information
# ==========================================================

DEVELOPER: Final[str] = "Dhiraj Kumar Mehangiya"

LICENSE: Final[str] = "MIT"

REPOSITORY: Final[str] = "https://github.com/Dhiraj-K-M/Hekay"


# ==========================================================
# Build Information
# ==========================================================

BUILD_STAGE: Final[str] = "Development"

BUILD_NUMBER: Final[int] = 1


# ==========================================================
# Runtime Limits
# ==========================================================

MAX_IDENTIFIER_LENGTH: Final[int] = 255

MAX_STRING_LENGTH: Final[int] = 65535

MAX_NUMBER_LENGTH: Final[int] = 1024


# ==========================================================
# Supported Number Systems
# ==========================================================

class NumberSystem(Enum):

    DECIMAL = 10

    BINARY = 2

    OCTAL = 8

    HEXADECIMAL = 16


# ==========================================================
# Supported Line Endings
# ==========================================================

class LineEnding(Enum):

    UNIX = "\n"

    WINDOWS = "\r\n"

    MAC = "\r"


# ==========================================================
# Future Reserved Features
# ==========================================================

FUTURE_FEATURES = {

    "AI",

    "ROBOTICS",

    "GAME",

    "WEB",

    "ANDROID",

    "DESKTOP",

    "DATABASE",

    "NETWORK",

    "SPACE",

    "DRONE",

    "VOICE",

    "CAMERA",

    "GRAPHICS",

    "CLOUD",

}