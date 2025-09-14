# 제목: .append() 메소드로 리스트에 원소 추가하기

# .append()는 리스트의 맨 뒤에 새로운 원소를 추가하는 기능(메소드)입니다.

# 비어있는 리스트로 시작
numbers = []
print(f"초기 리스트: {numbers}")

# .append()로 원소 추가
numbers.append(10)
print(f"10 추가 후: {numbers}")

numbers.append(20)
print(f"20 추가 후: {numbers}")

numbers.append(30)
print(f"30 추가 후: {numbers}")

# for문을 이용해 여러 원소 추가하기
fruits = ["apple", "banana"]
new_fruits = ["cherry", "orange"]

for fruit in new_fruits:
    fruits.append(fruit)

print(f"\n과일 추가 후: {fruits}")