# Clase 13: **Búsqueda lineal.**
import random


def busqueda_lineal(lista, objetivo):
    match = False
    contador = 0

    for elemento in lista:  # O(n)
        contador += 1
        if elemento == objetivo:
            # Se cambia el valor de match si se encuentra el objetivo.
            match = True
            break

    return match, contador


if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño será la lista?: '))
    objetivo = int(input('Qué número quieres encontrar?: '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(encontrado)
    print(
        f'El elemento {objetivo} {"está" if encontrado[0] else "no está."} {"en la lista y ha tomado " + f"{encontrado[1]}" + " encontrar el número." if encontrado[0] else ""}')
    # if encontrado[0]:
    #    print(f'Ha tomado {encontrado[1]} encontrar el número.')
