# 문자열 조작: split()으로 나누고 join()으로 합치기

"""
split()과 join()은 파이썬에서 문자열을 다룰 때 가장 기본적이고 중요한 메서드입니다.
- str.split(separator): 문자열을 'separator'를 기준으로 나누어 '리스트'로 반환합니다.
  separator를 지정하지 않으면 공백(스페이스, 탭, 개행 등)을 기준으로 나눕니다.
- separator.join(list): 리스트에 있는 여러 문자열 요소들을 'separator'를 사이에
  넣어 하나의 '문자열'로 합칩니다.
"""

# split(): 문자열 -> 리스트
sentence = "Python is a powerful programming language"
words = sentence.split()
print(f"문자열: '{sentence}'")
print(f"split() 결과: {words}\n")

csv_data = "Alice,20,Seoul"
user_info = csv_data.split(',')
print(f"CSV 데이터: '{csv_data}'")
print(f"split(',') 결과: {user_info}\n")

# join(): 리스트 -> 문자열
word_list = ['Life', 'is', 'too', 'short']
sentence_from_list = " ".join(word_list)
print(f"리스트: {word_list}")
print(f"' '.join() 결과: '{sentence_from_list}'")