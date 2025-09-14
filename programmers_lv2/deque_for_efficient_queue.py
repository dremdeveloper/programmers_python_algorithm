# 제목: collections.deque로 효율적인 큐/덱 사용하기
from collections import deque

# 파이썬 기본 리스트로 큐를 구현하면, 맨 앞의 원소를 제거(pop(0))할 때
# 뒤따르는 모든 원소들을 한 칸씩 앞으로 당겨야 하므로 비효율적입니다. (시간 복잡도: O(N))
# collections.deque는 양방향 연결 리스트로 구현되어 있어
# 양쪽 끝에서의 추가/제거가 모두 O(1)로 매우 빠릅니다.

# 큐(Queue): 선입선출 (FIFO)
q = deque()

# Enqueue (데이터 추가)
q.append(1)
q.append(2)
q.append(3)
print(f"큐 상태: {q}")

# Dequeue (데이터 추출)
item = q.popleft() # O(1) 연산
print(f"추출된 아이템: {item}, 남은 큐: {q}")


# 덱(Deque): 양쪽 끝에서 추가/제거 가능
d = deque([10, 20, 30])
print(f"\n덱 상태: {d}")

# 오른쪽 끝에 추가
d.append(40)
print(f"append(40) 후: {d}")

# 왼쪽 끝에 추가
d.appendleft(0)
print(f"appendleft(0) 후: {d}")

# 오른쪽 끝에서 제거
d.pop()
print(f"pop() 후: {d}")

# 왼쪽 끝에서 제거
d.popleft()
print(f"popleft() 후: {d}")