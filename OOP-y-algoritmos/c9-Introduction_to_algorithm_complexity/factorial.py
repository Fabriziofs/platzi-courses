# Clase 9: **Introducción a la complejidad algorítmica.**
import time


def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)


if __name__ == '__main__':

    n = 500  # Cantidad de iteraciones o ciclos recursivos a aplicar

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)
