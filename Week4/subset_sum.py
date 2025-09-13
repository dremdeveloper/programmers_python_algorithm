# 제목: 부분집합의 합(Subset Sum) 문제 (백트래킹)

# 부분집합의 합 문제는 주어진 숫자들 중에서 몇 개를 골라
# 그 합이 목표값(target)과 같아지는 경우가 있는지 확인하는 문제입니다.
# 예를 들어, 숫자 [3, 1, 4, 1, 5, 9]와 목표값 10이 주어졌을 때
# 부분집합 [1, 4, 5]의 합이 10이므로 '참'이 됩니다.
# 모든 부분집합을 구해서 합을 계산하는 대신, 합을 계산하는 과정 자체를
# 백트래킹으로 최적화하여 목표를 달성하면 바로 탐색을 중단할 수 있습니다.

def can_partition(nums, target_sum):
    """
    주어진 숫자 리스트의 부분집합 중 합이 target_sum이 되는 경우가 있는지 확인합니다.
    """
    
    # 성능 향상을 위한 최적화: 내림차순 정렬
    # 큰 숫자부터 확인하면 목표 합을 초과하는 경우를 더 빨리 발견하여
    # 불필요한 탐색(가지치기)을 줄일 수 있습니다.
    nums.sort(reverse=True)
    
    def backtrack(start_index, current_sum):
        # 현재 합이 목표와 같아지면 True 반환 (성공)
        if current_sum == target_sum:
            return True
        
        # 현재 합이 목표를 넘어서면 더 이상 탐색할 필요가 없음 (실패)
        if current_sum > target_sum:
            return False
            
        for i in range(start_index, len(nums)):
            # 현재 숫자를 포함하여 재귀 호출
            if backtrack(i + 1, current_sum + nums[i]):
                return True
        
        # 모든 경우를 탐색했는데도 합을 만들지 못하면 False 반환
        return False
        
    return backtrack(0, 0)

if __name__ == '__main__':
    my_nums = [3, 1, 4, 1, 5, 9, 2, 6]
    target1 = 10 # 1+9, 4+6, 3+1+6 등 가능
    target2 = 33 # 불가능
    
    print(f"리스트 {my_nums}의 부분집합 합으로 {target1}을 만들 수 있나요? -> {can_partition(my_nums, target1)}")
    print(f"리스트 {my_nums}의 부분집합 합으로 {target2}을 만들 수 있나요? -> {can_partition(my_nums, target2)}")