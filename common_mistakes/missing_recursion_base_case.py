# RecursionError: 재귀 탈출 조건 누락

# 재귀 함수는 자기 자신을 다시 호출하는 함수입니다.
# 재귀 함수를 만들 때 가장 중요한 것은 '탈출 조건(base case)'을 명시하는 것입니다.
# 탈출 조건이 없거나 잘못되면 함수가 무한히 자기 자신을 호출하다가,
# 파이썬이 정해놓은 최대 재귀 깊이(maximum recursion depth)를 초과하여
# RecursionError가 발생합니다.

# 예시: 1부터 n까지 더하는 재귀 함수
def recursive_sum(n):
    # 탈출 조건: n이 1이면 더 이상 재귀 호출을 하지 않고 1을 반환한다.
    if n == 1:
        return 1
    # 재귀 호출: n과 (n-1까지의 합)을 더한다.
    return n + recursive_sum(n - 1)

result = recursive_sum(5) # 5 + 4 + 3 + 2 + 1
print(f"올바른 재귀 함수 결과 (n=5): {result}")

# 잘못된 예시: 탈출 조건이 없는 경우
def infinite_recursion(n):
    # 탈출 조건이 없어서 무한히 자기 자신을 호출하게 된다.
    print(f"현재 n = {n}")
    return n + infinite_recursion(n - 1)

# 주석을 해제하고 실행하면 RecursionError가 발생합니다.
# 시스템에 따라 몇 초간 실행되다가 에러 메시지와 함께 멈춥니다.
# try:
#     infinite_recursion(5)
# except RecursionError as e:
#     print(f"\n에러 발생: {e}")


# 해결 방법:
# - 재귀 함수를 설계할 때 가장 먼저 "언제 멈출 것인가?" 즉, 탈출 조건을 정의해야 합니다.
# - 재귀 호출을 할 때마다 탈출 조건에 점점 가까워지는 방향으로 인자가 변경되어야 합니다.
#   (위 예시에서는 n이 1씩 줄어들어 결국 1이 됨)