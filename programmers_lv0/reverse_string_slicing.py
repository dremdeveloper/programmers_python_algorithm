# 제목: 문자열 뒤집기 ([::-1])

# 파이썬의 슬라이싱(slicing) 기능을 이용하면 문자열을 매우 간단하게 뒤집을 수 있습니다.
# [start:stop:step] 형식에서 step을 -1로 주면 역순으로 동작합니다.

my_string = "hello"

# [::-1]은 처음부터 끝까지 -1칸 간격(역순)으로 슬라이싱하라는 의미입니다.
reversed_string = my_string[::-1]

print(f"원본 문자열: {my_string}")
print(f"뒤집은 문자열: {reversed_string}")

# 다른 예제
palindrome = "level"
if palindrome == palindrome[::-1]:
    print(f"'{palindrome}'은(는) 거꾸로 읽어도 똑같은 단어입니다.")