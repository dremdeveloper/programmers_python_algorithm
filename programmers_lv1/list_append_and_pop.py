# 제목: 리스트에 원소 추가 및 제거 (append, pop)

my_list = [10, 20, 30]
print(f"초기 리스트: {my_list}")

# 1. .append(value): 리스트의 맨 뒤에 원소를 추가합니다.
my_list.append(40)
print(f".append(40) 후: {my_list}")

my_list.append(50)
print(f".append(50) 후: {my_list}")


# 2. .pop(): 리스트의 원소를 제거하고, 그 제거된 원소를 반환합니다.

# 인덱스를 지정하지 않으면 맨 마지막 원소를 제거합니다.
last_item = my_list.pop()
print(f"\n.pop() 실행 -> 제거된 원소: {last_item}")
print(f"리스트 상태: {my_list}")

# 인덱스를 지정하면 해당 위치의 원소를 제거합니다.
# 인덱스 1 (두 번째 원소) 제거
item_at_index_1 = my_list.pop(1)
print(f"\n.pop(1) 실행 -> 제거된 원소: {item_at_index_1}")
print(f"리스트 상태: {my_list}")