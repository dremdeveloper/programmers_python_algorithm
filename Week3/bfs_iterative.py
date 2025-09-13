# 제목: 큐(Queue)를 이용한 너비 우선 탐색(BFS) 구현

# 너비 우선 탐색(BFS, Breadth-First Search)은 DFS와 함께 그래프 탐색의 양대 산맥이죠.
# BFS는 시작 노드에서 가까운 노드들부터 차례대로, 즉 '넓게' 탐색하는 방식입니다.
# 최단 경로를 찾는 문제에 아주 효과적이에요.
# BFS는 '먼저 들어온 것이 먼저 나가는(FIFO)' 큐(Queue) 자료구조를 사용해서 구현합니다.

from collections import deque

def bfs_iterative(graph, start_node):
    """
    큐를 이용해 BFS 방식으로 그래프를 탐색합니다.
    """
    # 방문한 노드를 기록할 집합
    visited = set()
    
    # 탐색할 노드를 담을 큐
    # 파이썬에서는 collections.deque를 사용하면 효율적인 큐를 만들 수 있어요.
    queue = deque([start_node])
    
    # 시작 노드는 이미 방문 예정이므로 미리 기록합니다.
    visited.add(start_node)

    print("BFS 탐색 시작:")
    
    # 큐가 빌 때까지 계속 반복합니다.
    while queue:
        # 큐의 맨 앞에서 노드를 하나 꺼냅니다.
        node = queue.popleft()
        print(f"방문: {node}")
        
        # 꺼낸 노드의 이웃 노드들을 확인합니다.
        for neighbor in graph.get(node, []):
            # 아직 방문하지 않은 이웃이라면
            if neighbor not in visited:
                # 방문 기록을 남기고 큐에 추가합니다.
                visited.add(neighbor)
                queue.append(neighbor)

if __name__ == '__main__':
    # 탐색에 사용할 그래프 (인접 리스트)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # 'A' 노드부터 탐색을 시작합니다.
    bfs_iterative(graph, 'A')