# 제목: 리스트(List) 생성 및 특정 원소 접근하기 (인덱싱)

# 리스트는 여러 개의 데이터를 순서대로 담을 수 있는 자료형입니다.
# 대괄호 []를 사용해서 만듭니다.

# 리스트 생성
numbers = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "cherry"]

print(f"숫자 리스트: {numbers}")
print(f"과일 리스트: {fruits}")

# 리스트의 원소에 접근하기 (인덱싱)
# 인덱스는 0부터 시작합니다!
# [0]은 첫 번째 원소, [1]은 두 번째 원소를 의미합니다.

first_number = numbers[0]
second_fruit = fruits[1]

print(f"\n첫 번째 숫자: {first_number}")
print(f"두 번째 과일: {second_fruit}")

# 마지막 원소에 접근하기
# -1 인덱스는 뒤에서 첫 번째, 즉 마지막 원소를 가리킵니다.
last_number = numbers[-1]
print(f"마지막 숫자: {last_number}")