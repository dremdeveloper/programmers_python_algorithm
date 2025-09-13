# IndentationError: 잘못된 들여쓰기

# 파이썬은 코드의 구조를 나타내기 위해 중괄호({}) 대신 들여쓰기를 사용합니다.
# if, for, def, class 등 다음 줄에 새로운 코드 블록이 시작될 때
# 들여쓰기(일반적으로 스페이스 4칸)를 정확히 맞춰주어야 합니다.
# 들여쓰기가 일관되지 않거나, 필요한 곳에 없으면 IndentationError가 발생합니다.

# 예시 상황
def say_hello(name):
    # 올바른 들여쓰기 (스페이스 4칸)
    print(f"Hello, {name}")

# 함수 호출
say_hello("World")


# 잘못된 경우 1: 들여쓰기가 아예 없는 경우
# 주석을 해제하면 IndentationError: expected an indented block 발생
# def say_goodbye(name):
# print(f"Goodbye, {name}") # 이 줄은 들여쓰기가 필요합니다.


# 잘못된 경우 2: 들여쓰기 수준이 다른 경우
# 주석을 해제하면 IndentationError: unindent does not match any outer indentation level 발생
# def greet(name):
#     print(f"Welcome, {name}")
#   print("Have a nice day!") # 첫 줄과 들여쓰기 수준이 다릅니다.


# 해결 방법:
# - 코드 블록 내에서는 항상 동일한 수준의 들여쓰기를 유지합니다.
# - 텍스트 에디터에서 탭(tab) 키를 스페이스 4칸으로 자동 변환해주는 설정을 사용하는 것이 좋습니다.