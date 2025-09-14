# 제목: 조건부 표현식 (삼항 연산자)으로 if-else 간결하게 쓰기

# 조건부 표현식은 간단한 if-else 구문을 한 줄로 깔끔하게 표현할 수 있게 해줍니다.
# 다른 언어의 '삼항 연산자'와 비슷한 역할을 합니다.

# 기본 if-else 구문
score = 80
if score >= 60:
    message = "합격"
else:
    message = "불합격"
print(f"점수 {score}점은 {message}입니다.")

# 조건부 표현식
# [참일 때의 값] if [조건문] else [거짓일 때의 값]
score = 50
message_ternary = "합격" if score >= 60 else "불합격"
print(f"점수 {score}점은 {message_ternary}입니다.")

# 다른 예시: 짝수/홀수 판별
num = 7
result = "짝수" if num % 2 == 0 else "홀수"
print(f"\n숫자 {num}은(는) {result}입니다.")