# 제목: 리스트의 모든 조합(Combinations) 생성 (백트래킹)

# '조합'은 순서에 상관없이 주어진 요소들 중에서 특정 개수를 뽑는 경우의 수입니다.
# 예를 들어 [1, 2, 3, 4]에서 2개를 뽑는 조합은 [1, 2], [1, 3], [1, 4], [2, 3], ... 등이 있죠.
# 순열과 달리 [1, 2]와 [2, 1]은 같은 조합으로 취급합니다.
# 이 문제를 해결하기 위해, 우리는 항상 현재 숫자보다 뒤에 있는 숫자들만
# 고려하는 방식으로 중복을 피할 수 있습니다.

def find_combinations(nums, k):
    """주어진 리스트에서 k개의 원소로 만들 수 있는 모든 조합을 찾습니다."""
    
    results = []
    
    def backtrack(start_index, current_combination):
        """백트래킹으로 조합을 생성합니다."""
        # k개의 원소로 구성된 조합을 찾으면 결과에 추가
        if len(current_combination) == k:
            results.append(list(current_combination))
            return
            
        # start_index부터 시작하여 중복 선택을 방지합니다.
        for i in range(start_index, len(nums)):
            # 현재 숫자를 조합에 추가
            current_combination.append(nums[i])
            # 다음 숫자는 현재 숫자의 다음 인덱스부터 찾도록 재귀 호출
            backtrack(i + 1, current_combination)
            # 재귀 호출이 끝나면, 선택을 되돌립니다 (백트래킹)
            current_combination.pop()
    
    backtrack(0, [])
    return results

if __name__ == '__main__':
    my_list = [1, 2, 3, 4]
    k = 2
    all_combinations = find_combinations(my_list, k)
    
    print(f"{my_list}에서 {k}개를 뽑는 모든 조합:")
    for c in all_combinations:
        print(c)
    print(f"총 {len(all_combinations)}개의 조합이 있습니다.")