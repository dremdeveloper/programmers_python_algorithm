# 리스트 슬라이싱: 요소 추출, 뒤집기, 간격 조절

"""
슬라이싱(Slicing)은 리스트나 튜플, 문자열 같은 시퀀스 자료형의 일부를
원하는 만큼 잘라내어 새로운 시퀀스를 만드는 기능입니다.
[start:end:step] 형식을 사용하며, 인덱스를 유연하게 조작하여
데이터를 추출하거나 뒤집는 등 다양하게 활용할 수 있습니다.
"""

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"원본 리스트: {nums}\n")

# [start:end] - start 인덱스부터 end-1 인덱스까지 추출
sub_list = nums[2:5]
print(f"nums[2:5]: {sub_list}")

# [start:] - start 인덱스부터 끝까지 추출
from_start = nums[5:]
print(f"nums[5:]: {from_start}")

# [start:end:step] - start부터 end-1까지 step 간격으로 추출
evens = nums[0::2]
print(f"nums[0::2] (짝수): {evens}")

# [::-1] - 리스트를 거꾸로 뒤집기
reversed_list = nums[::-1]
print(f"nums[::-1] (뒤집기): {reversed_list}")