# 제목: itertools.permutations로 모든 순열 생성하기
from itertools import permutations

# 순열(Permutation)은 서로 다른 n개에서 r개를 선택하여 '순서대로' 나열하는 경우입니다.
# ('A', 'B')와 ('B', 'A')를 다른 것으로 취급합니다.

items = ['A', 'B', 'C']

# 1. 3개 중 3개를 뽑는 순열 (nPr, n=3, r=3)
p_3_3 = list(permutations(items, 3))
print(f"{items}에서 3개를 뽑는 순열 (결과 수: 3! = 6):")
print(p_3_3)

# 2. 3개 중 2개를 뽑는 순열 (nPr, n=3, r=2)
p_3_2 = list(permutations(items, 2))
print(f"\n{items}에서 2개를 뽑는 순열 (결과 수: 3*2 = 6):")
print(p_3_2)

# 예제: 숫자 리스트로 만들 수 있는 모든 순열
numbers = [1, 2, 3]
num_permutations = list(permutations(numbers))
print(f"\n{numbers}로 만들 수 있는 모든 순열:")
print(num_permutations)