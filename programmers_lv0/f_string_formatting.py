# 제목: f-string을 이용한 변수와 문자열 조합

# f-string은 문자열 안에 변수의 값을 쉽게 넣을 수 있게 해주는 편리한 기능입니다.
# 문자열 앞에 'f'를 붙이고, 넣고 싶은 변수를 중괄호 {}로 감싸주면 됩니다.

name = "Charlie"
age = 30
city = "Seoul"

# 기존 방식 (+ 연산자)
# 숫자를 str()로 변환해야 하는 번거로움이 있습니다.
old_way = "My name is " + name + ", I am " + str(age) + " years old and I live in " + city + "."
print(f"기존 방식: {old_way}")

# f-string 방식
# 훨씬 간결하고 읽기 쉽습니다.
f_string_way = f"My name is {name}, I am {age} years old and I live in {city}."
print(f"f-string 방식: {f_string_way}")

# 중괄호 안에서 간단한 연산도 가능합니다.
next_year_age = f"Next year, I will be {age + 1} years old."
print(next_year_age)