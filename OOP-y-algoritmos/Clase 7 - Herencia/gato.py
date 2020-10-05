# Clase 7: **Herencia**

from Animal import Animal


class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def maullar(self):
        print(f'{self.nombre} esta maullando.')


if __name__ == '__main__':
    animal = Animal('Fabrizio', 19)
    gata = Gato('Nara', 3)

    print(animal.nombre)
    gata.comer()
    gata.andar()
