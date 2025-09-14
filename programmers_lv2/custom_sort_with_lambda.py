# 제목: lambda를 활용한 사용자 정의 정렬 (다중 조건)

# sorted() 함수의 key 인자에 lambda 함수를 사용하면
# 복잡한 데이터를 원하는 기준으로 정렬할 수 있습니다.

students = [
    ('Alice', 90, 1995),
    ('Bob', 88, 1994),
    ('Charlie', 90, 1996),
]

print(f"원본 데이터: {students}")

# 1. 점수(인덱스 1) 기준으로 내림차순 정렬
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(f"\n점수 기준 내림차순: {sorted_by_score}")

# 2. 다중 조건 정렬
# 1순위: 점수(인덱스 1) 내림차순, 2순위: 출생년도(인덱스 2) 오름차순
# key에 튜플을 반환하면, 튜플의 앞 요소부터 순서대로 정렬 기준으로 사용됩니다.
# 점수는 내림차순이므로 -를 붙여줍니다.
sorted_multiple = sorted(students, key=lambda x: (-x[1], x[2]))
print(f"\n다중 조건 정렬: {sorted_multiple}")