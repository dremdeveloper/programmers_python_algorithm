# ValueError: 부적절한 값으로 함수 호출

# 함수에 전달된 인자의 타입은 맞지만, 그 값이 적절하지 않을 때
# ValueError가 발생합니다.
# 가장 흔한 예는 숫자로 변환할 수 없는 문자열을 int()나 float() 함수로 변환하려 할 때입니다.

# 예시 상황
text_number = "123"
text_invalid = "hello"

# 올바른 경우
number = int(text_number)
print(f"'{text_number}' -> {number} (타입: {type(number)})")

# 잘못된 경우 - ValueError 발생
# "hello"는 정수로 변환할 수 없는 값입니다.
# 주석을 해제하고 실행해보세요.
# invalid_number = int(text_invalid)
# print(invalid_number)

# 해결 방법:
# 1. try-except 구문을 사용하여 예외를 처리합니다.
user_input = "3.14" # 또는 "world"를 넣어보세요
try:
    # 코드를 먼저 시도하고
    parsed_number = int(user_input)
    print(f"입력값 '{user_input}'은 정수 {parsed_number}로 변환되었습니다.")
except ValueError:
    # 에러가 발생하면 여기를 실행
    print(f"'{user_input}'은 정수로 변환할 수 없습니다.")

# 2. .isdigit() 같은 문자열 메서드로 변환 가능성을 미리 확인합니다.
text = "456"
if text.isdigit():
    print(f"'{text}'는 숫자로 변환 가능: {int(text)}")
else:
    print(f"'{text}'는 숫자 문자열이 아닙니다.")