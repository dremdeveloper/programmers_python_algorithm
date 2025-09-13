# 튜플(Tuple): 불변(Immutable) 특성과 튜플 언패킹(Unpacking)

"""
튜플(Tuple)은 리스트와 매우 유사하지만, 한 가지 결정적인 차이점이 있습니다.
바로 '변경 불가능(immutable)'하다는 점입니다. 즉, 생성된 후에는
요소를 추가, 수정, 삭제할 수 없습니다.
이러한 불변성 때문에 튜플은 함수에서 여러 값을 반환하거나, 딕셔너리의 키로
사용되는 등 데이터의 무결성을 보장해야 하는 상황에서 유용하게 쓰입니다.

튜플 언패킹(Unpacking)은 튜플의 각 요소를 여러 변수에 한 번에 할당하는 편리한 기능입니다.
"""

# 튜플의 불변(Immutable) 특성
my_tuple = (1, "hello", 3.14)
try:
    my_tuple[0] = 100
except TypeError as e:
    print(f"튜플 수정 시도 -> TypeError: {e}\n")


# 튜플 언패킹 (Tuple Unpacking)
point = (10, 20)
x, y = point
print(f"튜플 언패킹: x={x}, y={y}")

# 변수 값 교환(swap)에 유용하게 사용됨
a = 10
b = 20
print(f"교환 전: a={a}, b={b}")
a, b = b, a # (b, a) 튜플을 만들어 a, b에 언패킹
print(f"교환 후: a={a}, b={b}\n")

# 함수에서 여러 값을 반환할 때 자동으로 튜플로 묶여서 반환됨
def get_user_info():
    name = "Alice"
    age = 21
    return name, age

name, age = get_user_info() # 반환된 튜플을 바로 언패킹
print(f"함수 반환값 언패킹: name='{name}', age={age}")