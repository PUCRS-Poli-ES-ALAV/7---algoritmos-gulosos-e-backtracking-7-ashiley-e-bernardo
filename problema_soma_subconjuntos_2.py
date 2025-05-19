'''
# Problema da Soma dos Subconjuntos

O problema da soma dos subconjuntos é um problema de ciência da computação que 
consiste em verificar se, dado um conjunto de inteiros, existe um subconjunto não-vazio cuja soma é zero. 

Por exemplo, no conjunto {−7, −3, −2, 5, 8}, a resposta é sim, pois o subconjunto {−3, −2, 5} resulta em uma soma de zero. 

Faça um método que recebe um conjunto de inteiros e retorna um subconjunto cuja soma seja zero;
Altere o método para que retorne todos subconjuntos cuja soma seja zero;
Analise a complexidade de ambas as soluções.
'''
def find_subset_with_sum_zero(set):
    stack = []
    marked = [False] * len(set)

    for i in set:
        stack.append((i, set[i]))
        marked[i] = True
        backtrack(stack, set, marked)
        if sum(y for x, y in stack) == 0:
            return stack
        stack.pop()
        marked[i] = False
    return None

def backtrack(stack, set, marked):
    for i in set:
        if not marked[i]:
            stack.append((i, set[i]))
            marked[i] = True
            backtrack(stack, set, marked)
            if sum(y for x, y in stack) == 0:
                return stack
            stack.pop()
            marked[i] = False

    return None    

if __name__ == "__main__":
    set = [1, 2, -3, 4, -1, 5]
    result = find_subset_with_sum_zero(set)
    print("Result:", result)