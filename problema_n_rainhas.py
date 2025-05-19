global iterations

def is_safe(board, row, col, n):
    global iterations
    # Verifica coluna
    for i in range(row):
        iterations += 1
        if board[i][col] == 1:
            return False

    # Verifica diagonal principal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        iterations += 1
        if board[i][j] == 1:
            return False

    # Verifica diagonal secundária
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        iterations += 1
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_rec(board, row, n):
    global iterations
    iterations += 1
    # Se todas as rainhas foram colocadas, você consegue chegar na última linha
    if row == n:
        return True
    for col in range(n):
        iterations += 1
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens_rec(board, row+1, n):
                return True
            board[row][col] = 0
    return False

def solve_n_queens(n):
    # Cria uma tabela toda zerada
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens_rec(board, 0, n):
        for row in board:
            print(' '.join(str(cell) for cell in row))
    else:
        print("Sem solução.")

def main():
    global iterations
    iterations = 0
    print('Problema das N-Rainhas')
    n = 4
    solve_n_queens(n)
    print(f"Total de iterações: {iterations}")

if __name__ == '__main__':
    main()
