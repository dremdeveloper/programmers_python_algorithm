# 값 분실: None을 반환하는 제자리(in-place) 메서드

# 파이썬의 일부 메서드는 객체를 직접 수정하며(in-place),
# 그 과정에서 아무것도 반환하지 않습니다 (즉, None을 반환).
# 대표적인 예가 리스트의 .sort()나 .reverse() 메서드입니다.
# 많은 초보자들이 이 메서드들이 정렬된 '새로운' 리스트를 반환할 것이라 착각하고
# 그 결과를 다시 변수에 할당하여 기존 리스트 데이터를 잃어버리는 실수를 합니다.

# 예시
numbers = [3, 1, 4, 1, 5, 9, 2]
print(f"원본 리스트: {numbers}")

# 잘못된 방법
# .sort()는 numbers 리스트 자체를 정렬하고, 반환값은 None입니다.
# sorted_numbers 변수에는 None이 할당됩니다.
sorted_numbers = numbers.sort()

print(f"\n.sort() 메서드의 반환값: {sorted_numbers}") # None
print(f"numbers 변수는 어떻게 됐을까?: {numbers}") # 원본이 직접 정렬됨

# 이 시점에서 원래의 numbers 리스트는 정렬된 상태로 바뀌었고,
# 정렬된 결과를 담으려던 sorted_numbers 변수는 None이 되어
# 데이터를 의도치 않게 잃어버린 셈이 됩니다.

print("-" * 20)

# 올바른 방법 1: 제자리(in-place) 메서드는 그냥 호출만 한다.
numbers_a = [3, 1, 4, 1, 5, 9, 2]
print(f"방법1 원본: {numbers_a}")
numbers_a.sort() # 반환값을 받지 않고, 그냥 호출하여 원본을 변경
print(f"방법1 결과: {numbers_a}")

# 올바른 방법 2: sorted() 내장 함수를 사용한다.
# sorted() 함수는 원본 리스트는 그대로 두고, 정렬된 '새로운' 리스트를 반환합니다.
# 원본을 유지하면서 정렬된 결과를 얻고 싶을 때 사용합니다.
numbers_b = [3, 1, 4, 1, 5, 9, 2]
print(f"\n방법2 원본: {numbers_b}")
new_sorted_list = sorted(numbers_b) # 새로운 리스트를 반환
print(f"방법2 원본 유지 확인: {numbers_b}")
print(f"방법2 결과 (새 변수): {new_sorted_list}")