# Basic Calculator Program


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(str(num1) + " + " + str(num2) + " = " + str(result))
elif operation == "-":
    result = num1 - num2
    print(str(num1) + " - " + str(num2) + " = " + str(result))
elif operation == "*":
    result = num1 * num2
    print(str(num1) + " * " + str(num2) + " = " + str(result))
elif operation == "/":
    result = num1 / num2
    print(str(num1) + " / " + str(num2) + " = " + str(result))
else:
    print("Invalid operation")
