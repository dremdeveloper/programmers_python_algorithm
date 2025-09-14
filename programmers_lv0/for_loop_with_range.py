# 제목: for 반복문과 range() 함수 기본 사용법

# for 반복문은 특정 코드를 여러 번 반복해서 실행하고 싶을 때 사용합니다.
# range() 함수는 반복 횟수를 지정하는 데 아주 편리합니다.

# 1. 기본적인 반복
# range(5)는 0, 1, 2, 3, 4까지의 숫자를 만들어냅니다. (5는 포함 안 됨)
print("0부터 4까지 출력:")
for i in range(5):
    print(i)

# 2. 시작과 끝 지정하기
# range(1, 6)은 1, 2, 3, 4, 5까지의 숫자를 만들어냅니다. (6은 포함 안 됨)
print("\n1부터 5까지 출력:")
for i in range(1, 6):
    print(i)

# 3. 리스트의 모든 원소에 접근하기
fruits = ["apple", "banana", "cherry"]
print("\n과일 리스트 출력:")
for fruit in fruits:
    print(fruit)