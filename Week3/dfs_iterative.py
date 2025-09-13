# 제목: 스택(Stack)을 이용한 반복문 기반의 깊이 우선 탐색(DFS)

# 재귀 함수 없이 DFS를 구현할 수도 있어요. 바로 스택(Stack)을 이용하는 방법입니다.
# 스택은 '나중에 들어간 것이 먼저 나오는(LIFO)' 자료구조죠.
# 이 특징이 '가장 최근에 방문한 노드의 이웃부터 탐색'하는 DFS의 동작 방식과 딱 맞아떨어져요.
# 재귀 깊이가 너무 깊어져 발생하는 오류를 피할 수 있는 장점이 있습니다.

def dfs_iterative(graph, start_node):
    """
    스택과 반복문을 이용해 DFS 방식으로 그래프를 탐색합니다.
    """
    # 방문한 노드를 기록할 집합
    visited = set()
    
    # 탐색할 노드를 담을 스택 (리스트를 스택처럼 사용)
    stack = [start_node]

    print("반복문 DFS 탐색 시작:")
    
    # 스택이 빌 때까지 계속 반복합니다.
    while stack:
        # 스택의 맨 위에서 노드를 하나 꺼냅니다.
        node = stack.pop()
        
        # 꺼낸 노드가 아직 방문하지 않은 곳이라면
        if node not in visited:
            # 방문 처리하고 출력합니다.
            print(f"방문: {node}")
            visited.add(node)
            
            # 해당 노드의 이웃 노드들을 스택에 추가합니다.
            # 여기서 reversed를 사용하는 이유는 재귀 방식과 출력 순서를 맞추기 위함입니다.
            # 스택은 LIFO 구조라 나중에 넣은 B, C 중 C가 먼저 나오게 되므로
            # 순서를 뒤집어 C, B 순으로 넣으면 B부터 탐색하게 됩니다.
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

if __name__ == '__main__':
    # 탐색에 사용할 그래프 (인접 리스트)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D']
    }
    
    # 'A' 노드부터 탐색을 시작합니다.
    dfs_iterative(graph, 'A')