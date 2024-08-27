def calculator ( a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return "Error: Invalid operator"
    

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

operator = input("Enter a opertor (+, -, *, /): ")

print(calculator(a,b,operator))

