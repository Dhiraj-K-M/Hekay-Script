# Hekay Official Development Standards v3.0

**Project:** Hekay Programming Language

**Version:** 3.0

**Status:** Official Standard

**Developer:** Dhiraj Kumar Mehangiya

**License:** MIT License

**Repository:** <https://github.com/Dhiraj-K-M/Hekay>

**Official Website:** *(Future)* <https://hekay.org>

---

## Table of Contents

1. Purpose
2. Project Philosophy
3. Folder Naming Rules
4. File Naming Rules
5. Coding Standards
6. Documentation Standards
7. Versioning Policy
8. Git Branch Strategy
9. Commit Message Rules
10. Testing Standards
11. Release Process
12. API Design Rules
13. Security Guidelines
14. Performance Guidelines
15. Future Compatibility
16. Long-Term Vision

---

## Purpose

This document defines the official development standards for the Hekay Programming Language.

Every contributor must follow these standards.

The goal is to keep the project:

- Clean
- Consistent
- Professional
- Maintainable
- Future Ready

---

## Project Philosophy

Hekay follows these principles:

- Simplicity First
- Readability Matters
- Performance Matters
- Security by Default
- Modular Design
- Cross Platform
- Future Ready
- Developer Friendly

---

## Folder Naming Rules

Folder names must use lowercase letters.

Correct

```txt
compiler/
lexer/
parser/
runtime/
stdlib/
docs/
examples/
tests/
sdk/
```

Wrong

```txt
Compiler/
Lexer/
Parser/
MyFolder/
```

---

## File Naming Rules

Python files

```txt
token.py

lexer.py

scanner.py

operators.py

memory.py
```

Documentation

```txt
README.md

compiler_architecture.md

development_standards.md

language_specification.md
```

---

## Coding Standards

Every Python file must include:

- Module Documentation
- Version Information
- Developer Information
- Type Hints
- Error Handling
- Clean OOP Design
- Future Compatibility

Example

```python
"""
Hekay Programming Language

Lexer

Developer: Dhiraj Kumar Mehangiya
"""
```

---

## Naming Conventions

Variables

```python
token_type

current_position

source_code
```

Classes

```python
Lexer

Parser

Interpreter
```

Constants

```python
MAX_LENGTH

VERSION

DEFAULT_ENCODING
```

Functions

```python
scan()

parse()

execute()

compile()
```

---

## Documentation Standards

Every Markdown document must contain:

- Title
- Version
- Developer
- Repository
- Table of Contents
- Sections
- Examples
- Notes

Use:

```md
#

##

###

```

Always specify code block language.

Example

````text
```python
```

```hky
```

```txt
```
