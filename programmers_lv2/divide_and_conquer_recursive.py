# 제목: 재귀 함수를 이용한 분할 정복 기본 구조

# 분할 정복(Divide and Conquer)은 큰 문제를 작은 여러 개의 하위 문제로 나누어(분할)
# 각각을 해결한 후, 그 결과를 합쳐(정복) 원래 문제의 답을 구하는 전략입니다.
# 재귀 함수는 이 구조를 표현하기에 매우 적합합니다.

# 예제: 리스트의 모든 원소 합 구하기 (분할 정복 방식)
def recursive_sum(arr):
    # 1. 탈출 조건 (Base Case): 더 이상 분할할 수 없는 가장 작은 문제
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    # 2. 분할 (Divide): 문제를 절반으로 나눔
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 3. 정복 (Conquer): 각 하위 문제에 대해 재귀적으로 함수를 호출하고, 결과를 합침
    return recursive_sum(left_half) + recursive_sum(right_half)

# 테스트
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = recursive_sum(my_list)
print(f"리스트 {my_list}의 합: {total}")
# 물론, 실제로는 내장 함수 sum()을 사용하는 것이 훨씬 효율적입니다.
# 이 예제는 분할 정복의 '구조'를 이해하기 위함입니다.