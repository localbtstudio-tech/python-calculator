# PYTHON CALCULATOR 🧮

<div align="center">

### A clean command-line calculator built with Python.

**Python · Functions · Control Flow · CLI**

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

</div>

---

## ◼︎ The Project

A simple but structured **command-line calculator** built from scratch with Python.

The goal wasn't just to make calculations work — it was to practice writing a program using **functions, conditions, loops, input handling, and basic error handling**.

> **Small project. Real fundamentals.**

---

## ✦ What It Can Do

```text
┌─────────────────────────────┐
│      PYTHON CALCULATOR      │
├─────────────────────────────┤
│  1. Addition                │
│  2. Subtraction             │
│  3. Multiplication          │
│  4. Division                │
│  5. Exit                    │
└─────────────────────────────┘
```

### Operations

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* 🚫 Division-by-zero protection
* 🔄 Continuous calculation loop
* ❌ Invalid option handling
* 👋 Clean exit

---

## ⚙️ How It Works

The calculator separates each operation into its own function:

```text
                  USER INPUT
                      │
                      ▼
                Display Menu
                      │
                      ▼
                Select Option
                      │
                      ▼
                 Get Numbers
                      │
                      ▼
                  calculate()
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
        add()    subtract()    multiply()
                                  │
                                  ▼
                               divide()
                                  │
                                  ▼
                               RESULT
```

This keeps the code simple, readable, and reusable.

---

## 🧠 Concepts Practiced

| Concept        | Used For                       |
| -------------- | ------------------------------ |
| `def`          | Creating reusable functions    |
| `if / elif`    | Selecting operations           |
| `while`        | Keeping the calculator running |
| `input()`      | Receiving user input           |
| `float()`      | Handling decimal numbers       |
| `return`       | Returning calculation results  |
| `strip()`      | Cleaning user input            |
| Error handling | Preventing division by zero    |
| `sleep()`      | Adding a small UI delay        |

---

## 🚀 Run It

### 1. Clone the repository

```bash
git clone https://github.com/localbtstudio-tech/python-calculator.git
```

### 2. Enter the project

```bash
cd python-calculator
```

### 3. Run the program

```bash
python main.py
```

---

## 🎮 Example

```text
===================================
         PYTHON CALCULATOR
===================================
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
===================================

Choose an option: 1
Enter first number: 15
Enter second number: 7

Result: 22.0
```

---

## 📁 Project Structure

```text
python-calculator/
│
├── main.py
├── README.md
└── .gitignore
```

---

## ◼︎ Why I Built This

This project is part of my **Python learning journey**, focusing on strengthening programming fundamentals before moving into more advanced topics.

The project helped me practice:

**Logic → Functions → Control Flow → User Input → Error Handling**

---

## 🔮 Next Steps

Possible improvements:

* [ ] Add percentage calculations
* [ ] Add exponentiation
* [ ] Add square root
* [ ] Improve input error handling
* [ ] Add calculation history
* [ ] Build a GUI version
* [ ] Add automated tests

---

## 👨‍💻 Author

**Hamza Weslati**

IT Student · Web Developer

[GitHub](https://github.com/localbtstudio-tech)

---

<div align="center">

### 🧮 PYTHON CALCULATOR

*Built with Python. One function at a time.*

**© 2026 Hamza Weslati**

</div>
