# 제목: sorted() 함수와 list.sort() 메소드를 이용한 기본 정렬

# 파이썬에서 리스트를 정렬하는 대표적인 두 가지 방법입니다.

numbers = [3, 1, 4, 1, 5, 9, 2]
print(f"원본 리스트: {numbers}")

# 1. sorted() 내장 함수
# - 원본 리스트는 그대로 두고, 정렬된 '새로운' 리스트를 반환합니다.
# - 어떤 종류의 반복 가능한 객체(리스트, 튜플 등)에도 사용할 수 있습니다.
sorted_list = sorted(numbers)
print(f"\nsorted() 함수 사용 결과: {sorted_list}")
print(f"sorted() 사용 후 원본 리스트: {numbers}") # 원본은 변하지 않음

# 내림차순 정렬
reverse_sorted_list = sorted(numbers, reverse=True)
print(f"sorted() 내림차순 결과: {reverse_sorted_list}")


# 2. list.sort() 메소드
# - 리스트 객체에만 사용할 수 있는 메소드입니다.
# - 원본 리스트 자체를 '직접' 수정하며, 아무것도 반환하지 않습니다 (None을 반환).
print("\n--- list.sort() 메소드 ---")
numbers.sort() # 원본 리스트를 오름차순으로 정렬
print(f".sort() 메소드 사용 후 원본 리스트: {numbers}")

numbers.sort(reverse=True) # 원본 리스트를 내림차순으로 정렬
print(f".sort(reverse=True) 사용 후: {numbers}")