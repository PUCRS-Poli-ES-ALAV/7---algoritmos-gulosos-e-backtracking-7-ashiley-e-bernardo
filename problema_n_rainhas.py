'''
# Problema das n-rainhas

## O problema

O problema das N-rainhas consiste em encontrar uma combinação possível de N

rainhas num tabuleiro de dimensão N por N tal que nenhuma das rainhas ataque
qualquer outra. Duas rainhas atacam-se uma à outra quando estão na mesma linha, 
na mesma coluna ou na mesma diagonal do tabuleiro. Na figura que se segue pode 
ver-se as posições atacadas por uma rainha colocada num tabuleiro de dimensão 7 
por 7 e ao lado uma possível solução para esse mesmo tabuleiro.

![N_Rainhas](https://github.com/PUCRS-Poli-ES-ALAV/7-algoritmos-gulosos-e-backtracking/blob/main/nrainhas1.bmp)

1. Desenvolver uma aplicação que resolva o problema das n-rainhas, 
encontrando uma solução válida para o problema. Como entrada, o programa
 recebe um valor para n >= 2, e retorna a disposição das rainhas no tabuleiro. 
 Utilize uma estratégia de backtracking.

1. Ajuste o algoritmo anterior, para que retorne todas as soluções possíveis.
'''
import random

def solve_problem(n):
    mat = [[0 for _ in range(n)] for _ in range(n)]
    result = {}
    rainhas = 0

    while rainhas < n:
        if try_put_queen(mat, n):
            rainhas += 1

        for row in mat:
            print(' '.join(str(cell) for cell in row))

        print('------------------')

def try_put_queen(mat, n):
    random_linha = random.randint(0, n-1)
    random_coluna = random.randint(0, n-1)

    if mat[random_linha][random_coluna] == 0:
        # Verifica Horizontal
        for i in range(0, n - 1):
            if mat[random_linha][i] == 1:
                return False
            
        # Verifica Vertical
        for i in range(0, n - 1):
            if mat[i][random_coluna] == 1:
                return False
            
        # Verifica Diagonal Principal
        i = random_linha
        j = random_coluna
        while ((i != n) and (j != -1)):
            if mat[i][j] == 1:
                return False
            i += 1
            j -= 1

        i = random_linha
        j = random_coluna
        while ((i != -1) and (j != n)):
            if mat[i][j] == 1:
                return False
            i -= 1
            j += 1
                       

        # Verifica Diagonal Secundária
        
        


        mat[random_linha][random_coluna] = 1
        return True


def main():
    print('Problema das N-Rainhas')
    solve_problem(3)

if __name__ == '__main__':
    main()
