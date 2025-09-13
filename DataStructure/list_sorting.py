# 리스트 정렬: sort()와 sorted()의 차이 및 key 활용법

"""
파이썬에서 리스트를 정렬하는 방법은 크게 두 가지가 있습니다.
1. list.sort(): 리스트 객체 자체의 메서드로, 원본 리스트를 직접 수정합니다 (in-place).
2. sorted(list): 내장 함수로, 원본 리스트는 그대로 두고 정렬된 '새로운' 리스트를 반환합니다.
'key' 매개변수를 사용하면 복잡한 데이터 구조도 원하는 기준으로 정렬할 수 있습니다.
"""

# Case 1: sort() vs sorted()

# sort() 메서드: 원본 리스트를 직접 수정 (반환값은 None)
nums1 = [3, 1, 4, 1, 5, 9, 2]
print(f"sort() 전 원본: {nums1}")
nums1.sort()
print(f"sort() 후 원본: {nums1}\n")

# sorted() 함수: 정렬된 새로운 리스트를 반환 (원본 유지)
nums2 = [3, 1, 4, 1, 5, 9, 2]
print(f"sorted() 전 원본: {nums2}")
sorted_nums = sorted(nums2)
print(f"sorted() 후 원본: {nums2}")
print(f"sorted() 결과: {sorted_nums}\n")

# Case 2: key 매개변수 활용
students = [
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 95)
]

# 점수(튜플의 인덱스 1)를 기준으로 내림차순 정렬
sorted_by_score = sorted(students, key=lambda s: s[1], reverse=True)
print(f"점수 기준 내림차순 정렬: {sorted_by_score}")