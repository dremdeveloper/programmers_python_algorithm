# 제목: 인접 행렬(Adjacency Matrix) 방식 그래프 표현

# 이번에는 그래프를 표현하는 또 다른 방법, 인접 행렬에 대해 배워볼게요.
# 인접 행렬은 2차원 배열(행렬)을 사용해서 노드 간의 연결 관계를 표현합니다.
# 행렬의 [i][j] 값이 1이면 i와 j 노드가 연결되었다는 뜻이고, 0이면 연결되지 않았다는 의미죠.
# 두 노드가 연결되어 있는지 바로 확인하고 싶을 때 O(1)의 시간 복잡도로 아주 빨라요.

def adjacency_matrix_graph(num_nodes):
    """
    인접 행렬 방식으로 무방향 그래프를 생성하고 출력합니다.

    Args:
        num_nodes: 그래프의 노드 개수
    """
    # 노드 개수만큼의 2차원 리스트를 0으로 초기화하여 생성합니다.
    matrix = [[0] * num_nodes for _ in range(num_nodes)]
    
    # 노드 이름을 인덱스로 매핑하기 위한 딕셔너리
    # 여기서는 간단하게 0, 1, 2, 3을 노드 이름처럼 사용하겠습니다.
    node_map = {i: i for i in range(num_nodes)} 

    # 엣지를 추가하는 함수
    def add_edge(u, v):
        # 무방향 그래프이므로 양쪽 모두 1로 설정합니다.
        matrix[u][v] = 1
        matrix[v][u] = 1

    # 그래프에 엣지를 추가해봅시다. (0-A, 1-B, 2-C, 3-D 라고 가정)
    add_edge(node_map[0], node_map[1])  # A-B
    add_edge(node_map[0], node_map[2])  # A-C
    add_edge(node_map[1], node_map[2])  # B-C
    add_edge(node_map[1], node_map[3])  # B-D
    add_edge(node_map[2], node_map[3])  # C-D

    # 생성된 인접 행렬을 출력해볼까요?
    print(f"인접 행렬 그래프 ({num_nodes}x{num_nodes}):")
    for row in matrix:
        print(row)

if __name__ == '__main__':
    # 노드가 4개(0, 1, 2, 3)인 그래프를 만들어 보겠습니다.
    adjacency_matrix_graph(4)