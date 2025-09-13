# Off-by-one 오류: 반복문 범위 실수

# Off-by-one 오류는 프로그래밍에서 매우 흔한 논리적 실수 중 하나로,
# 반복문의 범위나 인덱스 계산을 할 때 1만큼 더하거나 덜 계산해서 발생합니다.
# 특히 파이썬의 range() 함수나 리스트 인덱싱에서 자주 나타납니다.

# 파이썬의 특징:
# 1. 인덱스는 0부터 시작한다.
# 2. range(start, stop)은 stop 바로 앞까지의 숫자를 생성한다. (stop은 포함되지 않음)
# 3. 슬라이싱[start:stop] 역시 stop 인덱스는 포함하지 않는다.

# 예시: 1부터 10까지의 합 구하기
numbers = list(range(1, 11)) # 1, 2, ..., 10
total = sum(numbers)
print(f"1부터 10까지의 합은 {total} 입니다.")

# 잘못된 경우 1: range(1, 10) 사용
# 1부터 9까지만 반복하게 되어 결과가 틀립니다.
wrong_total_1 = 0
for i in range(1, 10): # 1, 2, ..., 9
    wrong_total_1 += i
print(f"잘못된 경우 1 (range(1, 10)): {wrong_total_1}")

# 잘못된 경우 2: 리스트의 마지막 요소에 접근하려 할 때
my_list = ['a', 'b', 'c'] # 길이: 3, 인덱스: 0, 1, 2
list_len = len(my_list)

# 마지막 요소의 인덱스는 len(my_list) - 1 입니다.
# len(my_list) 인덱스에 접근하면 IndexError가 발생합니다.
print(f"마지막 요소: {my_list[list_len - 1]}")
# 주석을 해제하고 실행해보세요
# print(my_list[list_len])

# 해결 방법:
# - range()의 두 번째 인자는 내가 원하는 마지막 숫자 + 1 이어야 함을 기억합니다.
# - 리스트의 마지막 인덱스는 항상 '길이 - 1' 임을 명심합니다.
# - 코드를 작성한 후 경계값(처음과 끝)을 기준으로 테스트하는 습관을 들입니다.