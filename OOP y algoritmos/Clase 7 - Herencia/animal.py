# Clase 7: **Herencia**

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        #self.disponibilidad = True

    def andar(self):
        print('Andando')

    def comer(self):
        print('Comiendo')
