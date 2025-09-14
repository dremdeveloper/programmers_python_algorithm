# 제목: 리스트 컴프리헨션(List Comprehension) 기본 활용법

# 리스트 컴프리헨션은 for문과 if문을 한 줄에 담아 간결하게 리스트를 만드는 방법입니다.

# 예시 1: 0부터 9까지의 숫자를 제곱한 리스트 만들기

# 기본 for문 방식
squares_loop = []
for i in range(10):
    squares_loop.append(i * i)
print(f"For 루프 방식: {squares_loop}")

# 리스트 컴프리헨션 방식
# [표현식 for 항목 in 반복가능객체]
squares_comp = [i * i for i in range(10)]
print(f"컴프리헨션 방식: {squares_comp}")


# 예시 2: 1부터 10까지의 짝수만 담은 리스트 만들기

# 기본 for문 방식
evens_loop = []
for i in range(1, 11):
    if i % 2 == 0:
        evens_loop.append(i)
print(f"\nFor 루프 방식 (짝수): {evens_loop}")

# 리스트 컴프리헨션 방식 (조건문 추가)
# [표현식 for 항목 in 반복가능객체 if 조건]
evens_comp = [i for i in range(1, 11) if i % 2 == 0]
print(f"컴프리헨션 방식 (짝수): {evens_comp}")