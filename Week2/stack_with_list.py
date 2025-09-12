# stack_with_list.py
# 제목: list를 이용한 스택(Stack) 구현

# 파이썬의 리스트는 스택의 모든 기능을 효율적으로 제공합니다.
# LIFO (Last-In, First-Out) 또는 후입선출 구조를 따릅니다.

# 1. 스택 생성 (빈 리스트로 초기화)
stack = []
print(f"초기 스택: {stack}")

# 2. PUSH 연산: 스택에 데이터 추가
# 리스트의 append() 메소드를 사용합니다. O(1)의 시간 복잡도를 가집니다.
stack.append(10)
stack.append(20)
stack.append(30)
print(f"데이터 PUSH 후: {stack}")

# 3. PEEK (or TOP) 연산: 스택의 가장 위 데이터 확인
# 스택을 변경하지 않고, 마지막 요소에 접근합니다.
# 스택이 비어있지 않을 때만 가능합니다.
if stack:
    top_element = stack[-1]
    print(f"현재 TOP 데이터: {top_element}")

# 4. POP 연산: 스택에서 데이터 꺼내기
# 리스트의 pop() 메소드를 사용합니다. 마지막 요소를 제거하고 반환합니다. O(1) 입니다.
if stack:
    popped_element = stack.pop()
    print(f"POP된 데이터: {popped_element}")
    print(f"데이터 POP 후: {stack}")

# 모든 데이터 POP 하기
popped_element = stack.pop()
print(f"POP된 데이터: {popped_element}, 스택 상태: {stack}")
popped_element = stack.pop()
print(f"POP된 데이터: {popped_element}, 스택 상태: {stack}")

# 5. 스택이 비었는지 확인
if not stack:
    print("스택이 비어있습니다.")