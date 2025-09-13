# Counter 활용: 두 단어의 애너그램(Anagram) 관계 확인

"""
애너그램(Anagram)은 한 단어의 문자를 재배열하여 만들 수 있는 다른 단어를 의미합니다.
(예: listen -> silent)
두 단어가 애너그램 관계이려면, 두 단어를 구성하는 알파벳의 종류와 각 알파벳의
개수가 정확히 일치해야 합니다. Counter는 이러한 조건을 확인하는 데 최적입니다.
"""
from collections import Counter

def is_anagram(word1, word2):
  """
  Counter를 이용해 두 단어가 애너그램 관계인지 확인한다.
  """
  # 각 단어의 문자별 개수를 센 Counter 객체가 완전히 동일한지 비교
  return Counter(word1) == Counter(word2)

# 테스트
word1 = "listen"
word2 = "silent"
word3 = "hello"

print(f"'{word1}'와 '{word2}'는 애너그램인가? {is_anagram(word1, word2)}")
print(f"'{word1}'와 '{word3}'는 애너그램인가? {is_anagram(word1, word3)}")