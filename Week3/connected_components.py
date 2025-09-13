# 제목: DFS를 이용한 연결 요소(Connected Components) 탐색

# '연결 요소'란 그래프에서 서로 연결된 노드들의 묶음(그룹)을 말해요.
# 예를 들어, 한 그래프 안에 서로 연결되지 않은 두 개의 독립적인 섬이 있다면,
# 연결 요소는 2개가 되는 거죠.
# 전체 노드를 순회하면서 아직 방문하지 않은 노드가 있다면,
# 새로운 연결 요소의 시작점으로 간주하고 탐색을 시작하면 개수를 셀 수 있습니다.

def find_connected_components(graph):
    """
    그래프의 모든 연결 요소의 개수를 찾습니다.
    """
    visited = set()
    count = 0

    def dfs(node):
        """특정 노드에서 시작하여 연결된 모든 노드를 방문 처리하는 함수"""
        stack = [node]
        visited.add(node)
        while stack:
            curr = stack.pop()
            for neighbor in graph.get(curr, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
    
    # 그래프의 모든 노드를 하나씩 확인합니다.
    for node in graph:
        # 만약 아직 방문하지 않은 노드라면,
        if node not in visited:
            # 새로운 연결 요소를 발견한 것이므로 카운트를 1 증가시키고,
            count += 1
            # 이 노드와 연결된 모든 노드를 찾아 방문 처리합니다.
            dfs(node)
            
    return count

if __name__ == '__main__':
    # 두 개의 독립된 컴포넌트를 가진 그래프
    graph = {
        'A': ['B'],
        'B': ['A', 'C'],
        'C': ['B'],
        'D': ['E'],
        'E': ['D'],
        'F': []
    }
    
    num_components = find_connected_components(graph)
    print(f"이 그래프의 연결 요소 개수는 {num_components}개 입니다.")