# 제목: BFS를 이용한 최단 경로(거리) 탐색

# BFS의 가장 강력한 특징 중 하나는 최단 경로를 찾는 데 사용될 수 있다는 점입니다.
# 시작점에서부터 거리가 1인 곳, 2인 곳, ... 순서로 넓게 탐색하기 때문에,
# 목표 지점을 발견했을 때 그 경로가 바로 최단 경로가 되는 원리죠.
# (단, 모든 엣지의 가중치가 1로 같을 때만 해당돼요!)

from collections import deque

def bfs_shortest_path(graph, start, end):
    """
    BFS를 이용해 start 노드에서 end 노드까지의 최단 거리를 찾습니다.
    """
    # 큐에는 (노드, 현재까지의 거리)를 튜플 형태로 저장합니다.
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        node, distance = queue.popleft()

        # 목표 노드를 찾았다면, 현재까지의 거리를 반환합니다.
        if node == end:
            return distance

        # 연결된 이웃 노드들을 탐색합니다.
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                # 다음 노드로 갈 때는 거리를 1 증가시켜 큐에 넣습니다.
                queue.append((neighbor, distance + 1))

    # 큐가 모두 비워질 때까지 목표를 찾지 못했다면 경로가 없는 것입니다.
    return -1

if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E', 'G'],
        'G': ['F']
    }

    start_node = 'A'
    end_node = 'G'
    
    distance = bfs_shortest_path(graph, start_node, end_node)
    
    if distance != -1:
        print(f"{start_node}에서 {end_node}까지의 최단 거리는 {distance}입니다.")
    else:
        print(f"{start_node}에서 {end_node}까지 가는 경로가 없습니다.")