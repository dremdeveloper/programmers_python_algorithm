# reverse_string_with_stack.py
# 제목: 스택을 이용한 문자열 뒤집기

def reverse_string_with_stack(s):
    """
    스택 자료구조를 이용하여 주어진 문자열을 뒤집습니다.
    """
    stack = []
    
    # 1. 문자열의 각 문자를 스택에 넣는다 (Push)
    for char in s:
        stack.append(char)
        
    reversed_list = []
    # 2. 스택이 빌 때까지 문자를 꺼내서(Pop) 리스트에 추가한다.
    #    가장 나중에 들어간 문자부터 나오므로 순서가 뒤집힌다.
    while stack:
        reversed_list.append(stack.pop())
        
    # 3. 문자 리스트를 하나의 문자열로 합쳐서 반환한다.
    return "".join(reversed_list)

# 테스트
original_string = "Hello, World!"
reversed_str = reverse_string_with_stack(original_string)

print(f"원본 문자열: {original_string}")
print(f"뒤집은 문자열: {reversed_str}")

original_string_2 = "Python"
reversed_str_2 = reverse_string_with_stack(original_string_2)

print(f"\n원본 문자열: {original_string_2}")
print(f"뒤집은 문자열: {reversed_str_2}")