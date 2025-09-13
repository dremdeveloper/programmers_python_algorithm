# AttributeError: 존재하지 않는 속성/메서드 호출

# 객체가 가지고 있지 않은 속성(변수)이나 메서드(함수)를 호출하려고 할 때
# AttributeError가 발생합니다.
# 예를 들어, 정수형 변수에서 리스트의 메서드인 .append()를 호출하는 경우입니다.

# 예시 상황
my_list = [1, 2, 3]
my_number = 100

# 올바른 경우: 리스트에 .append() 메서드 사용
my_list.append(4)
print("리스트:", my_list)

# 잘못된 경우 - AttributeError 발생
# 정수(int) 타입의 객체는 .append() 메서드를 가지고 있지 않습니다.
# 주석을 해제하고 실행해보세요.
# my_number.append(5)
# print(my_number)

# 또 다른 예: 오타
# .append()를 .add()로 잘못 입력
# 리스트는 .add() 메서드가 없습니다. (add는 세트 자료형의 메서드)
# 주석을 해제하고 실행해보세요.
# my_list.add(5)


# 해결 방법:
# 1. 변수의 타입을 확인합니다. (type() 함수 사용)
print("\n변수 타입 확인:")
print(f"my_list의 타입: {type(my_list)}")
print(f"my_number의 타입: {type(my_number)}")

# 2. dir() 함수나 코드 에디터의 자동완성 기능을 이용해
#    해당 객체가 사용할 수 있는 메서드 목록을 확인하고 오타가 없는지 검토합니다.
# print(dir(my_list))