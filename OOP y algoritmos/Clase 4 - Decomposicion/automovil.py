# Clase 4: **Decomposición.**
from motor import Motor


class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)

    def acelerar(self, velocidad='despacio'):
        if velocidad == 'rapida':
            self._motor.inyectar(10)
        else:
            self._motor.inyectar(3)

        self._estado = 'en_movimiento'


if __name__ == '__main__':
    coche_1 = Automovil('Astra', 'Opel', 'Gris')
# El programa en si no hace nada es solo para demostrar
# como decomponer un problema en partes mas pequenias.
