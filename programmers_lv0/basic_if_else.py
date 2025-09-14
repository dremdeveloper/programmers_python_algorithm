# 제목: if-else를 이용한 기초 조건 분기

# if-else 구문은 특정 조건이 참(True)인지 거짓(False)인지에 따라
# 다른 코드를 실행하게 만드는 제어문입니다.

temperature = 30

# "만약 온도가 25도보다 높으면"
if temperature > 25:
    # 조건이 참(True)일 때 이 블록이 실행됩니다.
    print("날씨가 덥습니다. 반팔을 입으세요.")
# "그렇지 않으면"
else:
    # 조건이 거짓(False)일 때 이 블록이 실행됩니다.
    print("날씨가 덥지 않습니다. 긴팔을 입으세요.")

money = 5000
price = 6000

if money >= price:
    print("물건을 구매했습니다.")
else:
    print("돈이 부족합니다.")