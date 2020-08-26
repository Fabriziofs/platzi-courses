# Clase 14: **Factorial de un numero con recursion**

def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


if __name__ == '__main__':
    number = int(
        input('Ingresa el número del que deseas saber el factorial: '))
    result = factorial(number)
    print(result)
    factorial(number)
