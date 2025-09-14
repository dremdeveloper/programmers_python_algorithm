# 제목: sum() 함수로 리스트의 모든 숫자 더하기

# sum() 함수는 숫자로 이루어진 리스트(또는 튜플 등)의 모든 원소의 합을 구해줍니다.

numbers = [10, 20, 30, 40, 50]
total = sum(numbers)

print(f"리스트: {numbers}")
print(f"리스트의 모든 원소 합: {total}")

# 빈 리스트에 sum()을 사용하면 0을 반환합니다.
empty_list = []
print(f"\n빈 리스트의 합: {sum(empty_list)}")

# sum() 함수는 숫자 이외의 데이터가 포함된 리스트에는 사용할 수 없습니다.
# mixed_list = [1, 2, "hello"]
# sum(mixed_list) # 이 코드는 TypeError를 발생시킵니다.