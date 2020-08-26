from coordenada import Coordenada
from borracho import BorrachoTradicional


class Campo:
    def __init__(self):
        self.coordenadas_de_borrachos = {}

    def anadir_borracho(self, borracho, coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada

    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]


def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='Fabrizio')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias


def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(
            pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')


if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1_000, 10_000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)
