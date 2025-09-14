# 제목: 간단한 함수 정의와 호출 (def, return)

# 함수는 특정 작업을 수행하는 코드 묶음입니다.
# 반복되는 코드를 함수로 만들어두면 필요할 때마다 호출해서 재사용할 수 있습니다.

# 1. 간단한 함수 정의
# def 함수이름():
def say_hello():
    print("안녕하세요!")

# 함수 호출
print("함수 호출 전")
say_hello()
print("함수 호출 후")


# 2. 값을 받아 처리하는 함수 (매개변수)
# def 함수이름(매개변수):
def greet(name):
    print(f"{name}님, 환영합니다!")

greet("Alice")
greet("Bob")


# 3. 결과를 반환하는 함수 (return)
# def 함수이름(매개변수):
#     return 결과값
def add(a, b):
    result = a + b
    return result

# 함수를 호출하고 반환된 결과를 변수에 저장
sum_result = add(10, 5)
print(f"\nadd(10, 5)의 결과: {sum_result}")
print(f"add(100, 200)의 결과: {add(100, 200)}")