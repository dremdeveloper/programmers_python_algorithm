# 제목: for 반복문과 enumerate()로 인덱스와 값 동시 접근

# for 반복문으로 리스트를 순회할 때, 각 원소의 인덱스 번호와 값을
# 동시에 사용해야 하는 경우가 많습니다. 이때 enumerate()가 매우 유용합니다.

fruits = ["apple", "banana", "cherry"]

# 방법 1: range()와 len() 사용
print("--- range(len()) 방식 ---")
for i in range(len(fruits)):
    print(f"인덱스 {i}: {fruits[i]}")

# 방법 2: enumerate() 사용 (더 파이썬답고 깔끔한 방법)
# enumerate()는 (인덱스, 값) 형태의 튜플을 만들어줍니다.
print("\n--- enumerate() 방식 ---")
for index, value in enumerate(fruits):
    print(f"인덱스 {index}: {value}")

# 시작 인덱스를 1로 지정하고 싶을 경우
print("\n--- enumerate(start=1) 방식 ---")
for index, value in enumerate(fruits, start=1):
    print(f"순번 {index}: {value}")