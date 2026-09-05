from time import sleep


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def display_menu():
    print("\n" + "=" * 35)
    print("         PYTHON CALCULATOR")
    print("=" * 35)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("=" * 35)


def calculate(choice, number1, number2):
    if choice == "1":
        return add(number1, number2)

    elif choice == "2":
        return subtract(number1, number2)

    elif choice == "3":
        return multiply(number1, number2)

    elif choice == "4":
        return divide(number1, number2)

    return None


def main():
    while True:
        display_menu()

        choice = input("Choose an option: ").strip()

        if choice == "5":
            print("\nGoodbye! 👋")
            break

        if choice not in ("1", "2", "3", "4"):
            print("\nInvalid option.")
            continue

        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        result = calculate(choice, number1, number2)

        if choice == "4" and number2 == 0:
            print("\nError: Cannot divide by zero.")
        else:
            print(f"\nResult: {result}")

        sleep(1)


if __name__ == "__main__":
    main()