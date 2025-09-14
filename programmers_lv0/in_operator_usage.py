# 제목: in 연산자로 특정 원소의 포함 여부 확인하기

# 'in' 연산자는 어떤 원소가 리스트나 문자열 같은 그룹 안에 포함되어 있는지
# 확인하여 결과를 참(True) 또는 거짓(False)으로 알려줍니다.

# 리스트에서 사용하기
fruits = ["apple", "banana", "cherry"]

# "apple"이 fruits 리스트 안에 있는가?
is_apple_in = "apple" in fruits
print(f"'apple' in {fruits} -> {is_apple_in}")

# "grape"가 fruits 리스트 안에 있는가?
is_grape_in = "grape" in fruits
print(f"'grape' in {fruits} -> {is_grape_in}")

# if문과 함께 사용
my_fruit = "banana"
if my_fruit in fruits:
    print(f"{my_fruit}은(는) 목록에 있습니다.")
else:
    print(f"{my_fruit}은(는) 목록에 없습니다.")

# 문자열에서 사용하기
# 특정 부분 문자열이 포함되어 있는지 확인할 수 있습니다.
sentence = "Hello, welcome to Python world!"

is_python_in = "Python" in sentence
print(f"\n'Python' in '{sentence}' -> {is_python_in}")

is_java_in = "Java" in sentence
print(f"'Java' in '{sentence}' -> {is_java_in}")