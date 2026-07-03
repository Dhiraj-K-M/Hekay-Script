# Hekay Official Functions v1.0

**Developer:** Dhiraj Kumar Mehangiya

**Version:** 1.0

**Status:** Draft

---

## What is a Function?

A function is a reusable block of code that performs a specific task.

---

## Function Keyword

| Keyword | Description |
| ---------- | ------------- |
| `func` | Create a function |
| `return` | Return a value from a function |

---

## Basic Function

```hky
func hello() {

    show "Hello Hekay"

}
```

---

## Calling a Function

```hky
hello()
```

---

## Function with Parameters

```hky
func welcome(name) {

    show name

}

welcome("Dhiraj")
```

---

## Function with Return Value

```hky
func add(a, b) {

    return a + b

}

het result = add(10, 20)

show result
```

---

## Notes

- Functions should perform one task.
- Function names should be meaningful.
- Use `return` when a value needs to be sent back.
