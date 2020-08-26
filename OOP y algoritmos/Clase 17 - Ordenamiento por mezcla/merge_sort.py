# Clase 17: **Ordenamiento por mezcla.**
import random


def ordenamiento_por_mezcla(lista):

    if len(lista) > 1:  # Se dividiran las listas que entren más grandes que 1.
        medio = len(lista) // 2
        izquierda = lista[:medio]  # Desde el principio hasta el medio.
        derecha = lista[medio:]  # Desde el medio hasta el final.
        print(lista)
        print(f'{izquierda}{"*" * 3}{derecha}')

        # Llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # Iteradores para recorrer las 2 sublistas.
        i = 0
        j = 0
        # Iterador para la lista principal.
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('*' * 40)
    print('\tfuerda del if')


if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño quieres la lista?: '))
    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    lista_ordenada = ordenamiento_por_mezcla(lista)
    # print(lista_ordenada)
