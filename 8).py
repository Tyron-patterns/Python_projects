def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def first_calculation():
    num1 = float(input("Enter the first number: "))
    for key in operations:
        print(key)
    operator = input("Select one operator ")
    num2 = float(input("Enter the second number: "))
    result = operations[operator](num1,num2)
    print(f"{num1} {operator} {num2} = {result}")
    return result


def n_calculation(previous_result):
    for key in operations:
        print(key)
    operator_n = input("Select one operator: ")
    num = float(input("Enter the next number: "))
    result_n = operations[operator_n](previous_result,num)
    print(f"{previous_result} {operator_n} {num} = {result_n}")
    return result_n

print("welcome to the calculator")
print("""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")

previous_result = first_calculation()
while True:
    new_operation = input("Type Y if you want to continue with the calculation or N if you want to perform a new calculation").upper()
    if new_operation == 'Y':
        previous_result = n_calculation(previous_result)
        continue
    else:
        print("\n" * 100)
        previous_result = first_calculation()
        continue
