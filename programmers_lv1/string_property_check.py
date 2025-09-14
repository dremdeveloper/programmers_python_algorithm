# 제목: isdigit(), isalpha()로 문자열 속성 검사하기

# 문자열이 어떤 종류의 문자로 구성되어 있는지 검사하는 유용한 메소드들입니다.

# 1. .isdigit(): 문자열이 '모두' 숫자로만 이루어져 있는지 확인
str1 = "12345"
str2 = "123a45"
print(f"'{str1}'.isdigit() -> {str1.isdigit()}")
print(f"'{str2}'.isdigit() -> {str2.isdigit()}")


# 2. .isalpha(): 문자열이 '모두' 알파벳으로만 이루어져 있는지 확인
str3 = "Python"
str4 = "Python3"
str5 = "Hello World" # 공백이 포함되어 있어 False
print(f"\n'{str3}'.isalpha() -> {str3.isalpha()}")
print(f"'{str4}'.isalpha() -> {str4.isalpha()}")
print(f"'{str5}'.isalpha() -> {str5.isalpha()}")


# 3. .isalnum(): 문자열이 '모두' 알파벳 또는 숫자로만 이루어져 있는지 확인
str6 = "User123"
str7 = "User@123" # 특수문자 '@' 포함
print(f"\n'{str6}'.isalnum() -> {str6.isalnum()}")
print(f"'{str7}'.isalnum() -> {str7.isalnum()}")