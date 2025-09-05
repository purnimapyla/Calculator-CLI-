import math

def calculator():
    print("===== Python CLI Calculator =====")
    print("Available operations:")
    print(" +  : Addition")
    print(" -  : Subtraction")
    print(" *  : Multiplication")
    print(" /  : Division")
    print(" ** : Power")
    print(" sqrt : Square root")
    print(" exit : Quit the calculator")

    while True:
        op = input("\nEnter operation (+, -, *, /, **, sqrt, exit): ")

        if op == "exit":
            print("Goodbye!")
            break

        try:
            if op == "sqrt":
                num = float(input("Enter number: "))
                print("Result:", math.sqrt(num))
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if op == "+":
                    print("Result:", num1 + num2)
                elif op == "-":
                    print("Result:", num1 - num2)
                elif op == "*":
                    print("Result:", num1 * num2)
                elif op == "/":
                    if num2 == 0:
                        print("Error! Division by zero.")
                    else:
                        print("Result:", num1 / num2)
                elif op == "**":
                    print("Result:", num1 ** num2)
                else:
                    print("Invalid operation!")
        except ValueError:
            print("Invalid input! Please enter numbers.")

# Run calculator
calculator()
