# 제목: zip 함수로 여러 리스트 동시에 순회하기

# zip() 함수는 여러 개의 리스트를 같은 인덱끼리 묶어 튜플로 반환합니다.

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Seoul']

# 1. 두 리스트를 묶어 딕셔너리 만들기
profile_dict = {}
for key, value in zip(keys, values):
    profile_dict[key] = value

print(f"zip으로 만든 딕셔너리: {profile_dict}")

# 파이썬다운 한 줄 코드
profile_dict_comp = dict(zip(keys, values))
print(f"한 줄로 만든 딕셔너리: {profile_dict_comp}")


# 2. 2차원 리스트의 행과 열 바꾸기 (전치 행렬)
matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
# *matrix는 리스트의 각 행을 zip의 개별 인자로 풀어주는 역할
# zip([1,4,7], [2,5,8], [3,6,9])
transposed = list(zip(*matrix))
print(f"\n전치 행렬: {transposed}")