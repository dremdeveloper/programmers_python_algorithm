# 제목: 숫자와 문자열 간 타입 변환 (int(), str())

# 프로그램에서는 종종 문자열로 된 숫자를 실제 숫자로, 또는 그 반대로 바꿔야 합니다.

# 1. 문자열 -> 정수 (int())
# 사용자의 키보드 입력(input())은 항상 문자열 형태이므로,
# 계산을 위해서는 반드시 숫자로 변환해주어야 합니다.
num_str = "100"
# num_str + 50 # 이 코드는 TypeError 발생

# int() 함수로 문자열을 정수로 변환
num_int = int(num_str)
result = num_int + 50

print(f"문자열 '{num_str}'을 정수 {num_int}로 변환")
print(f"{num_int} + 50 = {result}")

# 2. 정수 -> 문자열 (str())
# 숫자와 문자열을 하나로 합쳐서 출력하고 싶을 때 사용합니다.
age = 25
# "나이: " + age # 이 코드는 TypeError 발생

# str() 함수로 정수를 문자열로 변환
age_str = str(age)
message = "나이: " + age_str

print(f"\n정수 {age}를 문자열 '{age_str}'로 변환")
print(message)