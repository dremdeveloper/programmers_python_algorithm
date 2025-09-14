# 제목: len() 함수로 길이 구하기 (문자열, 리스트)

# len() 함수는 문자열의 글자 수나 리스트의 원소 개수(길이)를 알려줍니다.

# 문자열의 길이
my_string = "Hello, Python!"
string_length = len(my_string)
print(f"문자열 '{my_string}'의 길이: {string_length}")

# 리스트의 길이
my_list = [10, 20, 30, 40]
list_length = len(my_list)
print(f"리스트 {my_list}의 길이: {list_length}")

# for문과 함께 사용하기
# 리스트의 마지막 인덱스는 항상 len(리스트) - 1 입니다.
fruits = ["apple", "banana", "cherry"]
print(f"\n과일 리스트의 길이: {len(fruits)}")
print(f"마지막 과일의 인덱스: {len(fruits) - 1}")
print(f"마지막 과일: {fruits[len(fruits) - 1]}")