# TypeError: 지원하지 않는 타입 간의 연산

# 파이썬은 정수는 정수끼리, 문자는 문자끼리 연산하는 등
# 연산에 참여하는 데이터 타입이 서로 맞아야 합니다.
# 예를 들어, 숫자와 문자열을 직접 더하려고 하면 TypeError가 발생합니다.

# 예시 상황
year = 2025
message = "년 새해 복 많이 받으세요!"

# 잘못된 연산 - TypeError 발생
# 정수(int)와 문자열(str)은 '+' 연산을 함께 할 수 없습니다.
# 주석을 해제하고 실행해보세요.
# full_message = year + message
# print(full_message)

# 해결 방법:
# 1. str() 함수를 사용하여 숫자를 문자열로 변환(형 변환)합니다.
full_message_str = str(year) + message
print("str() 사용:", full_message_str)

# 2. f-string을 사용하여 간결하게 문자열을 조합합니다. (권장)
full_message_fstring = f"{year}년 새해 복 많이 받으세요!"
print("f-string 사용:", full_message_fstring)