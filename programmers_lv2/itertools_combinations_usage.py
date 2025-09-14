# 제목: itertools.combinations로 모든 조합 생성하기
from itertools import combinations

# 조합(Combination)은 서로 다른 n개에서 r개를 '순서에 상관없이' 뽑는 경우입니다.
# ('A', 'B')와 ('B', 'A')를 같은 것으로 취급합니다.

items = ['A', 'B', 'C', 'D']

# 1. 4개 중 2개를 뽑는 조합 (nCr, n=4, r=2)
c_4_2 = list(combinations(items, 2))
print(f"{items}에서 2개를 뽑는 조합 (결과 수: (4*3)/(2*1) = 6):")
print(c_4_2)

# 2. 4개 중 3개를 뽑는 조합 (nCr, n=4, r=3)
c_4_3 = list(combinations(items, 3))
print(f"\n{items}에서 3개를 뽑는 조합 (결과 수: 4):")
print(c_4_3)

# 예제: 로또 번호처럼 1~5번 중 3개 뽑기
numbers = [1, 2, 3, 4, 5]
num_combinations = list(combinations(numbers, 3))
print(f"\n{numbers}에서 3개를 뽑는 모든 조합:")
print(num_combinations)