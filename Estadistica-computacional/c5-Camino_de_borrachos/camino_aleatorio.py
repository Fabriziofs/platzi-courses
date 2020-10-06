from coordenada import Coordenada
from borracho import Borracho, BorrachoTradicional, BorrachoCircular
from campo import Campo
from bokeh.plotting import figure, show


def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, borracho):
    borracho = borracho(nombre='Fabrizio')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias


def ejecutar_caminata(campo, borracho, distancia_de_caminata):
    x_arr = []
    y_arr = []

    x_arr.append(campo.obtener_coordenada(borracho).x)
    y_arr.append(campo.obtener_coordenada(borracho).y)

    for _ in range(distancia_de_caminata):
        campo.mover_borracho(borracho)
        x_arr.append(campo.obtener_coordenada(borracho).x)
        y_arr.append(campo.obtener_coordenada(borracho).y)

    graficar(x_arr, y_arr)


def graficar(x, y):
    grafica = figure(title='Camino aleatorio')
    grafica.line(x, y)

    show(grafica)


def main(distancia_de_caminata, numero_de_intentos, borracho):
    campo = Campo()
    origen = Coordenada(0, 0)
    borracho = borracho('Fabrizio')
    campo.anadir_borracho(borracho, origen)

    ejecutar_caminata(campo, borracho, distancia_de_caminata)


if __name__ == '__main__':
    distancia_de_caminata = 100_000
    numero_de_intentos = 100

    main(distancia_de_caminata, numero_de_intentos, BorrachoCircular)
