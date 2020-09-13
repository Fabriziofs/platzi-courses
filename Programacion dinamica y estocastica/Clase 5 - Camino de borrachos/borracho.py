# Clase 5: **Camino de Borrachos**
import random


class Borracho:
    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho):
    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        # Elige de manera aleatoria un elemento de la lista.
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])


class BorrachoCircular(Borracho):
    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        # arriba    abajo   derecha izquierda
        return random.choice([(0, 2), (0, -1), (1, 0), (-2, 0)])
