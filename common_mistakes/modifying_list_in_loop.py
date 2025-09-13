# 예측 불가능한 결과: 반복 중 리스트 수정

# for 문으로 리스트를 순회하는 도중에 해당 리스트의 요소를 삭제하거나 추가하면
# 반복 순서가 꼬여서 예측하지 못한 결과를 낳거나 일부 요소를 건너뛰게 됩니다.
# 이는 for문이 내부적으로 인덱스를 기준으로 순회하기 때문입니다.

# 예시: 리스트에서 짝수 제거하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"원본 리스트: {numbers}")

# 잘못된 방법
# for number in numbers:
#     if number % 2 == 0:
#         numbers.remove(number)
# print(f"잘못된 방법으로 수정 후: {numbers}")
# 결과: [1, 3, 5, 7, 9, 10] -> 4, 6, 8이 제거될 때 다음 요소(5, 7, 9)를 건너뜀

# 왜 이런 일이 발생할까?
# 1. number가 2일 때: 2를 제거. 리스트는 [1, 3, 4, 5, ...]가 됨. 다음 차례는 인덱스 2번인 '4'가 됨. '3'은 건너뛰게 됨.
# 2. number가 4일 때: 4를 제거. 리스트는 [1, 3, 5, 6, ...]가 됨. 다음 차례는 인덱스 3번인 '6'이 됨. '5'는 건너뛰게 됨.
# 이런 식으로 요소를 제거할 때마다 인덱스가 재조정되어 문제를 일으킵니다.

# 해결 방법 1: 새로운 리스트 만들기 (가장 간단하고 안전함)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for number in numbers:
    if number % 2 != 0: # 홀수만 새로운 리스트에 추가
        result.append(number)
print(f"해결1 (새 리스트): {result}")

# 해결 방법 2: 리스트 컴프리헨션 사용 (더 파이써닉함)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_comp = [number for number in numbers if number % 2 != 0]
print(f"해결2 (컴프리헨션): {result_comp}")

# 해결 방법 3: 원본 리스트의 복사본을 순회하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers[:]: # [:]는 리스트 전체를 얕은 복사(shallow copy)
    if number % 2 == 0:
        numbers.remove(number)
print(f"해결3 (복사본 순회): {numbers}")