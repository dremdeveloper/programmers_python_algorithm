# 제목: 진수 변환 (10진수 -> 2, 3, 8, 16진수)

decimal_num = 27

# 1. 내장 함수를 이용한 변환 (2, 8, 16진수)
# 결과는 '0b', '0o', '0x' 접두사가 붙은 문자열로 나옵니다.
bin_str = bin(decimal_num)
oct_str = oct(decimal_num)
hex_str = hex(decimal_num)

print(f"10진수 {decimal_num} -> 2진수: {bin_str}")
print(f"10진수 {decimal_num} -> 8진수: {oct_str}")
print(f"10진수 {decimal_num} -> 16진수: {hex_str}")


# 2. 3진법 등 임의의 진법으로 변환하기 (직접 구현)
# 알고리즘 문제에서 3진법 변환 등이 요구될 수 있습니다.
def convert_to_base(n, base):
    if n == 0:
        return "0"
    
    result = ""
    while n > 0:
        remainder = n % base
        result = str(remainder) + result
        n //= base
    return result

base3_str = convert_to_base(decimal_num, 3)
print(f"\n10진수 {decimal_num} -> 3진수: {base3_str}")


# 3. 다른 진법 문자열을 10진수로 변환 (int() 함수 사용)
print("\n--- 다른 진법 -> 10진수 ---")
print(f"2진수 '11011' -> 10진수: {int('11011', 2)}")
print(f"3진수 '1000'  -> 10진수: {int('1000', 3)}")
print(f"16진수 '1b'   -> 10진수: {int('1b', 16)}")