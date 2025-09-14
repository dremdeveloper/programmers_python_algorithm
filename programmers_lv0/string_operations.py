# 제목: 문자열 합치기와 반복하기 (+, *)

# 문자열에도 산술 연산자 중 일부를 사용할 수 있습니다.

# 문자열 합치기 (Concatenation)
str1 = "Hello"
str2 = "World"
greeting = str1 + " " + str2
print(f"문자열 합치기: {greeting}")

# 문자열 반복하기 (Repetition)
laugh = "ha"
repeated_laugh = laugh * 5
print(f"문자열 반복하기: {repeated_laugh}")

# 주의! 문자열과 숫자는 직접 더할 수 없습니다. (TypeError 발생)
# error_case = "Age: " + 20 # 에러 발생
# 해결 방법은 str() 함수로 숫자를 문자열로 바꿔주는 것입니다.
correct_case = "Age: " + str(20)
print(correct_case)