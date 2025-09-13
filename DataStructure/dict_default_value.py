# 딕셔너리 기본값 처리: get() 메서드와 try-except 구문

"""
딕셔너리에서 존재하지 않는 키로 값을 조회하려고 하면 'KeyError'가 발생합니다.
이러한 예외를 처리하는 방법은 두 가지가 있습니다.
1. try-except: 예외 처리 구문을 사용하여 에러를 직접 처리합니다.
2. .get(key, default): .get() 메서드를 사용합니다. 키가 있으면 해당 값을,
   없으면 지정한 기본값(default)을 반환하여 코드를 더 간결하게 만듭니다.
"""

student = {
    "name": "Alice",
    "age": 21,
}

# Case 1: try-except 구문으로 KeyError 처리
try:
    print(student['major'])
except KeyError:
    print("'major' 키가 존재하지 않습니다.")

# Case 2: get() 메서드 사용 (권장)
# 'major'가 없으므로 기본값 'N/A' 반환
major = student.get('major', 'N/A')
# 'name'은 있으므로 해당 값 'Alice' 반환
name = student.get('name', 'N/A')

print(f"\nget()으로 조회한 전공: {major}")
print(f"get()으로 조회한 이름: {name}")