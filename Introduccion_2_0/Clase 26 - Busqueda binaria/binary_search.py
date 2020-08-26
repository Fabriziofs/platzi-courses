# Clase 26: **Implementar busqueda binaria en Python**
import random


def number_finder(numbers_sort, number_input, low, high):

    mid = int((low + high) // 2)

    if low > high:

        return False

    if number_input == numbers_sort[mid]:

        return True

    elif number_input < numbers_sort[mid]:

        number_finder(numbers_sort, number_input, low, mid - 1)

    elif number_input > numbers_sort[mid]:

        number_finder(numbers_sort, number_input, mid + 1, high)


if __name__ == '__main__':

    number_input = int(input('Ingresa el número que quieres consultar: '))
    numbers = []

    while len(numbers) < 10:

        numbers.append(random.randint(0, 20))

    numbers_sort = sorted(numbers)
    result = number_finder(numbers_sort, number_input,
                           0, len(numbers_sort) - 1)

    if result is True:
        print(numbers_sort)
        print('El número SI está en la lista.')

    else:
        print(numbers_sort)
        print('El número NO está en la lista.')
