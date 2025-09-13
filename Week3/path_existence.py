# 제목: DFS/BFS를 이용한 특정 노드 경로 존재 여부 확인

# 그래프 탐색의 대표적인 활용 사례! 바로 두 노드 사이에 경로가 있는지 확인하는 문제입니다.
# 시작 노드에서부터 탐색을 시작해서 목표 노드에 도달할 수 있다면 경로가 존재하는 것이죠.
# DFS, BFS 둘 다 사용할 수 있지만, 여기서는 DFS를 이용해서 간단하게 구현해 볼게요.

def has_path_dfs(graph, start, end):
    """
    DFS를 이용해 start 노드에서 end 노드로 가는 경로가 있는지 확인합니다.
    """
    # 방문한 노드를 기록할 집합
    visited = set()
    # 탐색할 노드를 담을 스택
    stack = [start]

    while stack:
        node = stack.pop()
        
        # 만약 현재 노드가 목표 노드라면, 경로를 찾은 것이니 True를 반환합니다.
        if node == end:
            return True
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    # 스택이 모두 비워질 때까지 목표 노드를 찾지 못했다면 경로가 없는 것입니다.
    return False

if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': [],
        'D': ['E'],
        'E': [],
        'F': ['G'] # 다른 연결 요소
    }

    start_node_1 = 'A'
    end_node_1 = 'E'
    print(f"{start_node_1}에서 {end_node_1}까지 경로가 있나요? -> {has_path_dfs(graph, start_node_1, end_node_1)}")

    start_node_2 = 'A'
    end_node_2 = 'G'
    print(f"{start_node_2}에서 {end_node_2}까지 경로가 있나요? -> {has_path_dfs(graph, start_node_2, end_node_2)}")