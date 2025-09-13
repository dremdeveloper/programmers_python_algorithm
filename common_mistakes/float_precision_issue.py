# 정밀도 문제: 부동 소수점 연산 오차

# 컴퓨터는 내부적으로 숫자를 이진수(0과 1)로 표현합니다.
# 0.1 이나 0.2 처럼 십진수에서는 간단해 보이는 소수 중 일부는
# 이진수로 정확하게 표현할 수 없어 아주 미세한 오차를 가진 근사치로 저장됩니다.
# 이 작은 오차들이 연산을 거치면서 눈에 보이는 차이로 나타날 수 있습니다.
# 이를 부동 소수점 정밀도(floating-point precision) 문제라고 합니다.

# 가장 유명한 예시
a = 0.1
b = 0.2
result = a + b

print(f"0.1 + 0.2 = {result}")
print(f"결과가 0.3과 같은가? -> {result == 0.3}") # False!

# 왜 False 인가?
# 파이썬이 내부적으로 저장하는 값을 확인해보면 알 수 있습니다.
# (출력 형식에 따라 모든 소수점 자리가 보이지 않을 수 있습니다)
print(f"0.1의 실제 값 (근사치): {a:.20f}")
print(f"0.2의 실제 값 (근사치): {b:.20f}")
print(f"결과의 실제 값 (근사치): {result:.20f}")
print(f"0.3의 실제 값 (근사치): {0.3:.20f}")
# 미세하게 다른 것을 볼 수 있습니다.

print("-" * 20)

# 해결 방법:
# 1. math.isclose() 함수 사용 (권장)
#    두 부동 소수점 숫자가 허용 오차 범위 내에서 '매우 가까운지'를 비교합니다.
import math

if math.isclose(result, 0.3):
    print("math.isclose(): 두 값은 매우 가깝습니다.")
else:
    print("math.isclose(): 두 값은 다릅니다.")


# 2. 아주 작은 수를 이용한 범위 비교
#    두 수의 차이의 절대값이 아주 작은 값(epsilon)보다 작은지 확인합니다.
epsilon = 1e-9 # 0.000000001
if abs(result - 0.3) < epsilon:
    print("범위 비교: 두 값은 매우 가깝습니다.")
else:
    print("범위 비교: 두 값은 다릅니다.")


# 3. decimal 모듈 사용
#    금융 계산과 같이 정확한 십진수 연산이 반드시 필요한 경우 사용합니다.
#    일반적인 과학/공학 계산보다 속도는 느립니다.
from decimal import Decimal

# 문자열로 Decimal 객체를 생성해야 오차 없이 정확한 값을 표현할 수 있습니다.
dec_a = Decimal('0.1')
dec_b = Decimal('0.2')
dec_result = dec_a + dec_b

print(f"\nDecimal 모듈 사용 결과: {dec_result}")
print(f"Decimal 결과가 0.3과 같은가? -> {dec_result == Decimal('0.3')}") # True