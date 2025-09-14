# 제목: 논리 연산자 (and, or, not) 활용하기

# 논리 연산자는 여러 개의 조건을 조합하여 더 복잡한 조건을 만들 때 사용합니다.

# and: 두 조건이 '모두' 참(True)일 때만 전체가 참
# or: 두 조건 중 '하나라도' 참(True)이면 전체가 참
# not: 조건의 참/거짓을 뒤집음 (True -> False, False -> True)

age = 25
has_ticket = True

# and 예제: 나이가 20 이상이고, 티켓도 있어야 입장 가능
if age >= 20 and has_ticket == True:
    print("입장 가능합니다.")
else:
    print("입장 불가능합니다.")

money = 3000
has_card = True

# or 예제: 돈이 5000원 이상 있거나, 카드가 있으면 결제 가능
if money >= 5000 or has_card == True:
    print("결제 가능합니다.")
else:
    print("결제 불가능합니다.")

is_raining = False

# not 예제: 비가 오지 않으면
if not is_raining:
    print("우산을 챙기지 않아도 됩니다.")
else:
    print("우산을 챙기세요.")