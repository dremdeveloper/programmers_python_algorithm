# 의도치 않은 동작: global 키워드 누락

# 파이썬에서 함수 내에서 변수에 값을 할당하면, 기본적으로 그 변수는
# '지역 변수(local variable)'로 취급됩니다.
# 만약 함수 바깥에 있는 '전역 변수(global variable)'의 값을 함수 내에서
# 직접 수정(재할당)하고 싶다면, 반드시 'global' 키워드를 사용해야 합니다.
# 'global' 키워드 없이 전역 변수와 같은 이름의 변수에 값을 할당하면,
# 전역 변수를 수정하는 것이 아니라, 이름만 같은 새로운 지역 변수가 생성됩니다.

# 예시
counter = 0 # 전역 변수

def increment_wrong():
    # 이 counter는 함수 내의 새로운 지역 변수로 인식됩니다.
    # 전역 변수 counter를 읽어와서 1을 더한 값을 새로운 지역 변수 counter에 할당하는 것과 같습니다.
    # UnboundLocalError가 발생할 수 있음 (주석 참고)
    # counter = counter + 1 # 이 코드는 사실상 counter(지역) = counter(전역?) + 1 이라 모호함
    print(f"잘못된 함수 내 counter: (에러 발생 가능)")

def increment_correct():
    global counter # 'counter'는 이제부터 전역 변수를 가리키겠다고 선언
    counter = counter + 1
    print(f"올바른 함수 내 counter: {counter}")


print(f"초기 counter 값: {counter}")

# 올바른 함수 호출
increment_correct()
print(f"올바른 함수 호출 후 counter: {counter}") # 전역 변수 값이 변경됨

increment_correct()
print(f"올바른 함수 호출 후 counter: {counter}") # 전역 변수 값이 또 변경됨

print("-" * 20)

# 잘못된 함수를 호출하면 어떻게 될까?
# 주석을 해제하고 실행하면 UnboundLocalError가 발생합니다.
# counter = counter + 1 에서, 할당(=)이 있기 때문에 파이썬은 counter를 지역 변수로 판단합니다.
# 하지만 값을 할당하기도 전에 우변의 counter(지역 변수)를 읽으려고 하니 에러가 발생합니다.
# try:
#     increment_wrong()
# except UnboundLocalError as e:
#     print(f"잘못된 함수 호출 시 에러: {e}")

# 정리:
# - 함수 내에서 전역 변수를 '읽기만' 하는 것은 global 선언 없이 가능합니다.
# - 함수 내에서 전역 변수의 값을 '수정(재할당)'하려면 반드시 global 키워드를 써야 합니다.
# - 단, 전역 변수를 남용하는 것은 코드의 흐름을 추적하기 어렵게 만들므로,
#   가급적 함수의 인자와 반환값을 통해 데이터를 주고받는 것이 좋습니다.