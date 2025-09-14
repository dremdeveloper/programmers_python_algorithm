# 제목: 아스키코드 변환 (ord(), chr()) (시저 암호 유형)

# ord(): 문자 -> 아스키 코드(숫자)
# chr(): 아스키 코드(숫자) -> 문자

# 1. 기본 사용법
char = 'A'
code = ord(char)
print(f"문자 '{char}'의 아스키 코드: {code}")

num = 66
char_from_num = chr(num)
print(f"아스키 코드 {num}의 문자: '{char_from_num}'")


# 2. 응용: 간단한 시저 암호 (Caesar cipher)
# 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식
plain_text = "HELLO"
shift = 3
encrypted_text = ""

for char in plain_text:
    # 1. 문자를 아스키 코드로 변환
    ascii_code = ord(char)
    # 2. shift만큼 더하기
    shifted_code = ascii_code + shift
    # 3. 숫자를 다시 문자로 변환하여 결과에 추가
    encrypted_text += chr(shifted_code)

print(f"\n원본: {plain_text}")
print(f"암호화 (shift={shift}): {encrypted_text}") # HELLO -> KHOOR

# 복호화 (암호 풀기)는 반대로 shift만큼 빼주면 됩니다.
decrypted_text = ""
for char in encrypted_text:
    decrypted_text += chr(ord(char) - shift)

print(f"복호화: {decrypted_text}")