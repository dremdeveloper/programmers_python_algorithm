# 제목: 리스트의 모든 순열(Permutations) 생성 (백트래킹)

# '순열'은 주어진 요소들의 순서를 바꿔서 만들 수 있는 모든 경우의 수를 의미합니다.
# 예를 들어 [1, 2, 3]의 순열은 [1, 2, 3], [1, 3, 2], [2, 1, 3], ... 등이 있죠.
# 이번에도 백트래킹을 사용해서 모든 순열을 효율적으로 찾아보겠습니다.
# 이미 사용한 숫자는 다시 사용하지 않는다는 조건만 잘 관리해주면 됩니다.

def find_permutations(nums):
    """주어진 리스트의 모든 순열을 찾습니다."""
    
    results = []
    current_permutation = []
    # 숫자의 사용 여부를 기록하는 배열
    used = [False] * len(nums)

    def backtrack():
        """백트래킹으로 순열을 생성합니다."""
        # 현재 순열이 원본 리스트와 같은 길이가 되면 하나의 순열 완성
        if len(current_permutation) == len(nums):
            results.append(list(current_permutation)) # 복사해서 추가
            return

        # 사용 가능한 숫자들을 모두 확인
        for i in range(len(nums)):
            # 아직 사용하지 않은 숫자라면
            if not used[i]:
                # 숫자를 사용했다고 표시하고
                used[i] = True
                # 현재 순열에 추가
                current_permutation.append(nums[i])
                
                # 다음 숫자를 찾기 위해 재귀 호출
                backtrack()
                
                # 재귀 호출이 끝나고 돌아오면, 선택을 되돌립니다 (백트래킹)
                # 다음 순열을 만들기 위해 방금 추가했던 숫자를 빼고
                current_permutation.pop()
                # 사용 여부도 원래대로 되돌립니다.
                used[i] = False

    backtrack()
    return results

if __name__ == '__main__':
    my_list = [1, 2, 3]
    all_permutations = find_permutations(my_list)
    
    print(f"{my_list}의 모든 순열:")
    for p in all_permutations:
        print(p)
    print(f"총 {len(all_permutations)}개의 순열이 있습니다.")