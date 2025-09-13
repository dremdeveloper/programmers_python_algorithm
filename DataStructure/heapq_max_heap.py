# 최대 힙(Max Heap) 구현: heapq와 튜플(음수) 활용

"""
최대 힙(Max Heap)은 부모 노드가 자식 노드보다 항상 크거나 같은 힙입니다.
루트에는 항상 최댓값이 위치합니다.
파이썬의 heapq 모듈은 최소 힙만 직접 지원하기 때문에, 최대 힙을 구현하려면
약간의 트릭이 필요합니다.
데이터를 저장할 때 값에 -1을 곱하여 부호를 바꾼 뒤 최소 힙에 저장하고,
힙에서 값을 꺼낼 때 다시 -1을 곱해 원래 값으로 복원하는 방식입니다.
이렇게 하면 최소 힙의 동작 원리(가장 작은 값을 루트에 두는)를 역이용하여
실질적으로는 최댓값을 루트에서 관리하는 효과를 얻을 수 있습니다.
"""
import heapq

max_heap = []

# push 할 때 음수로 변환하여 저장
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -4)
print(f"최대 힙 (음수로 저장됨): {max_heap}")

# pop 할 때 다시 음수로 변환하여 원래 값으로 복원
largest = -heapq.heappop(max_heap)
print(f"가장 큰 값 pop: {largest}")
print(f"pop 후: {max_heap}")

largest = -heapq.heappop(max_heap)
print(f"가장 큰 값 pop: {largest}")
print(f"pop 후: {max_heap}")