# IndexError: 범위를 벗어난 인덱스 접근

# 파이썬에서 리스트나 튜플 같은 시퀀스 자료형의 요소에 접근할 때는
# 0부터 시작하는 인덱스 번호를 사용합니다.
# 가지고 있는 요소의 개수를 넘어서는 인덱스에 접근하려고 할 때 IndexError가 발생합니다.

# 예시: 3개의 요소를 가진 리스트 (인덱스는 0, 1, 2)
my_list = [10, 20, 30]

print("리스트의 길이:", len(my_list))
print("마지막 인덱스:", len(my_list) - 1)

# 올바른 접근
print("인덱스 0:", my_list[0])
print("인덱스 2:", my_list[2])

# 잘못된 접근 - IndexError 발생
# 주석을 해제하고 실행해보세요.
# print("인덱스 3:", my_list[3]) # 없는 인덱스에 접근

# 해결 방법:
# 1. 인덱스 범위를 항상 확인합니다.
# 2. for-each 구문을 사용하여 인덱스를 직접 다루지 않고 모든 요소에 접근합니다.
print("\nfor-each 구문으로 안전하게 접근:")
for item in my_list:
    print(item)