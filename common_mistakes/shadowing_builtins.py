# 내장 함수 덮어쓰기: list, dict 변수명 사용

# 파이썬에는 list(), dict(), str(), int() 등 매우 유용한 내장 함수(built-in function)들이 있습니다.
# 만약 변수 이름을 이 내장 함수들의 이름과 똑같이 지으면,
# 해당 변수는 더 이상 원래의 내장 함수를 가리키지 않고 우리가 할당한 값을 가리키게 됩니다.
# 이를 '이름을 덮어쓴다(shadowing)'고 표현합니다.
# 이렇게 되면 코드의 뒷부분에서 원래 내장 함수를 사용하려고 할 때 TypeError가 발생합니다.

# 잘못된 예시
# list 라는 이름의 변수를 만듦
list = [1, 2, 3]
print(f"내 변수 list: {list}")

# 이제 원래의 list() 내장 함수를 사용하려고 시도
# list()는 튜플이나 다른 반복 가능한 객체를 리스트로 만들어주는 함수입니다.
# 하지만 지금 'list'라는 이름은 우리가 만든 [1, 2, 3] 리스트를 가리키고 있습니다.
# 따라서 리스트 객체를 함수처럼 호출하려는 시도가 되어 TypeError가 발생합니다.

# 주석을 해제하고 실행해보세요
# a_tuple = (4, 5, 6)
# try:
#     new_list = list(a_tuple) # 'list' is not callable
#     print(new_list)
# except TypeError as e:
#     print(f"\n에러 발생: {e}")
#     print(f"현재 'list'의 타입: {type(list)}")


# 다른 예: sum
# sum은 숫자로 이루어진 리스트 등의 합계를 구하는 내장 함수입니다.
# sum = 1 + 2 # sum 이라는 변수명 사용
# my_numbers = [10, 20, 30]
# total = sum(my_numbers) # TypeError: 'int' object is not callable


# 해결 방법:
# - 파이썬 내장 함수의 이름(list, dict, str, int, sum, max, min 등)을 변수명으로 사용하지 않습니다.
# - 일반적으로 변수명은 좀 더 구체적인 의미를 담도록 짓는 것이 좋습니다. (e.g., my_list, user_list, scores_dict)
# - 만약 실수로 덮어썼다면, del 키워드로 변수를 삭제하여 원래 내장 함수를 다시 보이게 할 수 있습니다. (권장하지는 않음)

# 복구 예시 (참고용)
print("\n--- 복구 예시 ---")
dict = {"key": "value"} # dict 내장 함수를 덮어씀
print(f"내 변수 dict: {dict}")
# print(dict()) # TypeError 발생

del dict # 우리가 만든 dict 변수를 삭제

# 이제 다시 원래 내장 함수인 dict()를 사용할 수 있음
new_dict = dict()
print(f"원래대로 돌아온 dict(): {new_dict}")