# Hekay Official Error Handling v1.0

**Developer:** Dhiraj Kumar Mehangiya

**Version:** 1.0

**Status:** Draft

---

## What is Error Handling?

Error handling allows programs to detect and manage errors without crashing.

---

## Error Keywords

| Keyword | Description |
| ---------- | ------------- |
| `try` | Execute risky code |
| `catch` | Handle an error |
| `throw` | Generate an error |
| `finally` | Always execute |

---

## Example

```hky
try {

    show "Connecting..."

} catch {

    show "Connection Failed"

} finally {

    show "Process Finished"

}
```

---

## Notes

- Use `try` for risky operations.
- Use `catch` to handle errors.
- Use `finally` for cleanup tasks.
