# 제목: 2차원 격자(Grid)에서 단어 찾기 (Word Search) (백트래킹/DFS)

# 2차원 문자 격자가 있고, 특정 단어가 주어졌을 때,
# 이 단어가 격자 안에서 상하좌우로 인접한 문자들을 연속으로 이어 만들 수 있는지
# 확인하는 문제입니다. 한 번 사용한 칸의 문자는 다시 사용할 수 없습니다.
# 이 문제는 특정 칸에서 탐색을 시작하여 단어의 다음 글자를 찾아나서는
# 깊이 우선 탐색(DFS)과 백트래킹의 조합으로 해결할 수 있습니다.

def word_search(board, word):
    """2D 격자에서 단어의 존재 여부를 확인합니다."""
    
    rows = len(board)
    cols = len(board[0])

    def dfs(r, c, k):
        """(r, c)에서 시작하여 word[k:]를 찾습니다."""
        # 범위를 벗어나거나 현재 칸의 문자가 찾는 문자와 다르면 실패
        if not (0 <= r < rows and 0 <= c < cols and board[r][c] == word[k]):
            return False
            
        # 단어의 마지막 글자까지 찾았다면 성공
        if k == len(word) - 1:
            return True
            
        # 현재 위치를 다시 방문하지 않도록 임시로 다른 문자로 변경
        original_char = board[r][c]
        board[r][c] = '#'
        
        # 상하좌우 네 방향으로 다음 글자 탐색
        found = (dfs(r + 1, c, k + 1) or
                 dfs(r - 1, c, k + 1) or
                 dfs(r, c + 1, k + 1) or
                 dfs(r, c - 1, k + 1))
        
        # 탐색이 끝났으면 원래 문자로 복원 (백트래킹)
        board[r][c] = original_char
        
        return found

    # 격자의 모든 칸에서 탐색을 시작해 봅니다.
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
                
    return False

if __name__ == '__main__':
    grid = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    
    word1 = "ABCCED"
    word2 = "SEE"
    word3 = "ABCB" # B를 중복해서 사용할 수 없으므로 False
    
    print(f"격자에서 단어 '{word1}'을(를) 찾을 수 있나요? -> {word_search(grid, word1)}")
    print(f"격자에서 단어 '{word2}'을(를) 찾을 수 있나요? -> {word_search(grid, word2)}")
    print(f"격자에서 단어 '{word3}'을(를) 찾을 수 있나요? -> {word_search(grid, word3)}")