# 제목: collections.Counter로 간단하게 개수 세기
from collections import Counter

# for문과 딕셔너리로 직접 개수를 세는 것보다 훨씬 간결하고 효율적입니다.
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

# Counter 객체 생성
p_counter = Counter(participant)
c_counter = Counter(completion)

print(f"참가자 카운트: {p_counter}")
print(f"완주자 카운트: {c_counter}")

# Counter 객체끼리 뺄셈 연산 가능
result = p_counter - c_counter
print(f"참가자 - 완주자: {result}")

# 딕셔너리의 키 리스트를 통해 결과 추출
answer = list(result.keys())[0]
print(f"완주하지 못한 선수: {answer}")