#Python Simple Arithmetic Calculator.
#It performs basic arithmetic operations between 2 numbers.
# Operators: +, -, *, /

Num1 = float(input("Enter a number: "))
Num2 = float(input("Enter another number: "))
Operation = input("Enter the respective operand((+)- Addition/(-)- Subtraction/(*)- Multiplication/(/)- Division): ")

if Operation == "+":
    print(Num1 + Num2)
elif Operation == "-":
    print(Num1 - Num2)
elif Operation == "*":
    print(Num1 * Num2)
elif Operation == "/":
    print(Num1 / Num2)