# 제목: set을 이용한 중복 원소 제거

# 집합(set) 자료형은 중복된 원소를 허용하지 않는 특징이 있습니다.
# 이를 이용하면 리스트에서 중복된 원소를 매우 간단하게 제거할 수 있습니다.

# 중복된 원소가 있는 리스트
my_list = [1, 2, 2, 3, 4, 4, 4, 5, 1]
print(f"원본 리스트: {my_list}")

# 1. 리스트를 set으로 변환하여 중복 제거
# set으로 변환하는 순간 중복이 사라지고, 순서도 보장되지 않습니다.
my_set = set(my_list)
print(f"Set으로 변환: {my_set}")

# 2. set을 다시 list로 변환
unique_list = list(my_set)
print(f"중복 제거된 리스트: {unique_list}")

# 3. 한 줄로 처리하기
unique_list_oneline = list(set(my_list))
print(f"한 줄로 처리: {unique_list_oneline}")

# 참고: 원래의 순서를 유지하면서 중복을 제거하고 싶다면
# 다른 방법(예: for문과 if문 사용)을 고려해야 합니다.