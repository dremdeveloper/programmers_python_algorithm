# 제목: 해시(딕셔너리)를 이용한 요소 개수 세기

# 딕셔너리(해시 테이블)를 사용하면 리스트에 있는 각 요소가 몇 번 등장하는지
# 효율적으로 계산할 수 있습니다.

def count_frequency(data_list):
    freq_counter = {}
    for item in data_list:
        # 딕셔너리에 아이템이 이미 키로 존재하면 값을 1 증가
        if item in freq_counter:
            freq_counter[item] += 1
        # 존재하지 않으면 새로운 키로 추가하고 값을 1로 설정
        else:
            freq_counter[item] = 1
    return freq_counter

fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = count_frequency(fruits)

print(f"원본 리스트: {fruits}")
print(f"각 요소의 개수: {frequency}")
print(f"사과의 개수: {frequency['apple']}")