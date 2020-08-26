# Clase 15: **Ordenamiento de burbuja.**
import random


def ordenamiento_de_burbuja(lista):
    n = len(lista)  # Almacena el tamaño de la lista.

    for i in range(n):  # Big-O => O(n**2)
        print(lista)
        # Se itera hasta una posición menos que la anterior.
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Swapping

    return lista


if __name__ == '__main__':

    tamano_lista = int(input('De que tamaño quieres la lista?: '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)
