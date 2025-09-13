# 계산 오류: 정수 나눗셈(//)과 실수 나눗셈(/) 혼동

# 파이썬 3에서는 나눗셈 연산자가 두 종류가 있으며, 각각의 역할이 다릅니다.
# 이를 혼동하면 계산 결과에서 소수점 부분이 사라지는 등 의도치 않은 결과가 나올 수 있습니다.

# / (실수 나눗셈, True Division):
# - 우리가 일반적으로 생각하는 나눗셈입니다.
# - 나누어 떨어지더라도 결과는 항상 실수(float) 타입이 됩니다.

# // (정수 나눗셈, Floor Division):
# - 나눗셈을 한 결과에서 소수점 이하를 '버리는' 연산입니다. (내림)
# - 연산에 참여하는 수가 모두 정수이면 결과도 정수, 하나라도 실수이면 결과는 실수가 됩니다.
#   (e.g., 7.0 // 2 = 3.0)

# 예시
a = 7
b = 2

# 실수 나눗셈 (/)
result_float = a / b
print(f"{a} / {b} = {result_float} (타입: {type(result_float)})")

# 정수 나눗셈 (//)
result_int = a // b
print(f"{a} // {b} = {result_int} (타입: {type(result_int)})")

print("-" * 20)

# 흔히 발생하는 실수: 평균 계산
scores = [90, 85, 92]
count = len(scores)
total = sum(scores)

# 실수 나눗셈을 해야 정확한 평균이 나옴
average_correct = total / count
print(f"올바른 평균 계산: {total} / {count} = {average_correct}")

# 정수 나눗셈을 사용하면 소수점 이하를 잃게 됨
average_wrong = total // count
print(f"잘못된 평균 계산: {total} // {count} = {average_wrong}")


# 참고: Python 2 에서는 / 가 정수끼리의 연산에서 // 처럼 동작했기 때문에
# Python 3 로 넘어오면서 혼동하는 경우가 많았습니다. 현재는 / 와 // 의 역할이 명확히 구분됩니다.