from engine import calculator

print(40 * '=')
print("Calculator")
print(40 * '=')

print()
operation = input("Operation: ")

result = calculator(operation)

print()
print(f"Answer: {result}")
