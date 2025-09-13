# 딕셔너리 기본: 키-값 쌍 조회, 추가, 삭제

"""
딕셔너리(Dictionary)는 '키(Key)'와 '값(Value)'을 하나의 쌍으로 묶어서 저장하는
자료구조입니다. 순서가 없는(Python 3.7+ 부터는 입력 순서 유지) 컬렉션이며,
키를 통해 값을 매우 빠르게 조회, 추가, 수정, 삭제할 수 있습니다.
키는 중복될 수 없으며, 보통 변경 불가능한(immutable) 자료형을 사용합니다.
"""

# 딕셔너리 생성
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
print(f"초기 딕셔너리: {student}")

# 키(key)를 이용해 값(value) 조회
name = student["name"]
print(f"이름 조회: {name}")

# 새로운 키-값 쌍 추가
student["gpa"] = 4.3
print(f"gpa 추가 후: {student}")

# 기존 키의 값 수정
student["age"] = 21
print(f"나이 수정 후: {student}")

# del 키워드로 키-값 쌍 삭제
del student["major"]
print(f"major 삭제 후: {student}")