# Hekay Official Classes v1.0

**Developer:** Dhiraj Kumar Mehangiya

**Version:** 1.0

**Status:** Draft

---

## What is a Class?

A class is a blueprint used to create objects.

---

## Class Keywords

| Keyword | Description |
| ---------- | ------------- |
| `class` | Create a new class |
| `new` | Create a new object |
| `this` | Reference the current object |
| `extends` | Inherit another class |
| `super` | Access the parent class |

---

## Basic Class

```hky
class Robot {

}
```

---

## Creating an Object

```hky
het bot = new Robot()
```

---

## Class with Properties

```hky
class Robot {

    het name = "Robo"

}
```

---

## Class with Functions

```hky
class Robot {

    func move() {

        show "Robot Moving"

    }

}
```

---

## Using an Object

```hky
het bot = new Robot()

bot.move()
```

---

## Inheritance

```hky
class SmartRobot extends Robot {

}
```

---

## Notes

- A class defines the structure of an object.
- Objects are created using the `new` keyword.
- Use `extends` to inherit another class.
