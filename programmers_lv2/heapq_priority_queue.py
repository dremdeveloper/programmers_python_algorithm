# 제목: heapq를 이용한 우선순위 큐 구현 (최소/최대 힙)
import heapq

# heapq는 파이썬 리스트를 최소 힙처럼 다룰 수 있게 해주는 라이브러리입니다.
# 우선순위가 높은(값이 작은) 데이터부터 처리할 때 사용합니다.

# 1. 최소 힙 (Min Heap)
min_heap = []
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 7)
print(f"최소 힙: {min_heap}") # 항상 heap[0]이 최솟값

print(f"가장 작은 값: {heapq.heappop(min_heap)}")
print(f"남은 힙: {min_heap}")


# 2. 최대 힙 (Max Heap)
# 파이썬 heapq는 최소 힙만 지원하므로, 최대 힙은 값에 -를 붙이는 트릭을 사용합니다.
max_heap = []
heapq.heappush(max_heap, -4)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -7)
print(f"\n최대 힙 (내부 표현): {max_heap}")

# 값을 꺼낼 때 다시 -를 붙여 원래 값으로 되돌립니다.
print(f"가장 큰 값: {-heapq.heappop(max_heap)}")
print(f"남은 힙: {max_heap}")