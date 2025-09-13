# collections.deque: 스택(Stack)과 큐(Queue) 구현

"""
데크(deque)는 'double-ended queue'의 약자로, 양쪽 끝에서 데이터를 추가하거나
삭제할 수 있는 자료구조입니다.
특히 큐(Queue, FIFO)를 구현할 때 매우 효율적입니다.

- 리스트로 큐 구현 시: list.pop(0)은 첫 요소를 빼고 모든 요소를 한 칸씩
  앞으로 당겨야 하므로 시간 복잡도가 O(N)입니다. 데이터가 많으면 매우 비효율적입니다.
- 데크로 큐 구현 시: deque.popleft()는 내부적으로 이중 연결 리스트로 구현되어
  있어 첫 요소를 제거하는 연산이 O(1)으로 매우 빠릅니다.
"""
from collections import deque

# 큐 (Queue) - 선입선출 (FIFO: First-In, First-Out)
queue = deque()
queue.append(1) # Enqueue
queue.append(2)
queue.append(3)
print(f"초기 큐: {queue}")

val = queue.popleft() # Dequeue
print(f"꺼낸 값: {val}")
print(f"큐 현황: {queue}\n")


# 스택 (Stack) - 후입선출 (LIFO: Last-In, First-Out)
# 스택은 일반 리스트의 append(), pop()으로도 O(1)이라 효율적이지만,
# 양방향 입출력이 모두 필요할 경우 deque으로 일관성 있게 구현하기도 합니다.
stack = deque()
stack.append(10) # Push
stack.append(20)
print(f"초기 스택: {stack}")

val = stack.pop() # Pop
print(f"꺼낸 값: {val}")
print(f"스택 현황: {stack}")