# search_comparison.py
# 제목: list와 set에서의 요소 검색 시간 비교 (in 연산자)

import time

# 비교를 위해 큰 데이터셋을 준비합니다.
# 1부터 10,000,000까지의 숫자를 사용하겠습니다.
num_elements = 10_000_000
data_list = list(range(num_elements))
data_set = set(range(num_elements))

# 찾고자 하는 값 (가장 마지막 값으로 설정하여 리스트에서 최악의 경우를 만듭니다)
target = num_elements - 1

# --- 1. list에서 요소 검색 ---
# 시간 복잡도: O(n)
# 이유: 리스트는 순차적인 자료구조이므로, 특정 요소를 찾기 위해
#      처음부터 끝까지 모든 요소를 하나씩 확인해야 할 수 있습니다. (선형 탐색)
start_time = time.time()
result_list = target in data_list
end_time = time.time()
print(f"list 검색 시간: {end_time - start_time:.6f}초 (결과: {result_list})")


# --- 2. set에서 요소 검색 ---
# 시간 복잡도: O(1) (평균)
# 이유: set은 해시 테이블을 기반으로 하는 자료구조입니다.
#      각 요소의 해시값(hash)을 통해 저장 위치를 바로 계산할 수 있어,
#      데이터의 양과 상관없이 거의 일정한 시간 안에 요소를 찾을 수 있습니다.
start_time = time.time()
result_set = target in data_set
end_time = time.time()
print(f"set 검색 시간: {end_time - start_time:.6f}초 (결과: {result_set})")