# 집합 연산: 교집합, 합집합, 차집합 활용

"""
셋(Set)은 수학의 집합 개념을 그대로 가져와 다양한 집합 연산을 지원합니다.
- 합집합 (Union): 두 집합의 모든 요소를 포함 (A | B)
- 교집합 (Intersection): 두 집합에 공통으로 존재하는 요소 (A & B)
- 차집합 (Difference): 한 집합에는 있지만 다른 집합에는 없는 요소 (A - B)
- 대칭차집합 (Symmetric Difference): 두 집합 중 한쪽에만 속하는 요소 (A ^ B)
"""

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}\n")

# 합집합 (Union)
union = set_a | set_b
print(f"합집합 (A | B): {union}")

# 교집합 (Intersection)
intersection = set_a & set_b
print(f"교집합 (A & B): {intersection}")

# 차집합 (Difference)
difference = set_a - set_b
print(f"차집합 (A - B): {difference}")

# 대칭차집합 (Symmetric Difference)
sym_diff = set_a ^ set_b
print(f"대칭차집합 (A ^ B): {sym_diff}")