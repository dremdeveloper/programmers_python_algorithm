# 제목: 해시(딕셔너리)를 이용한 데이터 매핑 및 조회

# 딕셔너리(해시)의 가장 큰 장점은 키를 통해 값을 매우 빠르게(O(1)) 조회할 수 있다는 점입니다.
# ID-이름, 전화번호-주소 등 데이터를 짝지어 관리할 때 유용합니다.

# 전화번호(key)와 이름(value) 매핑
phone_book = {
    "010-1234-5678": "Alice",
    "010-9876-5432": "Bob",
    "010-1111-2222": "Charlie"
}

# 1. 특정 키로 값 조회하기
phone_number = "010-9876-5432"
name = phone_book.get(phone_number, "알 수 없음") # .get()은 키가 없어도 에러 대신 기본값 반환
print(f"전화번호 {phone_number}의 주인은 {name}입니다.")


# 2. 데이터 업데이트 및 추가
phone_book["010-3333-4444"] = "David" # 새로운 데이터 추가
phone_book["010-1234-5678"] = "Alice Kim" # 기존 데이터 업데이트

print("\n업데이트된 전화번호부:")
for phone, name in phone_book.items():
    print(f"{phone}: {name}")