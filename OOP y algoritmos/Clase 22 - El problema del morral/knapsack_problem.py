# Clase 22: **El problema del morral.(0-1 knapsack)**

def morral(tamano_morral, pesos, valores, n):
    print(tamano_morral)

    if n == 0 or tamano_morral == 0:
        return 0

    if pesos[n - 1] > tamano_morral:
        return 0

    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
               morral(tamano_morral, pesos, valores, n - 1))


if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 30
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)
