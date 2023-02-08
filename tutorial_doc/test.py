def calculate():
    print("Welcome to the Calculator App!")
    print("-----------------------------")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        result = num1 + num2
        print("Result: ", num1, operator, num2, "=", result)
    elif operator == "-":
        result = num1 - num2
        print("Result: ", num1, operator, num2, "=", result)
    elif operator == "*":
        result = num1 * num2
        print("Result: ", num1, operator, num2, "=", result)
    elif operator == "/":
        result = num1 / num2
        print("Result: ", num1, operator, num2, "=", result)
    else:
        print("Invalid operator entered. Please try again.")

calculate()