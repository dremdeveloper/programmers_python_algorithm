# 제목: sum(), min(), max(), len() 등 기본 내장 함수 활용

# 파이썬은 리스트와 같은 데이터 그룹을 다루는 데 유용한 여러 내장 함수를 제공합니다.

scores = [90, 85, 77, 95, 100]
print(f"점수 리스트: {scores}")

# 1. sum(): 리스트의 모든 원소의 합계
total_score = sum(scores)
print(f"총점: {total_score}")

# 2. min(): 리스트의 원소 중 최솟값
min_score = min(scores)
print(f"최저 점수: {min_score}")

# 3. max(): 리스트의 원소 중 최댓값
max_score = max(scores)
print(f"최고 점수: {max_score}")

# 4. len(): 리스트의 원소 개수 (길이)
num_students = len(scores)
print(f"학생 수: {num_students}")

# 응용: 평균 점수 계산하기
average_score = total_score / num_students
print(f"평균 점수: {average_score}")