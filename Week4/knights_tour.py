# 제목: 체스 나이트의 경로(Knight's Tour) 문제 (백트래킹)

# '나이트의 경로' 문제는 체스판의 나이트(Knight)가 특정 위치에서 출발하여
# 보드의 모든 칸을 정확히 한 번씩만 방문하는 경로를 찾는 고전적인 문제입니다.
# 나이트는 L자 형태로만 움직일 수 있죠. (가로 2칸, 세로 1칸 또는 가로 1칸, 세로 2칸)
# 이 문제는 가능한 모든 경로를 탐색해야 하므로 백트래킹의 좋은 예시가 됩니다.
# 하지만 경우의 수가 매우 많아 N이 커지면 시간이 오래 걸릴 수 있습니다.

def solve_knights_tour(n):
    """N x N 체스판에서 나이트의 경로를 찾습니다."""
    
    # 체스판을 -1로 초기화 (-1은 아직 방문하지 않았음을 의미)
    board = [[-1 for _ in range(n)] for _ in range(n)]
    
    # 나이트가 이동할 수 있는 8가지 방향
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]
             
    # 시작 위치 (0, 0)에 0번째 방문 표시
    start_x, start_y = 0, 0
    board[start_x][start_y] = 0

    def backtrack(curr_x, curr_y, move_count):
        """백트래킹으로 경로를 탐색합니다."""
        # 모든 칸을 방문했다면 성공
        if move_count == n * n:
            return True

        # 8가지 방향으로 이동 시도
        for move_x, move_y in moves:
            next_x, next_y = curr_x + move_x, curr_y + move_y
            
            # 다음 위치가 체스판 범위 안에 있고 아직 방문하지 않았다면
            if 0 <= next_x < n and 0 <= next_y < n and board[next_x][next_y] == -1:
                # 다음 위치에 방문 순서 기록
                board[next_x][next_y] = move_count
                # 재귀적으로 다음 경로 탐색
                if backtrack(next_x, next_y, move_count + 1):
                    return True
                # 경로 탐색에 실패했다면, 선택을 되돌립니다 (백트래킹)
                board[next_x][next_y] = -1
                
        return False

    if backtrack(start_x, start_y, 1):
        print(f"{n}x{n} 체스판에서 나이트의 경로를 찾았습니다:")
        for row in board:
            # 각 숫자를 보기 좋게 정렬해서 출력
            print(" ".join(f"{num:2d}" for num in row))
    else:
        print(f"{n}x{n} 체스판에서 나이트의 경로를 찾을 수 없습니다.")

if __name__ == '__main__':
    # N=5 정도는 금방 풀리지만, N이 6 이상이 되면 매우 오래 걸릴 수 있습니다.
    solve_knights_tour(5)