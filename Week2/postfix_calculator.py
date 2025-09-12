# postfix_calculator.py
# 제목: 스택을 이용한 후위 표기법(Postfix) 수식 계산

def calculate_postfix(expression):
    """
    후위 표기법으로 된 수식을 계산하여 결과를 반환합니다.
    각 항목은 공백으로 구분됩니다.
    """
    stack = []
    tokens = expression.split()

    for token in tokens:
        # 토큰이 숫자인 경우, 스택에 push
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            stack.append(int(token))
        # 토큰이 연산자인 경우
        else:
            # 연산을 위해 스택에서 두 개의 피연산자를 pop
            # 스택이 비어있으면 잘못된 수식
            if len(stack) < 2:
                raise ValueError("잘못된 후위 표기법 수식입니다.")
            
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                # 0으로 나누는 경우를 방지하기 위해 정수 나눗셈 사용
                result = int(operand1 / operand2)
            else:
                raise ValueError(f"지원하지 않는 연산자입니다: {token}")
            
            # 계산 결과를 다시 스택에 push
            stack.append(result)

    # 모든 연산이 끝나면 스택에는 최종 결과만 남아있어야 함
    if len(stack) != 1:
        raise ValueError("잘못된 후위 표기법 수식입니다.")

    return stack.pop()

# 테스트 케이스
# (5 + 2) * (8 - 3) = 7 * 5 = 35
expression = "5 2 + 8 3 - *"
result = calculate_postfix(expression)
print(f'후위 표기법 수식: "{expression}"')
print(f'계산 결과: {result}')

# 또 다른 테스트 케이스
# (10 * 2) / (1 + 4) = 20 / 5 = 4
expression_2 = "10 2 * 1 4 + /"
result_2 = calculate_postfix(expression_2)
print(f'\n후위 표기법 수식: "{expression_2}"')
print(f'계산 결과: {result_2}')