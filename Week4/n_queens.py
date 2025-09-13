# 제목: N-Queens 문제 풀이 (백트래킹)

# 안녕하세요! 오늘은 백트래킹(Backtracking) 알고리즘의 대표적인 예제,
# N-Queens 문제를 함께 풀어보겠습니다.
# 이 문제는 N x N 크기의 체스판에 N개의 퀸을 서로 공격할 수 없도록
# 배치하는 모든 경우의 수를 찾는 문제입니다.
# 백트래킹은 가능성 있는 모든 해결책을 탐색하다가,
# 더 이상 진행이 불가능하다고 판단되면 이전 상태로 돌아가 다른 선택지를 찾아보는
# '퇴각 검색' 기법입니다. 마치 막다른 길에 다다르면 왔던 길을 되돌아가
# 다른 길을 찾아보는 것과 같죠.

def solve_n_queens(n):
    """N-Queens 문제의 모든 해답을 찾아 출력합니다."""
    
    # 각 행에 퀸이 어느 열에 위치하는지를 저장하는 리스트
    # 예: board[0] = 1 은 0행 1열에 퀸이 있다는 의미
    board = [-1] * n
    solutions = []

    def is_safe(row, col):
        """(row, col) 위치에 퀸을 놓아도 안전한지 확인합니다."""
        for i in range(row):
            # 같은 열에 다른 퀸이 있는지 확인
            if board[i] == col:
                return False
            # 대각선상에 다른 퀸이 있는지 확인
            # (행의 차이와 열의 차이가 같으면 대각선에 위치함)
            if abs(row - i) == abs(col - board[i]):
                return False
        return True

    def backtrack(row):
        """백트래킹을 이용해 퀸을 배치합니다."""
        # 모든 행에 퀸을 성공적으로 배치했다면 해답에 추가
        if row == n:
            solutions.append(list(board))
            return

        # 현재 행(row)의 모든 열(col)에 퀸을 놓아보는 시도를 합니다.
        for col in range(n):
            # 현재 위치가 안전하다면
            if is_safe(row, col):
                # 퀸을 배치하고
                board[row] = col
                # 다음 행으로 넘어갑니다.
                backtrack(row + 1)
                # 다음 행에서 해답을 찾지 못하고 돌아왔다면,
                # 현재 위치의 퀸을 치우고 다른 선택을 시도합니다. (이 부분이 백트래킹)
                # board[row] = -1 (이 줄은 없어도 다음 루프에서 덮어쓰여서 괜찮습니다)

    backtrack(0)  # 0번 행부터 시작
    
    # 찾은 해답들을 예쁘게 출력
    print(f"{n}x{n} 체스판의 N-Queens 문제 ({len(solutions)}개의 해답 발견):")
    for sol in solutions:
        for row in range(n):
            line = ""
            for col in range(n):
                line += "Q " if sol[row] == col else ". "
            print(line)
        print("-" * (2 * n))

if __name__ == '__main__':
    # 4x4 체스판 문제 풀이
    solve_n_queens(4)