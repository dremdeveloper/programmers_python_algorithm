# 제목: collections.Counter로 리스트의 원소 개수 세기
from collections import Counter

# Counter는 리스트나 문자열 같은 데이터 안에 각 원소가 몇 번씩
# 등장하는지를 세어 딕셔너리 형태로 반환하는 강력한 도구입니다.

my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# 1. Counter 객체 생성
counts = Counter(my_list)
print(f"리스트 원소 개수 세기: {counts}")

# 2. 특정 원소의 개수 확인
apple_count = counts['apple']
print(f"사과(apple)의 개수: {apple_count}")

# 존재하지 않는 원소는 0을 반환 (KeyError 없음)
grape_count = counts['grape']
print(f"포도(grape)의 개수: {grape_count}")


# 3. 가장 많이 등장한 원소 찾기
# .most_common(n) 메소드는 가장 빈도 높은 n개 아이템을 (원소, 개수) 튜플의 리스트로 반환
most_common_item = counts.most_common(1)
print(f"가장 흔한 아이템: {most_common_item}")
print(f"가장 흔한 아이템의 이름: {most_common_item[0][0]}")