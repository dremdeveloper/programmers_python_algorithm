# 원본 데이터 손상: 얕은 복사(shallow copy) 문제

# 리스트 안에 또 다른 리스트가 있는 중첩 구조에서 복사를 할 때 주의해야 합니다.
# 일반적인 복사 방법(copy() 메서드, [:] 슬라이싱)은 '얕은 복사'로 동작합니다.
# 얕은 복사는 가장 바깥쪽 리스트만 새로 만들고, 내부의 리스트들은 원본과 메모리 주소를 공유합니다.
# 이로 인해 복사본의 내부 리스트를 수정하면 원본까지 함께 변경되는 문제가 발생합니다.

# 예시:
original = [[1, 2], [3, 4]]

# 얕은 복사 수행
shallow_copied = original.copy()

print(f"복사 전 원본: {original}")
print(f"얕은 복사본: {shallow_copied}")
print("-" * 20)

# 복사본의 내부 리스트를 수정
shallow_copied[0].append('X')

print(f"복사본 수정 후 원본: {original}") # 원본까지 변경됨!
print(f"복사본 수정 후: {shallow_copied}")

# 왜 이런 일이?
# id() 함수로 메모리 주소를 확인해보면 이유를 알 수 있습니다.
print("-" * 20)
print(f"original의 주소:        {id(original)}")
print(f"shallow_copied의 주소: {id(shallow_copied)}") # 바깥 리스트는 주소가 다름
print("-" * 20)
print(f"original[0]의 주소:        {id(original[0])}")
print(f"shallow_copied[0]의 주소: {id(shallow_copied[0])}") # 내부 리스트는 주소가 같음!

# 해결 방법: 깊은 복사(deep copy)
# copy 모듈의 deepcopy() 함수를 사용하면 내부 객체들까지 모두 새로 복사하여
# 원본과 완전히 독립적인 복사본을 만들 수 있습니다.

import copy

original_deep = [[1, 2], [3, 4]]
deep_copied = copy.deepcopy(original_deep)

print("\n--- 깊은 복사 예시 ---")
print(f"깊은 복사 전 원본: {original_deep}")
print(f"깊은 복사본: {deep_copied}")
print("-" * 20)

# 깊은 복사본의 내부 리스트 수정
deep_copied[0].append('Y')

print(f"깊은 복사본 수정 후 원본: {original_deep}") # 원본이 변경되지 않음!
print(f"깊은 복사본 수정 후: {deep_copied}")