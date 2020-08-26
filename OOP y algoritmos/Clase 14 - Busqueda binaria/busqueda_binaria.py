# Clase 14: **Búsqueda binaria**
import random


def busqueda_binaria(lista, objetivo, comienzo, final, contador):
    print(f'Buscando entre {lista[comienzo]} y {lista[final - 1]}')
    contador += 1

    if comienzo > final:
        return False

    medio = (comienzo + final) // 2
    print(lista[medio])

    if lista[medio] == objetivo:
        print(
            f'Ha tomado {contador} {"paso" if contador == 1 else "pasos"} encontrar el número {objetivo}.')
        return True

    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, objetivo, comienzo, medio - 1, contador)

    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, objetivo, medio + 1, final, contador)


if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño será la lista?: '))
    objetivo = int(input('Qué número quieres encontrar?: '))
    contador = 0
    lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])

    encontrado = busqueda_binaria(lista, objetivo, 0, len(lista), contador)

    print(lista)
    print(
        f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista.')
