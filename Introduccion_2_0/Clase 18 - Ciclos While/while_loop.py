# Clase 18: **Ciclos en Python con While**
import random


def run():
    number_found = False
    random_number = random.randint(0, 100)

    while not number_found:
        number = int(input('Ingresa un número: '))

        if number == random_number:

            print(
                f'¡FELICIDADES! has descubierto que {random_number} es el número aleatorio.')
            number_found = True

        elif number < random_number:

            temperature = random_number - number

            if temperature <= 10:

                warm = ' Pero..estás muuuuuuuuuuy cerca.'

                print(
                    f'El número {number} es MENOR que el número aleatorio.' + warm)

            elif temperature <= 50:

                lukewarm = ' Pero..estás a menos de 50.'

                print(
                    f'El número {number} es MENOR que el número aleatorio.' + lukewarm)

            elif temperature <= 100:

                cold = ' Y para ser sincero, estás muy lejos del número..más de 50 números lejos..'

                print(
                    f'El número {number} es MENOR que el número aleatorio.' + cold)

        elif number > random_number:

            print(f'El número {number} es MAYOR que el número aleatorio.')


if __name__ == '__main__':
    run()
