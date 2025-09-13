# heapq 활용: K번째 가장 작은/큰 수 찾기

"""
힙(heap) 자료구조는 전체 데이터를 정렬하지 않고도 K번째로 크거나 작은 원소를
효율적으로 찾는 데 활용될 수 있습니다.
- K번째 작은 수: 데이터를 모두 힙에 넣고 K번 pop하면 됩니다. (O(N log N))
  또는, 데이터를 힙으로 만든 후(O(N)), K번 pop(O(K log N))하면 더 효율적입니다.
- K번째 큰 수: 크기가 K인 '최소 힙'을 유지하는 것이 핵심입니다.
  전체 데이터를 순회하며 현재 원소가 힙의 최솟값(루트)보다 크면, 루트를 제거하고
  현재 원소를 힙에 추가합니다. 이 과정을 마치면 힙에는 가장 큰 K개의 원소가
  남게 되며, 그중 최솟값(루트)이 바로 K번째 큰 수가 됩니다. (시간 복잡도: O(N log K))
"""
import heapq

nums = [9, 4, 7, 2, 8, 5, 3, 6, 1]
k = 3

# K번째 가장 작은 수 찾기
heap_s = list(nums)
heapq.heapify(heap_s)
kth_smallest = heapq.nsmallest(k, heap_s)[-1]
print(f"{k}번째 가장 작은 수: {kth_smallest}")

# K번째 가장 큰 수 찾기 (O(N log K) 알고리즘)
# 핵심 코드
max_heap_k = []
for num in nums:
    if len(max_heap_k) < k:
        heapq.heappush(max_heap_k, num)
    elif num > max_heap_k[0]: # 힙의 최솟값보다 크면
        heapq.heapreplace(max_heap_k, num) # 최솟값을 빼고 새 원소를 넣음

# 최종적으로 힙의 루트가 K번째 큰 수가 됨
kth_largest = max_heap_k[0]
print(f"{k}번째 가장 큰 수: {kth_largest}")