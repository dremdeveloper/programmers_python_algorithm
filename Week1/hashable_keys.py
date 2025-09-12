# hashable_keys.py
# 제목: list와 tuple의 해시 가능성(hashable) 비교

# 딕셔너리의 키는 '해시 가능(hashable)'해야 합니다.
# 해시 가능하다는 것은 객체의 생명주기 동안 변하지 않는 해시값을 가진다는 의미입니다.
# 일반적으로 불변(immutable) 객체들이 해시 가능합니다.

my_dict = {}

# --- 1. 튜플(tuple)을 딕셔너리 키로 사용하기 ---
# 튜플은 불변(immutable) 객체이므로 해시 가능합니다.
# 따라서 딕셔너리의 키로 사용할 수 있습니다.
key_tuple = (1, 2, 'hello')
my_dict[key_tuple] = 'value_for_tuple'
print(f"튜플 키 사용 성공: {my_dict}")


# --- 2. 리스트(list)를 딕셔너리 키로 사용하기 ---
# 리스트는 가변(mutable) 객체이므로 해시 가능하지 않습니다.
# 내용이 언제든지 바뀔 수 있어 고유한 해시값을 유지할 수 없기 때문입니다.
# 따라서 딕셔너리의 키로 사용하려고 하면 TypeError가 발생합니다.
key_list = [1, 2, 'hello']
try:
    my_dict[key_list] = 'value_for_list'
except TypeError as e:
    print(f"리스트 키 사용 실패: {e}")