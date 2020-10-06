# Clase 8: **Polimorfismo.**
from ciclista import Ciclista
from persona import Persona


def main():
    persona = Persona('Fabrizio')
    persona.avanza()

    ciclista = Ciclista('Ainara')
    ciclista.avanza()


if __name__ == '__main__':
    main()
