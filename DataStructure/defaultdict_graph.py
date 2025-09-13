# defaultdict 활용: 그래프 인접 리스트 표현하기

"""
그래프(Graph)는 노드(정점)와 그 노드들을 연결하는 엣지(간선)로 구성된 자료구조입니다.
그래프를 표현하는 방법 중 하나인 '인접 리스트'는 각 노드에 연결된 다른 노드들의
리스트를 저장하는 방식입니다.
defaultdict(list)를 사용하면 각 노드에 대한 리스트를 초기화하는 과정 없이
간결하게 인접 리스트를 구현할 수 있습니다.
"""
from collections import defaultdict

# 그래프의 엣지(간선) 리스트: (출발 노드, 도착 노드)
edges = [
    (1, 2), (1, 3),
    (2, 4), (2, 5),
    (3, 1), (4, 2)
]

# defaultdict(list)를 이용해 인접 리스트 생성
graph = defaultdict(list)

for u, v in edges:
    graph[u].append(v)

print("그래프 인접 리스트:")
for node in sorted(graph.keys()):
    print(f"{node}: {graph[node]}")