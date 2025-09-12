# defaultdict_counter.py
# 제목: collections.defaultdict를 이용한 요소 개수 카운팅

from collections import defaultdict

fruits = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']

# --- 1. 일반 딕셔너리를 사용한 카운팅 ---
# 키가 존재하는지 매번 확인해야 하는 번거로움이 있습니다.
counts_dict = {}
for fruit in fruits:
    if fruit not in counts_dict:
        counts_dict[fruit] = 0
    counts_dict[fruit] += 1
print(f"일반 dict 사용 결과: {dict(counts_dict)}")


# --- 2. defaultdict를 사용한 카운팅 ---
# defaultdict는 존재하지 않는 키를 조회할 때, 지정된 기본값(여기서는 int()의 결과인 0)을
# 자동으로 생성해주므로, 키 존재 여부를 검사할 필요가 없습니다.
# 코드가 훨씬 깔끔하고 간결해집니다.
counts_defaultdict = defaultdict(int)
for fruit in fruits:
    counts_defaultdict[fruit] += 1
print(f"defaultdict 사용 결과: {dict(counts_defaultdict)}")