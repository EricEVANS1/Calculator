#Calculator
print("Here is Calculator")

while True:
    try:
        num1 = float(input("What is your first number?: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("What is your second number?: "))

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            if num2 == 0:
                print("ERROR: division is not applicable")
                continue
            result = num1 / num2

        else:
            print("Invalid operator")
            continue

        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers")
        continue

    choice = input("Would you like to continue? (y/n): ")
    if choice.lower() != "y":
        print("Calculator stopped")
        break
