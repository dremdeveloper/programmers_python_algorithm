# 딕셔너리 순회: keys(), values(), items() 메서드 활용

"""
딕셔너리를 for 루프와 함께 사용할 때, 어떤 것을 기준으로 순회할지 정할 수 있습니다.
- .keys(): 딕셔너리의 모든 키를 순회합니다. (for key in my_dict: 와 동일)
- .values(): 딕셔너리의 모든 값을 순회합니다.
- .items(): (키, 값) 튜플 쌍을 순회합니다. 가장 일반적으로 사용됩니다.
"""

student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

# .keys() - 딕셔너리의 모든 키 순회
print("--- Keys ---")
for key in student.keys():
    print(key)

# .values() - 딕셔너리의 모든 값 순회
print("\n--- Values ---")
for value in student.values():
    print(value)

# .items() - 딕셔너리의 모든 (키, 값) 쌍을 튜플로 순회
print("\n--- Items ---")
for key, value in student.items():
    print(f"{key}: {value}")