"""
## Problema do Troco

Suponha que tenhamos disponíveis moedas com certos valores (por exemplo, de 100, 25, 10, 5 e 1). O problema do
troco consiste criar um algoritmo que para conseguir obter um determinado valor com o menor número de moedas ´
possível.
Por exemplo, para “dar um troco” de R$2,89, a melhor solução, isto é, o menor número de 
moedas possível para obter o valor consiste em 10 moedas: 2 de valor 100, 3 de valor 25, 1 de valor 10
e 4 de valor 1.

1) **Objetivo:** contrua um algorítmo que recebe a lista das moedas disponíveis e um valor, e retorna uma lista com a menor
quantidade de moedas para este troco;
  * Defina uma assinatura adequada para este método;
  * Utiliza uma abordagem gulosa (se puder);
  * Contabilize e exiba o número de iterações para cada caso de teste;
  * O exercício pode ser feito em grupos de um, dois ou três elementos.
"""


def main():
    # Example 1
    coins = [100, 25, 10, 5, 1]
    value = 289
    result = get_change(coins, value)
    print(f"Change for {value} cents: {result}")
    print(f"Total coins used: {len(result)}")

    # Example 2
    coins = [50, 20, 10, 5, 2, 1]
    value = 123
    result = get_change(coins, value)
    print(f"Change for {value} cents: {result}")
    print(f"Total coins used: {len(result)}")

    # Example 3
    coins = [200, 100, 50, 25, 10, 5, 1]
    value = 378
    result = get_change(coins, value)
    print(f"Change for {value} cents: {result}")
    print(f"Total coins used: {len(result)}")

    # Example 4
    coins = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    value = 999
    result = get_change(coins, value)
    print(f"Change for {value} cents: {result}")
    print(f"Total coins used: {len(result)}")


def get_change(coins, value):
    original_value = value
    print(f"Coins available: {coins}")
    print(f"Value to change: {value} cents")
    result = []
    iterations = 0

    # Pensei em duas aborgagens:
    # 1) Ordenar a lista de moedas, usar cada moeda a maior quantidade de vezes possível e depois passar para a próxima moeda
    value = original_value
    sorted_coins, sort_iterations = insertion_sort(coins, True) # Timsort, que o Python usa, usa Insertion Sort para listas até 32 elementos
    iterations += sort_iterations

    for coin in sorted_coins:
        while value >= coin:
            result.append(coin)
            value -= coin
            iterations += 1

    print(f"Total iterations (1): {iterations}")
    print(f"Result (1): {result}")
    result = [] # Reset
    iterations = 0 # Reset

    # 2) Não ordernar a lista, mas pegar a maior moeda possível e usar ela o maior número de vezes possível, depois passar para a próxima moeda
    value = original_value
    while value > 0:
        max_coin = max([coin for coin in coins if coin <= value])
        iterations += len(coins) # Aproximacao

        while value >= max_coin:
            result.append(max_coin)
            value -= max_coin
            iterations += 1

    print(f"Total iterations (2): {iterations}")
    print(f"Result (2): {result}")
    return result


def insertion_sort(arr, reverse=False):
    iterations = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((arr[j] < key) if reverse else (arr[j] > key)):
            arr[j + 1] = arr[j]
            j -= 1
            iterations += 1
        arr[j + 1] = key
    return arr, iterations


if __name__ == "__main__":
    main()
