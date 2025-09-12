# queue_with_deque.py
# 제목: collections.deque를 이용한 큐(Queue) 구현

from collections import deque

# 큐는 FIFO (First-In, First-Out) 또는 선입선출 구조를 따릅니다.
# 리스트로 큐를 구현할 수 있지만, 맨 앞 요소를 제거(pop(0))하는 것은
# O(n)의 비효율적인 연산입니다.
# 따라서 양쪽 끝에서 데이터를 추가하고 제거하는 것이 O(1)인 deque를 사용하는 것이 좋습니다.

# 1. 큐 생성 (빈 deque로 초기화)
queue = deque()
print(f"초기 큐: {queue}")

# 2. Enqueue 연산: 큐에 데이터 추가
# deque의 append() 메소드를 사용합니다. (오른쪽 끝에 추가)
queue.append(100)
queue.append(200)
queue.append(300)
print(f"데이터 Enqueue 후: {queue}")

# 3. Dequeue 연산: 큐에서 데이터 꺼내기
# deque의 popleft() 메소드를 사용합니다. (왼쪽 끝에서 제거)
if queue:
    dequeued_element = queue.popleft()
    print(f"Dequeue된 데이터: {dequeued_element}")
    print(f"데이터 Dequeue 후: {queue}")

# 모든 데이터 Dequeue 하기
dequeued_element = queue.popleft()
print(f"Dequeue된 데이터: {dequeued_element}, 큐 상태: {queue}")
dequeued_element = queue.popleft()
print(f"Dequeue된 데이터: {dequeued_element}, 큐 상태: {queue}")

# 4. 큐가 비었는지 확인
if not queue:
    print("큐가 비어있습니다.")