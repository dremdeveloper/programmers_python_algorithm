# list_comprehensions.py
# 제목: 리스트 컴프리헨션(List Comprehension) 활용

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# --- 예제 1: 각 숫자의 제곱으로 이루어진 새로운 리스트 만들기 ---

# 일반적인 for 루프 사용
squares_loop = []
for num in numbers:
    squares_loop.append(num * num)
print(f"For 루프 사용: {squares_loop}")

# 리스트 컴프리헨션 사용 (더 간결하고 파이써닉합니다)
# [표현식 for 항목 in 반복가능객체]
squares_comp = [num * num for num in numbers]
print(f"컴프리헨션 사용: {squares_comp}")


# --- 예제 2: 짝수만 골라서 새로운 리스트 만들기 ---

# 일반적인 for 루프와 if문 사용
evens_loop = []
for num in numbers:
    if num % 2 == 0:
        evens_loop.append(num)
print(f"\nFor 루프와 if문 사용: {evens_loop}")

# 리스트 컴프리헨션에 조건문 추가
# [표현식 for 항목 in 반복가능객체 if 조건문]
evens_comp = [num for num in numbers if num % 2 == 0]
print(f"컴프리헨션과 if문 사용: {evens_comp}")