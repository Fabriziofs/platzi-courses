# Clase 3: **Tipos de datos abstractos y clases, instancias.**

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        '''Recibe otra Persona y utiliza su nombre para saludarla.'''
        print(f'Hola {otra_persona.nombre}, me llamo {self.nombre}')


if __name__ == '__main__':
    Fabrizio = Persona('Fabrizio', 19)
    Ainara = Persona('Ainara', 19)

    Fabrizio.saluda(Ainara)
