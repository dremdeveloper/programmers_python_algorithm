# 논리 오류: and, or 단축 평가(short-circuit) 오해

# 파이썬의 'and'와 'or' 논리 연산자는 '단축 평가'라는 특징을 가집니다.
# 이는 전체 식의 결과가 확정되는 순간, 더 이상 뒤의 표현식을 평가(실행)하지 않고
# 바로 결과를 반환하는 동작 방식입니다.
# 이 특징을 모르고 'and'나 'or'의 양쪽에 항상 실행되리라 기대하는 코드를 넣으면
# 의도치 않게 일부 코드가 실행되지 않는 논리적 오류를 겪을 수 있습니다.

# 'and'의 단축 평가:
# - 'A and B' 에서 A가 False로 판별되면, 전체 결과는 무조건 False입니다.
# - 따라서 B는 아예 평가(실행)되지 않습니다.

# 'or'의 단축 평가:
# - 'A or B' 에서 A가 True로 판별되면, 전체 결과는 무조건 True입니다.
# - 따라서 B는 아예 평가(실행)되지 않습니다.


# 예시 함수
def is_positive(n):
    print(f"is_positive({n}) 함수 실행")
    return n > 0

def is_even(n):
    print(f"is_even({n}) 함수 실행")
    return n % 2 == 0

print("--- 'and' 단축 평가 예시 ---")
num = -10
# is_positive(-10)이 False이므로, 뒤의 is_even(-10)은 실행되지 않습니다.
if is_positive(num) and is_even(num):
    print(f"{num}은 양수이면서 짝수입니다.")
else:
    print(f"{num}은 양수인 짝수가 아닙니다.")


print("\n--- 'or' 단축 평가 예시 ---")
num = 5
# is_positive(5)가 True이므로, 뒤의 is_even(5)는 실행되지 않습니다.
if is_positive(num) or is_even(num):
    print(f"{num}은 양수이거나 짝수입니다.")
else:
    print(f"{num}은 양수도 짝수도 아닙니다.")


# 이 특징을 유용하게 사용하는 경우:
# - 에러 방지: divisor가 0일 때 나누는 것을 방지
print("\n--- 단축 평가의 유용한 활용 ---")
divisor = 0
value = 100

# divisor != 0 이 False 이므로, 뒤의 (value / divisor) > 1 코드는 실행되지 않아
# ZeroDivisionError를 피할 수 있습니다.
if divisor != 0 and (value / divisor) > 1:
    print("나눗셈 결과가 1보다 큽니다.")
else:
    print("나눌 수 없거나, 결과가 1보다 작거나 같습니다.")