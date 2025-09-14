# 제목: 문자열 인덱싱으로 특정 문자 접근하기

# 문자열도 리스트처럼 각 문자에 0부터 시작하는 인덱스 번호가 매겨져 있습니다.
# 이를 이용해 특정 위치의 문자를 가져올 수 있습니다.

message = "Hello, World!"
print(f"전체 문자열: {message}")

# 첫 번째 문자 (인덱스 0)
first_char = message[0]
print(f"첫 번째 문자: {first_char}")

# 다섯 번째 문자 (인덱스 4)
fifth_char = message[4]
print(f"다섯 번째 문자: {fifth_char}")

# 마지막 문자 (인덱스 -1)
last_char = message[-1]
print(f"마지막 문자: {last_char}")

# 주의! 문자열은 리스트와 달리 특정 위치의 문자를 바꿀 수 없습니다. (immutable)
# message[0] = 'J' # 이 코드는 TypeError를 발생시킵니다.