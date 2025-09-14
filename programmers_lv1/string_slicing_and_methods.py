# 제목: 문자열 슬라이싱 및 기본 메소드 (upper, lower, replace)

my_string = "Hello, Python World!"

# 1. 슬라이싱 (Slicing)
# 문자열의 일부를 잘라냅니다. [시작인덱스:끝인덱스] (끝인덱스는 포함 안 됨)
# 인덱스 7부터 13 전까지
python_word = my_string[7:13]
print(f"슬라이싱 결과: {python_word}")

# 처음부터 5글자
hello_word = my_string[:5]
print(f"처음부터 슬라이싱: {hello_word}")


# 2. 대소문자 변환 메소드
# .upper(): 모든 문자를 대문자로 변경
upper_str = my_string.upper()
print(f"대문자로: {upper_str}")

# .lower(): 모든 문자를 소문자로 변경
lower_str = my_string.lower()
print(f"소문자로: {lower_str}")


# 3. 문자열 치환 메소드
# .replace(바꿀문자열, 새문자열)
replaced_str = my_string.replace("World", "Programming")
print(f"문자열 치환: {replaced_str}")