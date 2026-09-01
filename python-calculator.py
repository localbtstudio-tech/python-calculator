print("==========================")
print("     PYTHON CALCULATOR")
print("==========================")

exist = "O"

while exist != "N":

    number1 = float(input("Give me the first number: "))
    number2 = float(input("Give me the second number: "))

    op = input("Choose the operation: + | - | * | / :")

    if op == "+":
        s = number1 + number2
        print(f"Result: {s}")

    elif op == "-":
        s = number1 - number2
        print(f"Result: {s}")

    elif op == "*":
        s = number1 * number2
        print(f"Result: {s}")

    elif op == "/":
        if number2 != 0:
            s = number1 / number2
            print(f"Result: {s}")
        else:
            print("Error: Cannot divide by zero.")

    else:
        print("Error: Choose a correct operation.")

    exist = input("Do you want to continue? O/N: ").upper()

print("Goodbye!")