# 제목: zip() 함수로 여러 리스트를 병렬로 묶어 순회하기

# zip() 함수는 여러 개의 리스트(또는 다른 반복 가능한 객체)를 받아,
# 같은 인덱스에 있는 원소들을 하나의 튜플로 묶어줍니다.
# for문에서 여러 리스트를 동시에 순회할 때 매우 편리합니다.

students = ["Alice", "Bob", "Charlie"]
scores = [95, 88, 76]

# zip()을 사용하여 두 리스트를 묶기
student_scores = zip(students, scores)
print("zip 객체:", student_scores) # zip 객체는 내용을 바로 보여주지 않음
print("list(zip) 결과:", list(student_scores)) # 이터레이터는 한 번 사용하면 소진됨

print("\n--- for문과 zip 함께 사용하기 ---")
# for 반복문에서 각 튜플을 바로 변수로 받아 사용할 수 있습니다.
for name, score in zip(students, scores):
    print(f"학생: {name}, 점수: {score}")

# 주의: zip()은 가장 짧은 리스트의 길이를 기준으로 동작합니다.
ids = [1, 2]
names = ["John", "Susan", "David"]
for id_num, name in zip(ids, names):
    print(f"ID: {id_num}, 이름: {name}") # David는 짝이 없으므로 출력되지 않음