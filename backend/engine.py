
def calculator(operation):

    if "+" in operation:
        operation_left, operation_right = operation.split("+")
        addition = int(operation_left) + int(operation_right)
        return addition

    elif "-" in operation:
        operation_left, operation_right = operation.split("-")
        subtraction = int(operation_left) - int(operation_right)
        return subtraction

    elif "x" in operation or "*" in operation:

        if 'x' in operation:
            operation_left, operation_right = operation.split("x")
        else:
            operation_left, operation_right = operation.split("*")

        multiplication = int(operation_left) * int(operation_right)
        return multiplication

    elif "/" in operation:
        operation_left, operation_right = operation.split("/")
        division = int(operation_left) / int(operation_right)
        return division

    
