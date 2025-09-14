# 제목: 2차원 리스트(행렬) 기본 순회 및 접근

# 2차원 리스트는 리스트 안에 또 다른 리스트가 들어있는 구조로,
# 행렬이나 게임 맵 등을 표현할 때 자주 사용됩니다.

# 3행 4열의 2차원 리스트
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# 1. 특정 원소에 접근하기
# matrix[행_인덱스][열_인덱스]
element = matrix[1][2] # 1번 행, 2번 열의 원소 (값: 7)
print(f"matrix[1][2]의 값: {element}")

# 2. 2차원 리스트 순회하기 (기본)
# 중첩 for문을 사용하여 각 행(row)을 순회하고,
# 각 행 안의 원소(col)를 다시 순회합니다.
print("\n2차원 리스트 전체 순회:")
for row in matrix:
    for col_item in row:
        print(col_item, end='\t')
    print() # 한 행 출력이 끝나면 줄바꿈

# 3. 인덱스를 이용한 순회
print("\n인덱스를 이용한 순회:")
num_rows = len(matrix)
num_cols = len(matrix[0]) # 첫 번째 행의 길이를 통해 열의 개수를 파악

for r in range(num_rows):
    for c in range(num_cols):
        print(f"({r},{c}): {matrix[r][c]}", end=' | ')
    print()