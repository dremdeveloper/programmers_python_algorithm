# pop_performance.py
# 제목: list.pop(0)와 collections.deque.popleft()의 성능 비교

import time
from collections import deque

num_elements = 200000

# --- 1. list.pop(0) 성능 측정 ---
# 시간 복잡도: O(n)
# 이유: 리스트의 맨 앞 요소를 제거하면, 그 뒤에 있던 모든 요소들을
#      한 칸씩 앞으로 이동시켜야 합니다. 이 때문에 데이터가 많을수록
#      pop(0) 연산은 매우 느려집니다.
data_list = list(range(num_elements))
start_time = time.time()
while data_list:
    data_list.pop(0)
end_time = time.time()
print(f"list.pop(0) 시간: {end_time - start_time:.6f}초")


# --- 2. deque.popleft() 성능 측정 ---
# 시간 복잡도: O(1)
# 이유: deque(덱)는 양방향 큐(double-ended queue)로, 내부적으로
#      이중 연결 리스트(doubly-linked list)로 구현되어 있습니다.
#      따라서 맨 앞이나 맨 뒤 요소를 추가하거나 제거할 때, 포인터만
#      변경하면 되므로 데이터 양과 상관없이 매우 빠릅니다.
data_deque = deque(range(num_elements))
start_time = time.time()
while data_deque:
    data_deque.popleft()
end_time = time.time()
print(f"deque.popleft() 시간: {end_time - start_time:.6f}초")