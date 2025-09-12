# set_operations.py
# 제목: set 자료구조의 집합 연산 (합집합, 교집합, 차집합)

# 두 개의 집합 정의
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}\n")

# --- 1. 합집합 (Union) ---
# 두 집합의 모든 원소를 포함하는 집합 (중복 제외)
union_operator = set_a | set_b
union_method = set_a.union(set_b)
print(f"합집합 ( | ): {union_operator}")
print(f"합집합 (.union()): {union_method}\n")


# --- 2. 교집합 (Intersection) ---
# 두 집합에 공통으로 존재하는 원소들의 집합
intersection_operator = set_a & set_b
intersection_method = set_a.intersection(set_b)
print(f"교집합 ( & ): {intersection_operator}")
print(f"교집합 (.intersection()): {intersection_method}\n")


# --- 3. 차집합 (Difference) ---
# 첫 번째 집합에는 있지만 두 번째 집합에는 없는 원소들의 집합
difference_operator = set_a - set_b
difference_method = set_a.difference(set_b)
print(f"차집합 (A - B): {difference_operator}")
print(f"차집합 (A.difference(B)): {difference_method}\n")

difference_operator_2 = set_b - set_a
print(f"차집합 (B - A): {difference_operator_2}")