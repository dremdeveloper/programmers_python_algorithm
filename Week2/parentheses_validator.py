# parentheses_validator.py
# 제목: 스택을 이용한 괄호 유효성 검사

def is_valid_parentheses(s):
    """
    주어진 문자열의 괄호가 유효한지 검사합니다.
    (), {}, [] 세 종류의 괄호를 지원합니다.
    """
    stack = []
    # 닫는 괄호를 key, 여는 괄호를 value로 매핑
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        # 여는 괄호인 경우, 스택에 push
        if char in mapping.values():
            stack.append(char)
        # 닫는 괄호인 경우
        elif char in mapping.keys():
            # 스택이 비어있거나, 짝이 맞지 않으면 유효하지 않음
            if not stack or mapping[char] != stack.pop():
                return False
        # 괄호가 아닌 다른 문자는 무시
        else:
            continue

    # 루프 종료 후 스택이 비어있어야 모든 짝이 맞은 것
    return not stack

# 테스트 케이스
test_cases = [
    "()",
    "()[]{}",
    "(]",
    "([)]",
    "{[]}",
    "[[",
    "var a = { b: [1, 2] };", # 괄호 외 문자는 무시되어야 함
]

for case in test_cases:
    if is_valid_parentheses(case):
        print(f'"{case}" -> 유효함')
    else:
        print(f'"{case}" -> 유효하지 않음')