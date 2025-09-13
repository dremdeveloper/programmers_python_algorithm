# 제목: 유효한 괄호의 모든 조합 생성 (백트래킹)

# '유효한 괄호'란 짝이 잘 맞는 괄호 문자열을 의미합니다.
# 예를 들어 "(())"나 "()()"는 유효하지만, ")(("나 "(()"는 유효하지 않죠.
# n개의 괄호 쌍이 주어졌을 때, 만들 수 있는 모든 유효한 괄호 조합을
# 찾는 문제입니다.
# 백트래킹을 사용하며 두 가지 규칙만 지키면 됩니다.
# 1. 여는 괄호 '('는 n개까지만 추가할 수 있다.
# 2. 닫는 괄호 ')'는 현재까지 사용된 여는 괄호의 수보다 많지 않을 때만 추가할 수 있다.

def generate_parentheses(n):
    """n개의 괄호 쌍으로 만들 수 있는 모든 유효한 조합을 생성합니다."""
    
    results = []
    
    def backtrack(current_string, open_count, close_count):
        # 괄호 문자열의 길이가 2*n이 되면 하나의 조합 완성
        if len(current_string) == 2 * n:
            results.append(current_string)
            return

        # 1. 여는 괄호 '(' 추가 조건: 아직 n개 미만으로 사용했다면
        if open_count < n:
            backtrack(current_string + "(", open_count + 1, close_count)
            
        # 2. 닫는 괄호 ')' 추가 조건: 닫는 괄호 수가 여는 괄호 수보다 적다면
        if close_count < open_count:
            backtrack(current_string + ")", open_count, close_count + 1)
            
    backtrack("", 0, 0)
    return results

if __name__ == '__main__':
    n = 3
    combinations = generate_parentheses(n)
    
    print(f"{n}쌍의 괄호로 만들 수 있는 모든 조합:")
    print(combinations)