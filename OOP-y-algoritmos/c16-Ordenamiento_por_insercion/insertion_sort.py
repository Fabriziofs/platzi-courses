# Clase 16: **Ordenamiento por inserción.**
import random


def ordenamiento_por_insercion1(lista):
    n = len(lista)
    sublista_ordenada = []  # Sublista Ordenada.
    sublista_ordenada.append(lista[0])

    for i in range(n - 1):
        valor_actual = lista[i + 1]

        if valor_actual < lista[i]:
            valor_actual = lista[i]
            lista[i] = valor_actual

    return lista


def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual


if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño quieres la lista?: '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(f'lista desordenada: {lista}')

    ordenamiento_por_insercion(lista)
    print(lista)
    #lista_ordenada =  ordenamiento_por_insercion(lista)
    #print(f'lista ordenada: {lista_ordenada}')
