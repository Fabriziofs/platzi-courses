# 52 - Desafío 1: **Suma recursiva**


def suma_r(num):
    if num == 1:
        return 1

    return num + suma_r(num - 1)


if __name__ == '__main__':

    print('Programa que suma recursivamente\nhasta 972(en google Colab)')
    print('-' * 32)

    num = int(input('Ingresa el número a sumar recursivamente\n>>>'))

    resultado = suma_r(num)
    print(f'La suma recursiva de {num} es igual a {resultado}')
