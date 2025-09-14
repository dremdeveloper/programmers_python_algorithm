# 제목: 스택(Stack)을 이용한 짝 맞추기 및 검사 (괄호 유형)

# 스택은 후입선출(LIFO) 구조로, 괄호의 짝이 맞는지 검사하는 문제에 효과적입니다.
# 여는 괄호를 만나면 스택에 넣고, 닫는 괄호를 만나면 스택에서 꺼내 짝을 확인합니다.

def is_balanced(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        # 여는 괄호는 스택에 추가
        if char in "({[":
            stack.append(char)
        # 닫는 괄호일 경우
        elif char in ")}]":
            # 스택이 비어있으면 짝이 안 맞음
            if not stack:
                return False
            # 스택의 맨 위 괄호와 짝이 맞는지 확인
            top_element = stack.pop()
            if mapping[char] != top_element:
                return False

    # 모든 괄호를 확인한 후 스택이 비어있어야 올바른 괄호 문자열
    return not stack

# 테스트
str1 = "()[]{}"
str2 = "([)]"
str3 = "{([])}"
str4 = "())"

print(f"'{str1}' is balanced: {is_balanced(str1)}")
print(f"'{str2}' is balanced: {is_balanced(str2)}")
print(f"'{str3}' is balanced: {is_balanced(str3)}")
print(f"'{str4}' is balanced: {is_balanced(str4)}")