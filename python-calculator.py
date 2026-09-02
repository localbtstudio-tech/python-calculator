print("==========================")
print("     PYTHON CALCULATOR")
print("==========================")

exist = "O"


def add(number1, number2):
    return number1 + number2


def sub(number1, number2):
    return number1 - number2


def multi(number1, number2):
    return number1 * number2


def div(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        return None


while exist != "N":

    number1 = float(input("Give me the first number: "))
    number2 = float(input("Give me the second number: "))

    op = input("Choose the operation: + | - | * | / ")

    if op == "+":
        s = add(number1, number2)
        print(f"Result: {s}")

    elif op == "-":
        s = sub(number1, number2)
        print(f"Result: {s}")

    elif op == "*":
        s = multi(number1, number2)
        print(f"Result: {s}")

    elif op == "/":
        s = div(number1, number2)

        if s is None:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Result: {s}")

    else:
        print("Invalid operation.")

    exist = input("Do you want to continue? O/N: ").upper()

print("Goodbye!")
