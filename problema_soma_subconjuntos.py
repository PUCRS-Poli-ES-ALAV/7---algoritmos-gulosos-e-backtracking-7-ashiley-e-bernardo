# Problema da Soma dos Subconjuntos

# O problema da soma dos subconjuntos é um problema de ciência da computação que 
# consiste em verificar se, dado um conjunto de inteiros, existe um subconjunto não-vazio cuja soma é zero. 

# Por exemplo, no conjunto {−7, −3, −2, 5, 8}, a resposta é sim, pois o subconjunto {−3, −2, 5} resulta em uma soma de zero. 

# Faça um método que recebe um conjunto de inteiros e retorna um subconjunto cuja soma seja zero;
# Altere o método para que retorne todos subconjuntos cuja soma seja zero;
# Analise a complexidade de ambas as soluções.

def gerar_subconjuntos(lista):
    subconjuntos = []
    n = len(lista)

    for i in range(1, 2 ** n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(lista[j])
        subconjuntos.append(subset)
    return subconjuntos


def encontrar_subconjunto_soma_zero(subconjuntos, i, n):
    if sum(subconjuntos[i]) == 0:
        return subconjuntos[i]
    if i == n:
        return None

    return encontrar_subconjunto_soma_zero(subconjuntos, i+1, n)


if __name__ == "__main__":
    nums = [3, -3]
    subconjuntos = gerar_subconjuntos(nums)
    print(subconjuntos)
    sub = encontrar_subconjunto_soma_zero(subconjuntos, 0, len(subconjuntos) - 1)
    print(sub)
