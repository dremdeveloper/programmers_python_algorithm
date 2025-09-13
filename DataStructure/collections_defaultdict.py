# collections.defaultdict: 키가 없을 때 기본값 자동 생성

"""
defaultdict는 collections 모듈의 클래스로, 딕셔너리와 거의 유사하지만
한 가지 중요한 차이점이 있습니다.
조회하려는 키가 딕셔너리에 존재하지 않을 때, KeyError를 발생시키는 대신
미리 지정된 '기본값(default value)'을 자동으로 생성하여 반환해 줍니다.
이 덕분에 딕셔너리에 키가 있는지 매번 확인하는 코드를 생략할 수 있어 편리합니다.
"""
from collections import defaultdict

# defaultdict(int) 사용: 키가 없을 때 기본값으로 0을 생성
word_list = ['apple', 'banana', 'apple', 'orange']
word_counts_dd = defaultdict(int)
for word in word_list:
    word_counts_dd[word] += 1 # 키 존재 여부 확인 없이 바로 연산 가능
print(f"defaultdict(int) 사용: {dict(word_counts_dd)}\n")

# defaultdict(list) 사용: 키가 없을 때 기본값으로 빈 리스트 []를 생성
name_list = ['Alice', 'Bob', 'Anna', 'Beth', 'Charles']
grouped_names = defaultdict(list)
for name in name_list:
    key = name[0] # 첫 글자를 키로 사용
    grouped_names[key].append(name) # 키 존재 여부 확인 없이 바로 append 가능
print(f"defaultdict(list)로 그룹핑: {dict(grouped_names)}")