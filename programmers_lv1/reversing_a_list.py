# 제목: 리스트 뒤집기 ([::-1] 슬라이싱, reversed())

numbers = [1, 2, 3, 4, 5]
print(f"원본 리스트: {numbers}")

# 방법 1: 슬라이싱 사용 [::-1]
# - 가장 간편하고 널리 쓰이는 방법입니다.
# - 원본 리스트는 그대로 두고, 뒤집힌 '새로운' 리스트를 반환합니다.
reversed_by_slicing = numbers[::-1]
print(f"\n슬라이싱 [::-1] 결과: {reversed_by_slicing}")
print(f"슬라이싱 후 원본 리스트: {numbers}")


# 방법 2: reversed() 내장 함수
# - reversed() 함수는 뒤집힌 순서로 원소를 반환하는 '이터레이터'를 만듭니다.
# - list() 함수를 이용해 다시 리스트로 만들어주어야 합니다.
# - 원본 리스트는 그대로 둡니다.
reversed_iterator = reversed(numbers)
reversed_by_function = list(reversed_iterator)
print(f"\nreversed() 함수 결과: {reversed_by_function}")
print(f"reversed() 사용 후 원본 리스트: {numbers}")


# 방법 3: list.reverse() 메소드 (참고)
# - 원본 리스트 자체를 '직접' 뒤집습니다.
# - 아무것도 반환하지 않습니다 (None을 반환).
print("\n--- list.reverse() 메소드 ---")
numbers.reverse()
print(f".reverse() 메소드 사용 후 원본 리스트: {numbers}")