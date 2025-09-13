# 논리 오류: is와 ==의 혼동

# '=='와 'is'는 파이썬에서 비교 연산자로 쓰이지만, 그 의미는 다릅니다.
# 이 둘을 혼동하면 눈에 띄지 않는 논리적 오류를 만들 수 있습니다.

# == : 값(Value)의 동등성을 비교합니다. 두 객체가 담고 있는 내용이 같은지 확인합니다.
# is : 정체성(Identity)의 동등성을 비교합니다. 두 변수가 완전히 동일한 메모리 주소의 객체를 가리키는지 확인합니다.

# 예시
list_a = [1, 2, 3]
list_b = [1, 2, 3] # list_a와 내용은 같지만, 새로 만들어진 별개의 객체
list_c = list_a   # list_a가 가리키는 메모리 주소를 그대로 가리킴

# '=='로 값 비교
print(f"list_a == list_b : {list_a == list_b}") # True (내용이 같음)
print(f"list_a == list_c : {list_a == list_c}") # True (내용이 같음)

print("-" * 20)

# 'is'로 메모리 주소(정체성) 비교
print(f"list_a is list_b : {list_a is list_b}") # False (서로 다른 객체)
print(f"list_a is list_c : {list_a is list_c}") # True (완전히 같은 객체)

print("-" * 20)

# id() 함수로 실제 메모리 주소 확인
print(f"id(list_a): {id(list_a)}")
print(f"id(list_b): {id(list_b)}") # list_a와 주소가 다름
print(f"id(list_c): {id(list_c)}") # list_a와 주소가 같음

# 정리:
# - 객체의 내용물이 같은지 비교할 때는 '=='를 사용해야 합니다.
# - 두 변수가 정말로 같은 객체를 참조하고 있는지 확인해야 하는 특별한 경우에 'is'를 사용합니다.
# - None, True, False 와 같은 단일 객체는 'is'로 비교하는 것이 관례입니다. (e.g., if x is None:)