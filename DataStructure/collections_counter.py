# collections.Counter: 해시 가능한 객체의 개수 세기

"""
Counter는 collections 모듈에 포함된 클래스로, 딕셔너리의 하위 클래스입니다.
리스트나 문자열 등 순회 가능한 객체 내의 각 요소가 몇 번씩 나타나는지를
딕셔너리 형태로 반환해주는 편리한 도구입니다.
"""
from collections import Counter

# 리스트에 있는 각 항목의 개수를 세기
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = Counter(words)

print(f"원본 리스트: {words}")
print(f"Counter 결과: {word_counts}\n")

# 특정 항목의 개수 조회
print(f"apple의 개수: {word_counts['apple']}")
# 존재하지 않는 키를 조회해도 KeyError 없이 0을 반환
print(f"grape의 개수: {word_counts['grape']}\n")

# 가장 빈번하게 나타나는 항목 조회
# .most_common(n) - 빈도수 상위 n개의 항목을 리스트로 반환
top_two = word_counts.most_common(2)
print(f"가장 많이 나온 2개: {top_two}")