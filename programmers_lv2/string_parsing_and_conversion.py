# 제목: 문자열 파싱 및 숫자 변환 (N진수 변환 포함)

# 코딩 테스트에서는 문자열을 특정 규칙에 따라 분해(파싱)하고,
# 그 일부를 숫자로 변환하여 계산하는 작업이 매우 흔합니다.

# 예시: "1001 (2)" -> 2진수 1001을 10진수로 변환
def parse_and_convert(s):
    # 공백을 기준으로 문자열 분리: "1001", "(2)"
    parts = s.split()
    
    num_str = parts[0]
    # 괄호와 숫자만 남기기: "(2)" -> "2"
    base_str = parts[1].replace("(", "").replace(")", "")
    
    # 문자열을 숫자로 변환
    base = int(base_str)
    
    # int(string, base) 함수를 이용해 N진수 문자열을 10진수 정수로 변환
    decimal_value = int(num_str, base)
    
    return decimal_value

# 테스트
input1 = "1101 (2)"
input2 = "2A (16)"
input3 = "120 (3)"

print(f"'{input1}' -> {parse_and_convert(input1)}")
print(f"'{input2}' -> {parse_and_convert(input2)}")
print(f"'{input3}' -> {parse_and_convert(input3)}")