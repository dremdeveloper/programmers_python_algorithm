# 2차원 리스트: 초기화와 행/열 우선 순회

"""
2차원 리스트는 리스트의 각 요소가 또 다른 리스트로 구성된 형태를 말합니다.
주로 행렬(Matrix)이나 표(Table) 형태의 데이터를 표현할 때 사용됩니다.
초기화 시 '얕은 복사' 문제를 주의해야 하며, 리스트 컴프리헨션을 사용하는 것이 안전합니다.
"""

rows = 3
cols = 4

# 잘못된 2차원 리스트 초기화 방법
# [[0, 0, 0, 0]] 이라는 내부 리스트에 대한 '참조'만 3번 복사(얕은 복사)합니다.
# 따라서 한 행을 바꾸면 모든 행이 함께 변경되는 문제가 발생합니다.
wrong_list = [[0] * cols] * rows
wrong_list[0][0] = 1 # 첫 번째 행의 첫 열을 1로 바꿨지만...
print(f"잘못된 초기화 결과 (모든 행이 바뀜):\n{wrong_list}\n")

# 올바른 2차원 리스트 초기화 방법 (리스트 컴프리헨션)
# 각 행마다 새로운 리스트 [0, 0, 0, 0]을 독립적으로 생성하므로 문제가 없습니다.
correct_list = [[0 for _ in range(cols)] for _ in range(rows)]
correct_list[0][0] = 1
print(f"올바른 초기화 결과:\n{correct_list}\n")

# 2차원 리스트 순회
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 행 우선 순회 (일반적인 순회 방법)
print("행 우선 순회:")
for row in range(len(data)):
    for col in range(len(data[row])):
        print(data[row][col], end=" ")
    print()