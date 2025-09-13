# TypeError: input() 결과 형 변환 누락

# input() 함수는 사용자로부터 키보드 입력을 받는 편리한 기능을 제공합니다.
# 하지만 중요한 점은, input() 함수는 사용자가 무엇을 입력하든
# 그 결과를 항상 '문자열(string)' 타입으로 반환한다는 것입니다.
# 만약 입력받은 값을 숫자처럼 사용해 계산하려고 하면,
# 문자열과 숫자를 연산하려는 시도가 되어 TypeError가 발생합니다.

# 예시: 태어난 연도를 입력받아 나이 계산하기
# current_year = 2025 # 예시를 위해 현재 연도 고정

# 잘못된 경우
# birth_year_str = input("태어난 연도를 입력하세요: ")
# age_wrong = current_year - birth_year_str # 정수 - 문자열 -> TypeError!

# print(f"당신은 {birth_year_str}년에 태어났군요.")
# 주석을 해제하고 실행해보세요
# try:
#     age_wrong = current_year - birth_year_str
#     print(f"나이: {age_wrong}")
# except TypeError as e:
#     print(f"계산 중 에러 발생: {e}")
#     print(f"입력받은 값의 타입: {type(birth_year_str)}")


# 해결 방법:
# input()으로 받은 문자열을 int()나 float() 같은 함수를 사용해
# 원하는 숫자 타입으로 명시적으로 변환(type casting)해주어야 합니다.
print("-" * 20)

current_year = 2025
print("--- 올바른 방법 ---")
birth_year_input = input("태어난 연도를 입력하세요: ")

try:
    # 입력받은 문자열을 정수(int)로 변환
    birth_year = int(birth_year_input)
    age_correct = current_year - birth_year
    print(f"당신의 나이는 약 {age_correct}세 입니다.")
except ValueError:
    # 사용자가 숫자가 아닌 값을 입력했을 경우에 대한 예외 처리
    print(f"'{birth_year_input}'은 유효한 연도가 아닙니다. 숫자를 입력해주세요.")