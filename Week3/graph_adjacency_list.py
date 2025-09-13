# 제목: 인접 리스트(Adjacency List) 방식 그래프 표현

# 안녕하세요! 오늘은 그래프를 표현하는 가장 흔한 방법 중 하나인
# 인접 리스트 방식에 대해 알아볼 거예요.
# 인접 리스트는 각 노드(정점)에 연결된 노드들을 리스트 형태로 저장하는 방식입니다.
# 특정 노드와 연결된 모든 노드를 빠르게 찾고 싶을 때 아주 유용하죠.

def adjacency_list_graph():
    """
    인접 리스트 방식으로 무방향 그래프를 생성하고 출력합니다.
    """
    # 그래프를 딕셔너리로 표현해볼게요.
    # key는 노드, value는 해당 노드에 연결된 노드들의 리스트입니다.
    graph = {}

    # 엣지(간선)를 추가하는 함수
    def add_edge(u, v):
        # u에 v를 연결하고, v에도 u를 연결합니다 (무방향 그래프)
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)

    # 그래프에 엣지를 추가해봅시다.
    add_edge('A', 'B')
    add_edge('A', 'C')
    add_edge('B', 'C')
    add_edge('B', 'D')
    add_edge('C', 'D')

    # 생성된 인접 리스트를 출력해볼까요?
    print("인접 리스트 그래프:")
    for node, neighbors in graph.items():
        print(f"{node} -> {neighbors}")

if __name__ == '__main__':
    adjacency_list_graph()