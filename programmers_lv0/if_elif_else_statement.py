# 제목: if-elif-else를 이용한 다중 조건 분기

# 여러 개의 조건을 순서대로 확인하고 싶을 때 if-elif-else 구문을 사용합니다.
# if -> 조건1이 참인가?
# elif -> (조건1이 거짓일 때) 조건2가 참인가?
# else -> 위의 모든 조건이 거짓일 때

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"점수: {score}, 학점: {grade}")

# elif는 여러 개를 사용할 수 있습니다.
age = 15

if age >= 20:
    print("성인입니다.")
elif age >= 17:
    print("고등학생입니다.")
elif age >= 14:
    print("중학생입니다.")
elif age >= 8:
    print("초등학생입니다.")
else:
    print("미취학 아동입니다.")