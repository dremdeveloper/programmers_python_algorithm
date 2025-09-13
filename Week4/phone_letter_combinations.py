# 제목: 전화번호 키패드 문자 조합 생성 (백트래킹)

# 옛날 피처폰 키패드를 생각해보세요. 숫자 2에는 'abc', 3에는 'def'가 할당되어 있죠.
# 이 문제은 숫자 문자열(예: "23")이 주어졌을 때, 그 숫자들이 나타낼 수 있는
# 모든 문자 조합을 찾는 것입니다. "23"이라면 "ad", "ae", "af", "bd", "be", ... 등이 되겠죠.
# 각 자리의 숫자에서 문자를 하나씩 선택해나가는 과정을 백트래킹으로 구현할 수 있습니다.

def letter_combinations(digits):
    """숫자 문자열에 해당하는 모든 문자 조합을 반환합니다."""
    
    if not digits:
        return []

    # 키패드 매핑 정보
    keypad_map = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }
    
    results = []
    
    def backtrack(index, current_combination):
        # 현재 조합의 길이가 입력된 숫자 문자열의 길이와 같으면 완성
        if index == len(digits):
            results.append(current_combination)
            return
            
        # 현재 숫자에 해당하는 문자들을 가져옵니다.
        possible_chars = keypad_map[digits[index]]
        
        # 각 문자를 하나씩 조합에 추가하며 다음 단계로 넘어갑니다.
        for char in possible_chars:
            backtrack(index + 1, current_combination + char)

    backtrack(0, "")
    return results

if __name__ == '__main__':
    input_digits = "23"
    combinations = letter_combinations(input_digits)
    
    print(f"숫자 '{input_digits}'에 해당하는 문자 조합:")
    print(combinations)