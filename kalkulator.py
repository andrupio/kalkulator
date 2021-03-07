import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def check1(num1):
    try:
        float(num1)
    except ValueError:
        return False
    return True

def check2(num2):
    try:
        float(num2)
    except ValueError:
        return False
    return True

def calc(choice, num1, num2):
    if choice == '1':
        result = num1 + num2
        logging.info (f" Dodaję {num1} i {num2}")
        return result
    elif choice == '2':
        result = num1 - num2
        logging.info (f" Odejmuję {num2} od {num1}")
        return result      
    elif choice == '3':
        result = num1 * num2
        logging.info (f" Mnożę {num1} przez {num2}")
        return result
    elif choice == '4':
        if num2 == 0:
            print("Nie wolno dzielić przez 0")
            exit(1)
        result = num1 / num2
        logging.info (f" Dzielę {num1} pzez {num2}")
        return result

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    choice = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    
    if choice not in {'1', '2', '3', '4'}:
        print("Zły wybór")
        exit(1)
    
    num1 = input("Podaj składnik 1. ")
    if check1(num1) == True:
        num1 = float(num1)
    else:
        print("Podana wartość nie jest liczbą")
        exit(1)
    
    num2 = input("Podaj składnik 2. ")
    if check2(num2) == True:
        num2 = float(num2)
    else:
        print("Podana wartość nie jest liczbą")
        exit(1)
    
    result = calc(choice, num1, num2)
    print("Wynik to:\n", result)


