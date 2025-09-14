# 제목: 이진 탐색(Binary Search) 기본 템플릿

# 이진 탐색은 '정렬된' 리스트에서 특정 값을 찾는 매우 빠른 알고리즘입니다. (O(log N))
# 탐색 범위를 계속 절반으로 줄여나가며 값을 찾습니다.

def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]

        if guess == target:
            return mid # 값을 찾았을 경우 인덱스 반환
        if guess > target:
            high = mid - 1 # 추측값이 더 크면 오른쪽 절반을 버림
        else:
            low = mid + 1 # 추측값이 더 작으면 왼쪽 절반을 버림
            
    return None # 값을 찾지 못한 경우

# 테스트
sorted_list = [2, 5, 7, 8, 11, 12, 15, 19, 22]
target_num = 12

result_index = binary_search(sorted_list, target_num)
if result_index is not None:
    print(f"값 {target_num}은(는) 인덱스 {result_index}에 있습니다.")
else:
    print(f"값 {target_num}을(를) 찾을 수 없습니다.")