# 제목: 재귀 함수를 이용한 깊이 우선 탐색(DFS) 구현

# 깊이 우선 탐색(DFS, Depth-First Search)은 그래프 탐색의 기본 중 하나예요.
# 이름처럼 '깊이'를 우선으로 해서, 한 방향으로 갈 수 있을 때까지 계속 가다가
# 더 이상 갈 곳이 없으면 뒤로 돌아와 다른 길을 찾아보는 방식이죠.
# 재귀 함수를 사용하면 코드를 아주 간결하게 구현할 수 있습니다.

# 탐색에 사용할 그래프 (인접 리스트)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

# 방문한 노드를 기록하기 위한 집합(set)
visited = set()

def dfs_recursive(node):
    """
    재귀를 이용해 DFS 방식으로 그래프를 탐색합니다.
    """
    # 현재 노드가 아직 방문하지 않은 곳이라면
    if node not in visited:
        # 방문했다고 기록하고, 노드 이름을 출력합니다.
        print(f"방문: {node}")
        visited.add(node)
        
        # 현재 노드와 연결된 다른 노드들을 하나씩 확인하면서
        for neighbor in graph[node]:
            # 아직 방문하지 않은 노드가 있다면, 그 노드로 다시 dfs 함수를 호출합니다.
            dfs_recursive(neighbor)

if __name__ == '__main__':
    print("재귀 DFS 탐색 시작:")
    # 'A' 노드부터 탐색을 시작해볼게요.
    dfs_recursive('A')