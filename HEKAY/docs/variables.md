# Hekay Official Variables v1.0

**Developer:** Dhiraj Kumar Mehangiya

**Version:** 1.0

**Status:** Draft

---

## What is a Variable?

A variable is a named memory location used to store data.

---

## Variable Keywords

| Keyword | Description |
| ---------- | ------------- |
| `het` | Mutable Variable (Value can be changed) |
| `hook` | Constant Variable (Value cannot be changed) |

---

## Variable Naming Rules

- Variable names must start with a letter (A-Z or a-z).
- Numbers can be used after the first letter.
- Underscore (`_`) is allowed.
- Spaces are not allowed.
- Keywords cannot be used as variable names.

---

## Valid Variable Names

```hky
het age = 18

het userName = "Hekay"

het student_1 = "Rahul"
```

---

## Invalid Variable Names

```hky
het 123name = "Error"

het my name = "Error"

het if = 20
```

---

## Constant Variable

```hky
hook PI = 3.14159
```

---

## Mutable Variable

```hky
het score = 100

score = 200
```

---

## Notes

- Use `het` for normal variables.
- Use `hook` for constants.
- Variable names should be meaningful and easy to understand.
