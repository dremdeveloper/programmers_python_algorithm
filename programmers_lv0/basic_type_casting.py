# 제목: int()와 str()를 사용한 숫자-문자열 변환

# 때로는 숫자처럼 생긴 문자열을 실제 숫자로, 또는 숫자를 문자열로 바꿔야 할 때가 있습니다.
# 이것을 '형 변환(Type Casting)'이라고 합니다.

# 1. 문자열을 숫자로 변환: int()
# input() 함수는 항상 문자열을 반환하므로, 계산을 위해서는 숫자로 바꿔줘야 합니다.
num_str = "123"
num_int = int(num_str)

result = num_int + 100
print(f"문자열 '{num_str}' -> 숫자 {num_int}")
print(f"{num_int} + 100 = {result}")

# 2. 숫자를 문자열로 변환: str()
# 숫자와 문자열을 합치기(+) 위해서는 숫자를 문자열로 바꿔줘야 합니다.
num_val = 456
str_val = str(num_val)

message = "The number is " + str_val
print(f"\n숫자 {num_val} -> 문자열 '{str_val}'")
print(message)