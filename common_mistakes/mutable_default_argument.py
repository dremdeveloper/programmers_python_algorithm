# 함정: 가변 객체를 기본 인자로 사용

# 파이썬 함수에서 기본 인자(default argument)는 함수가 정의될 때 딱 한 번만 생성됩니다.
# 만약 이 기본 인자가 리스트나 딕셔너리 같은 '가변(mutable)' 객체라면,
# 함수를 여러 번 호출할 때마다 동일한 객체가 계속 공유되어 예기치 않은 결과를 낳습니다.

# 잘못된 예시:
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

# 함수 호출
list1 = add_item(1)
print(f"첫 번째 호출: {list1}") # 기대: [1] -> 결과: [1] (정상)

list2 = add_item(2)
print(f"두 번째 호출: {list2}") # 기대: [2] -> 결과: [1, 2] (문제 발생!)

list3 = add_item(3)
print(f"세 번째 호출: {list3}") # 기대: [3] -> 결과: [1, 2, 3] (문제 발생!)

# 왜 이런 일이?
# my_list=[]는 함수가 정의될 때 메모리에 단 한번 생성됩니다.
# add_item을 호출할 때마다 my_list 인자를 주지 않으면, 이전에 사용했던 바로 그 리스트가
# 계속해서 재사용되기 때문에 값이 누적됩니다.

print("-" * 20)

# 올바른 해결 방법:
# 기본값으로 None을 사용하고, 함수 내부에서 새로운 리스트를 생성합니다.
def add_item_correct(item, my_list=None):
    if my_list is None:
        my_list = [] # 함수가 호출될 때마다 새로운 빈 리스트가 생성됨
    my_list.append(item)
    return my_list

# 올바른 방법으로 함수 호출
list_a = add_item_correct(1)
print(f"올바른 방법 첫 호출: {list_a}") # 결과: [1]

list_b = add_item_correct(2)
print(f"올바른 방법 두 번째 호출: {list_b}") # 결과: [2] (독립적임)

# 기존 리스트를 전달하는 것도 여전히 가능합니다.
list_c = [10, 20]
add_item_correct(30, list_c)
print(f"기존 리스트 전달: {list_c}") # 결과: [10, 20, 30]