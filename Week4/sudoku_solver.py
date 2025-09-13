# 제목: 스도쿠(Sudoku) 퍼즐 풀이 (백트래킹)

# 스도쿠는 9x9 격자의 빈칸에 1부터 9까지의 숫자를 채워 넣는 퍼즐입니다.
# 규칙은 간단하죠. 각 가로줄, 세로줄, 그리고 3x3 작은 상자 안에
# 숫자가 한 번씩만 나타나야 합니다.
# 이 문제 역시 백트래킹으로 풀 수 있습니다. 빈칸을 하나 찾고,
# 1부터 9까지의 숫자를 넣어본 뒤, 규칙에 맞으면 다음 빈칸으로 넘어가는 식이죠.
# 만약 막다른 길에 다다르면 이전의 선택을 취소하고 다른 숫자를 시도합니다.

def solve_sudoku(board):
    """스도쿠 퍼즐을 푸는 함수. 풀이가 가능하면 True, 아니면 False를 반환."""
    
    empty_cell = find_empty(board)
    # 빈칸이 없으면 퍼즐이 완성된 것이므로 True 반환
    if not empty_cell:
        return True
    else:
        row, col = empty_cell

    # 1부터 9까지의 숫자를 하나씩 시도해 봅니다.
    for num in range(1, 10):
        # 현재 위치에 숫자를 놓아도 규칙에 맞는지 확인
        if is_valid(board, num, (row, col)):
            # 규칙에 맞으면 숫자를 배치
            board[row][col] = num

            # 다음 빈칸을 채우기 위해 재귀적으로 함수 호출
            if solve_sudoku(board):
                return True # 최종적으로 풀리면 True 반환

            # 재귀 호출 결과가 False이면 (즉, 막다른 길이면)
            # 방금 놓았던 숫자를 다시 0으로 되돌립니다 (백트래킹).
            board[row][col] = 0

    # 1부터 9까지 모든 숫자를 시도했는데도 풀리지 않으면 False 반환
    return False

def is_valid(board, num, pos):
    """특정 위치에 숫자를 놓는 것이 유효한지 확인합니다."""
    row, col = pos
    
    # 1. 같은 행에 같은 숫자가 있는지 확인
    for i in range(len(board[0])):
        if board[row][i] == num and col != i:
            return False

    # 2. 같은 열에 같은 숫자가 있는지 확인
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    # 3. 3x3 상자 안에 같은 숫자가 있는지 확인
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(board):
    """빈칸(0)을 찾아 그 위치를 반환합니다."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # (행, 열)
    return None

def print_board(board):
    """스도쿠 보드를 예쁘게 출력합니다."""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(f"{board[i][j]} ", end="")
        print()

if __name__ == '__main__':
    # 0은 빈칸을 의미합니다.
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("풀기 전 스도쿠 보드:")
    print_board(sudoku_board)
    print("\n" + "="*23 + "\n")
    
    solve_sudoku(sudoku_board)
    
    print("풀이 후 스도쿠 보드:")
    print_board(sudoku_board)