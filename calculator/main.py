# Day 10 -> Function with Outputs
# Calculator

from art import logo

print(logo)


def sum(first, second):
    return first + second


def sub(first, second):
    return first - second


def divide(first, second):
    return first / second


def mult(first, second):
    return first * second


operations = {
    "+": sum,
    "-": sub,
    "*": mult,
    "/": divide
}

loop = 'y'

while loop != 'n':
    first = float(input("What's the first number? "))

    for value in operations:
        print(value)

    operation = input("What's the operation? ")
    second = float(input("What's the second number? "))

    result = operations[operation](first, second)

    print(f"{first} {operation} {second} = {result}")

    loop = input("Type 'y' to start a new operation. Type 'n' to exit: ")
