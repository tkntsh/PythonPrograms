# enhanced_calculator.py
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /, %, **): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
elif operation == '%':
    result = num1 % num2
elif operation == '**':
    result = num1 ** num2
else:
    result = "Invalid operation"

print("Result:", result)

again = input("Calculate again (yes/no)? ")
if again == "yes":
    print("Restart the program!")
else:
    print("Goodbye!")