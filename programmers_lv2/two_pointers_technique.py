# 제목: 투 포인터(Two Pointers) 기법 활용

# 투 포인터는 '정렬된' 리스트에서 두 개의 포인터(보통 시작과 끝)를
# 이용해 원하는 값을 찾는 O(N) 시간 복잡도의 알고리즘입니다.

# 문제 예시: 정렬된 리스트에서 두 수의 합이 특정 값(target)이 되는 쌍 찾기
def find_sum_pair(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            # 합을 키워야 하므로 왼쪽 포인터를 오른쪽으로 이동
            left += 1
        else:
            # 합을 줄여야 하므로 오른쪽 포인터를 왼쪽으로 이동
            right -= 1
    return None

# 테스트
sorted_data = [1, 2, 4, 6, 8, 9, 14, 15]
target_sum = 10

result = find_sum_pair(sorted_data, target_sum)
if result:
    print(f"합이 {target_sum}이 되는 쌍: {result}")
else:
    print(f"합이 {target_sum}이 되는 쌍을 찾지 못했습니다.")