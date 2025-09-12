# list_slicing.py
# 제목: 리스트 슬라이싱(Slicing)을 활용한 데이터 처리

# 슬라이싱 기본 구문: list[start:stop:step]
# start: 시작 인덱스 (포함). 생략 시 처음부터.
# stop:  종료 인덱스 (미포함). 생략 시 끝까지.
# step:  간격. 생략 시 1.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"원본 리스트: {numbers}\n")

# --- 1. 기본 슬라이싱 ---
# 인덱스 2부터 5 전까지 (2, 3, 4)
sub_list = numbers[2:5]
print(f"numbers[2:5]: {sub_list}")

# --- 2. 시작/끝 생략 ---
# 처음부터 인덱스 3 전까지 (0, 1, 2)
first_three = numbers[:3]
print(f"numbers[:3]: {first_three}")

# 인덱스 6부터 끝까지
from_six = numbers[6:]
print(f"numbers[6:]: {from_six}")

# --- 3. step 활용 ---
# 처음부터 끝까지 2칸 간격으로 (짝수)
evens = numbers[::2]
print(f"numbers[::2]: {evens}")

# 인덱스 1부터 끝까지 2칸 간격으로 (홀수)
odds = numbers[1::2]
print(f"numbers[1::2]: {odds}")

# --- 4. 리스트 뒤집기 ---
# step을 -1로 주면 리스트를 역순으로 순회합니다.
reversed_list = numbers[::-1]
print(f"numbers[::-1]: {reversed_list}")

# --- 5. 슬라이싱으로 값 변경하기 ---
# 인덱스 2, 3, 4의 값을 새로운 리스트로 대체
print(f"\n값 변경 전: {numbers}")
numbers[2:5] = [99, 98, 97]
print(f"값 변경 후: {numbers}")