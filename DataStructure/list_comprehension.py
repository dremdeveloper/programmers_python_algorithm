# 리스트 컴프리헨션: 간결한 리스트 생성 및 필터링

"""
리스트 컴프리헨션(List Comprehension)은 기존의 리스트나 다른 순회 가능한(iterable)
객체를 기반으로 새로운 리스트를 만드는 간결하고 우아한 방법입니다.
일반적인 for 루프와 if 조건문을 한 줄로 압축하여 가독성을 높일 수 있습니다.
"""

# Case 1: 0부터 9까지의 제곱수 리스트 만들기

# 일반적인 for문 사용
squares_loop = []
for i in range(10):
    squares_loop.append(i * i)

# 리스트 컴프리헨션 사용
squares_comp = [i * i for i in range(10)]

print(f"for문 사용: {squares_loop}")
print(f"컴프리헨션 사용: {squares_comp}")


# Case 2: 1부터 20까지의 짝수만 담은 리스트 만들기

# 일반적인 for문과 if문 사용
evens_loop = []
for i in range(1, 21):
    if i % 2 == 0:
        evens_loop.append(i)

# 리스트 컴프리헨션에 필터링(if) 추가
evens_comp = [i for i in range(1, 21) if i % 2 == 0]

print(f"\nfor문+if문 사용: {evens_loop}")
print(f"컴프리헨션+if문 사용: {evens_comp}")