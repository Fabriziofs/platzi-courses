# Clase 11: **Calcular si es un numero primo**
import random


def run():
    number = int(input('Escribe el número: '))

    prime_verificator(number)
    result = prime_verificator(number)

    if result is True:
        print('Es primo.')
    else:
        print('NO es primo.')

# True = Es primo | False = NO es primo


def prime_verificator(number):

    if number > 1:
        if number % 2 == 0 and number != 2:
            return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    run()
