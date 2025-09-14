# 제목: 문자열 split()으로 특정 기준에 따라 나누기

# .split()은 문자열을 특정 구분자(delimiter)를 기준으로 잘라서
# 여러 개의 문자열이 담긴 리스트로 만들어주는 매우 유용한 메소드입니다.

# 1. 공백을 기준으로 나누기
# 구분자를 지정하지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 자릅니다.
sentence = "Life is too short"
words = sentence.split()
print(f"'{sentence}'.split() -> {words}")

# 2. 특정 문자를 기준으로 나누기
date_str = "2025-09-14"
date_parts = date_str.split('-')
print(f"'{date_str}'.split('-') -> {date_parts}")

# 코딩 테스트에서 자주 사용되는 입력 처리 방식
# "10 20 30"과 같은 입력을 받아 숫자 리스트로 변환하기
input_str = "10 20 30 40 50"
str_numbers = input_str.split() # -> ['10', '20', '30', '40', '50']
int_numbers = [int(n) for n in str_numbers] # 리스트 컴프리헨션을 이용한 형 변환
print(f"'{input_str}' -> {int_numbers}")