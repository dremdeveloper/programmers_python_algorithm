# 제목: BFS (너비 우선 탐색) 큐 기본 템플릿 (최단거리 찾기)
from collections import deque

# BFS는 시작 노드에서 가까운 노드부터 차례대로 탐색하는 알고리즘입니다.
# 큐(Queue)를 사용하며, 가중치가 없는 그래프에서 최단 경로를 찾는 데 사용됩니다.

def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (인접 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

# 정의된 BFS 함수 호출
print("BFS 방문 순서:")
bfs(graph, 1, visited)