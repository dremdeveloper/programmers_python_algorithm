# heapq 모듈: 최소 힙(Min Heap) 생성 및 사용법

"""
힙(Heap)은 '완전 이진 트리' 구조를 기반으로 하는 자료구조로,
부모 노드와 자식 노드 간에 특정 대소 관계가 항상 성립합니다.
- 최소 힙(Min Heap): 부모 노드의 값이 자식 노드의 값보다 항상 작거나 같습니다.
  따라서 루트 노드에는 항상 전체 데이터 중 최솟값이 위치합니다.
파이썬의 heapq 모듈은 일반 리스트를 최소 힙처럼 다룰 수 있게 해주는 함수들을 제공합니다.
데이터를 넣고(push) 빼는(pop) 연산은 O(log N)의 시간 복잡도를 가집니다.
"""
import heapq

# 리스트를 힙으로 변환 (heapify) - O(N)
nums = [4, 1, 7, 3, 8, 5]
heapq.heapify(nums)
print(f"heapify 후 리스트: {nums}")

# 힙에 원소 추가 (heappush) - O(log N)
heapq.heappush(nums, 2)
print(f"2 추가 후: {nums}")

# 힙에서 가장 작은 원소 삭제 및 반환 (heappop) - O(log N)
min_val = heapq.heappop(nums)
print(f"가장 작은 값 pop: {min_val}, pop 후: {nums}")

min_val = heapq.heappop(nums)
print(f"가장 작은 값 pop: {min_val}, pop 후: {nums}")