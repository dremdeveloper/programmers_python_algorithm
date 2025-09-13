# 제목: 인접 행렬을 인접 리스트로 변환하기

# 인접 행렬은 두 노드 간의 연결 여부를 O(1)에 확인할 수 있는 장점이 있지만,
# 노드 개수가 많아지면 메모리 공간을 많이 차지하는 단점이 있어요. (V^2에 비례)
# 반면 인접 리스트는 실제 엣지 개수만큼만 공간을 사용해서 더 효율적일 수 있죠. (V+E에 비례)
# 그래서 상황에 맞게 두 표현 방식을 변환해서 사용할 줄 알면 좋습니다.
# 여기서는 인접 행렬을 인접 리스트로 바꾸는 코드를 만들어 볼게요.

def matrix_to_list(matrix):
    """
    인접 행렬을 인접 리스트로 변환합니다.
    """
    num_nodes = len(matrix)
    adj_list = {i: [] for i in range(num_nodes)}

    # 행렬의 모든 요소를 순회합니다.
    for i in range(num_nodes):
        for j in range(num_nodes):
            # 만약 matrix[i][j]가 1이라면, i와 j 사이에 엣지가 있다는 뜻입니다.
            if matrix[i][j] == 1:
                adj_list[i].append(j)
    
    return adj_list

if __name__ == '__main__':
    # 변환할 인접 행렬 (4x4)
    # 노드 0, 1, 2, 3
    adj_matrix = [
        [0, 1, 1, 0],  # 0번 노드는 1, 2번 노드와 연결
        [1, 0, 1, 1],  # 1번 노드는 0, 2, 3번 노드와 연결
        [1, 1, 0, 0],  # 2번 노드는 0, 1번 노드와 연결
        [0, 1, 0, 0]   # 3번 노드는 1번 노드와 연결
    ]
    
    print("변환 전 (인접 행렬):")
    for row in adj_matrix:
        print(row)
        
    print("-" * 20)
    
    # 함수를 호출하여 인접 리스트로 변환
    adj_list = matrix_to_list(adj_matrix)
    
    print("변환 후 (인접 리스트):")
    for node, neighbors in adj_list.items():
        print(f"{node} -> {neighbors}")