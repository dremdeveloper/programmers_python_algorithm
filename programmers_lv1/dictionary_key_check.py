# 제목: if key in dictionary로 딕셔너리 키 존재 여부 확인

# 딕셔너리에서 존재하지 않는 키로 값을 조회하려고 하면 KeyError가 발생합니다.
# 이를 방지하기 위해 'in' 연산자로 키가 존재하는지 미리 확인하는 것이 안전합니다.

inventory = {
    "apple": 5,
    "banana": 10,
    "orange": 0
}

item_to_check = "banana"

# 'in'을 사용하여 키 존재 여부 확인
if item_to_check in inventory:
    print(f"{item_to_check}의 재고는 {inventory[item_to_check]}개 입니다.")
else:
    print(f"{item_to_check}은(는) 재고 목록에 없습니다.")

item_to_check = "grape"
if item_to_check in inventory:
    print(f"{item_to_check}의 재고는 {inventory[item_to_check]}개 입니다.")
else:
    print(f"{item_to_check}은(는) 재고 목록에 없습니다.")

# 'not in'도 사용할 수 있습니다.
if "apple" not in inventory:
    print("사과가 없습니다.")
else:
    print("사과가 있습니다.")