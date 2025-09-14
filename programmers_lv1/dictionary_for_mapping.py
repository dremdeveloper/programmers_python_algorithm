# 제목: 딕셔너리(Dictionary)로 key-value 데이터 관리하기

# 딕셔너리는 '키(Key)'와 '값(Value)'을 하나의 쌍으로 묶어 저장하는 자료형입니다.
# 순서가 아닌 고유한 키를 통해 데이터를 빠르고 효율적으로 찾을 수 있습니다.

# 1. 딕셔너리 생성
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
print(f"학생 정보 딕셔너리: {student}")

# 2. 값 접근하기 (키 사용)
student_name = student["name"]
print(f"이름: {student_name}")

# 3. 새로운 key-value 쌍 추가하기
student["grade"] = "A"
print(f"학점 추가 후: {student}")

# 4. 기존 값 수정하기
student["age"] = 21
print(f"나이 수정 후: {student}")

# 5. key-value 쌍 삭제하기
del student["major"]
print(f"전공 삭제 후: {student}")