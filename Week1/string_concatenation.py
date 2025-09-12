# string_concatenation.py
# 제목: 문자열 합치기: + 연산과 join() 메소드의 성능 비교

import time

# 합칠 문자열의 개수
num_strings = 50000
my_strings = ['hello'] * num_strings

# --- 1. '+' 연산을 사용한 문자열 합치기 ---
# 시간 복잡도: O(n^2)
# 이유: 파이썬에서 문자열은 불변(immutable) 객체입니다.
#      따라서 '+' 연산이 일어날 때마다 새로운 문자열 객체가 생성되고,
#      이전 문자열의 내용이 새 객체로 '복사'됩니다.
#      이 복사 과정 때문에 루프가 돌수록 처리 시간이 기하급수적으로 늘어납니다.
start_time = time.time()
result_plus = ''
for s in my_strings:
    result_plus += s
end_time = time.time()
print(f"'+' 연산 사용 시간: {end_time - start_time:.6f}초")


# --- 2. join() 메소드를 사용한 문자열 합치기 ---
# 시간 복잡도: O(n)
# 이유: join() 메소드는 리스트의 모든 문자열을 한 번만 순회하여
#      필요한 전체 메모리 공간을 미리 계산하고 할당합니다.
#      그 후, 각 문자열을 해당 공간에 복사하므로 훨씬 효율적입니다.
start_time = time.time()
result_join = ''.join(my_strings)
end_time = time.time()
print(f"join() 메소드 사용 시간: {end_time - start_time:.6f}초")