# 셋(Set) 기본: 중복 제거 및 멤버십 테스트(in)

"""
셋(Set)은 순서가 없고, 중복되는 요소를 허용하지 않는 자료구조입니다.
주로 데이터의 중복을 제거하거나, 특정 요소의 존재 여부(멤버십 테스트)를
매우 빠르게 확인해야 할 때 유용하게 사용됩니다.

- 리스트의 멤버십 테스트 시간 복잡도: O(N)
  리스트는 요소를 처음부터 하나씩 비교하며 찾아야 합니다.
- 셋의 멤버십 테스트 시간 복잡도: O(1)
  셋은 해시 테이블로 구현되어 있어 요소의 개수와 상관없이 거의 일정한 시간 안에
  존재 여부를 확인할 수 있습니다.
"""

# 리스트의 중복된 요소를 제거할 때 유용
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
unique_fruits = set(fruits)
print(f"원본 리스트: {fruits}")
print(f"중복 제거 후(set): {unique_fruits}\n")

# 멤버십 테스트(Membership Test) 성능
# 아래 코드는 성능 차이를 설명하기 위한 개념적 코드입니다.
large_list = list(range(1000000))
large_set = set(range(1000000))
target = 999999

# 핵심 코드
is_in_list = target in large_list  # O(N) - 오래 걸림
is_in_set = target in large_set    # O(1) - 매우 빠름

print("데이터가 많을 때, 'in' 연산은 리스트보다 셋이 압도적으로 빠릅니다.")