import logging
logging.basicConfig(level=logging.DEBUG)

def add(a, b, *args):
    return a + b + sum(args)

def sub(a, b):
    return a - b

def multiply(a, b, *args):
    z = 1
    for c in args:
        z = z * c
    return a * b * z

def divide(a, b):
    return a / b

def get_data():
    op = input('Jaką operację chcesz wykonać: +, -, *, / ')
    a = int(input('podaj a: '))
    b = int(input('podaj b: '))
    args = []
    if op == "+":
        while True:
            x = input("Podaj kolejną liczbę lub q by zakończyć: ")
            if x == 'q':
                break
            args.append(int(x))
    elif op == "-":
        pass
    elif op == "*":
        while True:
            x = input("Podaj kolejną liczbę lub q by zakończyć: ")
            if x == 'q':
                break
            args.append(int(x))
    elif op == "/":
        pass
    else:
        print("Zły wybór")
        exit(1)
    return op, a, b, args

op, a, b, args = get_data()

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}

result = operations[op](a, b, *args)
logging.info(f" Wynik = {result}")
