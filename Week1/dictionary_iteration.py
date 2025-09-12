# dictionary_iteration.py
# 제목: 딕셔너리(Dictionary)의 다양한 순회 방법

student = {
    'name': '홍길동',
    'age': 25,
    'major': '컴퓨터공학'
}

# --- 1. 키(key) 순회 ---
# 딕셔너리를 for문에서 그냥 사용하면 기본적으로 키를 순회합니다.
print("--- 키(key) 순회 ---")
for key in student:
    print(key)
# .keys() 메소드를 명시적으로 사용할 수도 있습니다.
for key in student.keys():
    print(key)


# --- 2. 값(value) 순회 ---
# .values() 메소드를 사용합니다.
print("\n--- 값(value) 순회 ---")
for value in student.values():
    print(value)


# --- 3. 키와 값(key-value) 동시 순회 ---
# .items() 메소드를 사용하면 (키, 값) 형태의 튜플을 얻을 수 있습니다.
# 이를 언패킹하여 키와 값을 동시에 변수에 할당받는 것이 일반적입니다.
print("\n--- 키와 값 동시 순회 ---")
for key, value in student.items():
    print(f"{key}: {value}")