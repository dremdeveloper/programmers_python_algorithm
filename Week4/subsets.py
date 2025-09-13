# 제목: 모든 부분집합(Subsets) 구하기 (백트래킹)

# '부분집합'은 어떤 집합의 원소들로 만들 수 있는 모든 집합을 의미합니다.
# 공집합({})도 부분집합이고, 자기 자신도 부분집합이죠.
# 예를 들어 {1, 2}의 부분집합은 {}, {1}, {2}, {1, 2} 네 가지입니다.
# 이 문제는 각 원소에 대해 '포함한다'와 '포함하지 않는다' 두 가지 선택을
# 반복하는 과정으로 생각할 수 있어서 백트래킹으로 풀기 좋습니다.

def find_subsets(nums):
    """주어진 리스트의 모든 부분집합을 찾습니다."""
    
    all_subsets = []
    
    def backtrack(start_index, current_subset):
        # 현재까지 만들어진 부분집합을 결과에 바로 추가합니다.
        # 모든 경로의 중간 결과가 하나의 부분집합이 되기 때문이죠.
        all_subsets.append(list(current_subset))
        
        # start_index부터 순회하면서 원소를 하나씩 추가해 봅니다.
        for i in range(start_index, len(nums)):
            # 현재 원소를 부분집합에 포함
            current_subset.append(nums[i])
            # 다음 원소를 포함할지 결정하기 위해 재귀 호출
            backtrack(i + 1, current_subset)
            # 재귀 호출에서 돌아오면, 방금 포함했던 원소를 다시 빼줍니다 (백트래킹)
            current_subset.pop()
            
    backtrack(0, [])
    return all_subsets

if __name__ == '__main__':
    my_list = [1, 2, 3]
    subsets = find_subsets(my_list)
    
    print(f"{my_list}의 모든 부분집합:")
    # 보기 좋게 정렬해서 출력
    subsets.sort(key=len)
    print(subsets)
    print(f"총 {len(subsets)}개의 부분집합이 있습니다.")