# 리스트 기본: 생성, 추가, 삭제, 수정

"""
리스트(List)는 파이썬의 가장 기본적인 자료구조 중 하나입니다.
여러 개의 데이터를 순서대로 저장하는 '변경 가능한(mutable)' 시퀀스입니다.
데이터를 추가, 수정, 삭제할 수 있으며, 인덱스를 통해 각 요소에 접근할 수 있습니다.
"""

# 빈 리스트 생성
nums = []
print(f"초기 리스트: {nums}")

# 리스트에 요소 추가 (append: 맨 뒤에 추가)
nums.append(10)
nums.append(30)
print(f"append 후: {nums}")

# 리스트에 요소 추가 (insert: 원하는 위치에 추가)
nums.insert(1, 20) # 인덱스 1 위치에 20 추가
print(f"insert 후: {nums}")

# 리스트 요소 수정
nums[2] = 40 # 인덱스 2 위치의 값을 40으로 변경
print(f"수정 후: {nums}")

# 리스트 요소 삭제 (del: 인덱스로 삭제)
del nums[0] # 인덱스 0 위치의 값 삭제
print(f"del 후: {nums}")

# 리스트 요소 삭제 (pop: 마지막 요소를 꺼내고 삭제)
last_val = nums.pop()
print(f"pop으로 꺼낸 값: {last_val}, pop 후: {nums}")

# 리스트 요소 삭제 (remove: 값으로 삭제)
nums.append(20) # 테스트를 위해 20 다시 추가
print(f"remove 전: {nums}")
nums.remove(20) # 값이 20인 첫 번째 요소를 찾아서 삭제
print(f"remove 후: {nums}")