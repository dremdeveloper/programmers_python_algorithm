# 제목: 2차원 배열(리스트) 90도 회전시키기

# 2차원 배열을 90도 회전하는 것은 이미지 처리 등에서 자주 사용되는 기술입니다.
# 가장 일반적인 방법은 '전치(행과 열 바꾸기) 후 행별로 뒤집기' 입니다.

def rotate_90(matrix):
    n = len(matrix) # 행 길이
    m = len(matrix[0]) # 열 길이
    
    # 1. 전치 행렬 만들기
    transposed = [[0] * n for _ in range(m)]
    for r in range(n):
        for c in range(m):
            transposed[c][r] = matrix[r][c]
            
    # 2. 각 행을 뒤집기
    rotated = [row[::-1] for row in transposed]
    
    return rotated

# 더 파이썬다운 방법 (zip 활용)
def rotate_90_pythonic(matrix):
    # 1. zip(*matrix)로 행과 열을 바꿈 (전치)
    # 2. 각 행(튜플)을 뒤집고 리스트로 변환
    rotated = [list(reversed(row)) for row in zip(*matrix)]
    return rotated


# 테스트
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("원본 행렬:")
for row in mat: print(row)

rotated_mat = rotate_90_pythonic(mat)
print("\n90도 회전된 행렬:")
for row in rotated_mat: print(row)