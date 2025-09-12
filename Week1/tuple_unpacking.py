# tuple_unpacking.py
# 제목: 튜플 언패킹(Tuple Unpacking) 활용 예제

# --- 1. 기본 변수 할당 ---
# 튜플 (또는 리스트)의 각 요소를 순서대로 변수에 할당합니다.
point = (3, 5)
x, y = point
print(f"점의 좌표: x={x}, y={y}")


# --- 2. 변수 값 교환 (Swap) ---
# 임시 변수 없이 한 줄로 두 변수의 값을 바꿀 수 있는 파이써닉한 방법입니다.
a = 10
b = 20
print(f"\n교환 전: a={a}, b={b}")
a, b = b, a  # (b, a) 라는 새로운 튜플을 만들어 a, b에 각각 언패킹
print(f"교환 후: a={a}, b={b}")


# --- 3. for문에서 활용 ---
# 리스트 안에 튜플이 있는 구조에서 매우 유용합니다.
students = [('김철수', 18), ('이영희', 19), ('박지성', 20)]
print("\n학생 명단:")
for name, age in students:
    print(f"이름: {name}, 나이: {age}")


# --- 4. 확장 언패킹 (Extended Unpacking) ---
# `*`를 사용하여 여러 개의 요소를 하나의 리스트로 받을 수 있습니다.
numbers = [1, 2, 3, 4, 5, 6]
first, *middle, last = numbers
print("\n확장 언패킹:")
print(f"first: {first}")   # 1
print(f"middle: {middle}") # [2, 3, 4, 5]
print(f"last: {last}")     # 6


# --- 5. 특정 값 무시하기 ---
# 관례적으로 사용하지 않을 변수는 밑줄(_)로 받습니다.
person_data = ('홍길동', 30, '서울시', '010-1234-5678')
name, _, city, _ = person_data
print(f"\n무시하기:")
print(f"이름: {name}, 도시: {city}")