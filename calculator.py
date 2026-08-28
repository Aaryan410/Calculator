a = int(input("What is a? "))
b = int(input("What is b? "))

sign = input("What operation? ")

if sign == '+':
    addition = a + b
    print(addition)
elif sign == '-':
    substraction = a - b
    print(substraction)
elif sign == '*':
    multiplication = a * b
    print(multiplication)
elif sign == '/':
    division = a / b
    print(division)
