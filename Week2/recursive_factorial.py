# recursive_factorial.py
# 제목: 재귀 함수를 통한 팩토리얼(Factorial) 계산 (콜 스택)

def factorial(n):
    """
    재귀를 이용하여 n! (n 팩토리얼)을 계산합니다.
    n * (n-1) * ... * 2 * 1
    """
    # 베이스 케이스(Base Case): 재귀 호출을 멈추는 조건
    if n == 0 or n == 1:
        print(f"factorial(1) -> 1 반환")
        return 1
    # 재귀 단계(Recursive Step): 자기 자신을 다시 호출하는 부분
    else:
        print(f"factorial({n}) 호출: {n} * factorial({n-1})")
        return n * factorial(n - 1)

# 재귀 함수가 동작하는 과정은 내부적으로 '콜 스택(Call Stack)'을 사용합니다.
# factorial(4)를 호출하면 다음과 같이 콜 스택에 함수가 쌓입니다.
#
# 1. factorial(4) 호출 -> 스택: [factorial(4)]
# 2. factorial(3) 호출 -> 스택: [factorial(4), factorial(3)]
# 3. factorial(2) 호출 -> 스택: [factorial(4), factorial(3), factorial(2)]
# 4. factorial(1) 호출 -> 스택: [factorial(4), factorial(3), factorial(2), factorial(1)]
#
# factorial(1)이 1을 반환하면, 스택에서 하나씩 빠져나오며 계산이 완료됩니다.
# 1. factorial(1)이 1 반환, 스택에서 pop
# 2. factorial(2)는 2 * 1 = 2 반환, 스택에서 pop
# 3. factorial(3)은 3 * 2 = 6 반환, 스택에서 pop
# 4. factorial(4)는 4 * 6 = 24 반환, 스택에서 pop

num = 4
print(f"{num}의 팩토리얼 계산 과정:")
result = factorial(num)
print(f"\n최종 결과: {num}! = {result}")