# 제목: 문자열 split()과 join()으로 분리 및 결합하기

# 1. .split(): 하나의 문자열을 특정 구분자를 기준으로 나누어 리스트로 만듭니다.
sentence = "Python is a powerful programming language"

# 공백을 기준으로 나누기
words = sentence.split()
print(f"원본 문장: '{sentence}'")
print(f".split() 결과: {words}")

csv_data = "apple,banana,cherry"
# 쉼표(,)를 기준으로 나누기
items = csv_data.split(',')
print(f"\n원본 CSV: '{csv_data}'")
print(f".split(',') 결과: {items}")


# 2. .join(): 리스트의 여러 문자열을 하나의 문자열로 합칩니다.
# '구분자'.join(리스트) 형태로 사용합니다.
word_list = ["Life", "is", "too", "short"]

# 공백(' ')을 구분자로 하여 합치기
joined_sentence = " ".join(word_list)
print(f"\n원본 리스트: {word_list}")
print(f"' '.join() 결과: '{joined_sentence}'")

# 하이픈('-')을 구분자로 하여 합치기
hyphen_joined = "-".join(word_list)
print(f"'-'.join() 결과: '{hyphen_joined}'")