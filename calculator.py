operation = input("Operation: ")


if "+" in operation:
    operation_left, operation_right = operation.split("+")
    addition = int(operation_left) + int(operation_right)
    print(addition)

elif "-" in operation:
    operation_left, operation_right = operation.split("-")
    subtraction = int(operation_left) - int(operation_right)
    print(subtraction)

elif "x" in operation or "*" in operation:

    if 'x' in operation:
        operation_left, operation_right = operation.split("x")
    else:
        operation_left, operation_right = operation.split("*")

    multiplication = int(operation_left) * int(operation_right)
    print(multiplication)

elif "/" in operation:
    operation_left, operation_right = operation.split("/")
    division = int(operation_left) / int(operation_right)
    print(division)
