# KeyError: 딕셔너리에 없는 키 조회

# 딕셔너리는 key-value 쌍으로 데이터를 저장합니다.
# 특정 key를 통해 value를 찾으려고 할 때, 해당 key가 딕셔너리에 존재하지 않으면
# KeyError가 발생합니다.

# 예시: 학생 점수 딕셔너리
scores = {
    "math": 90,
    "english": 85,
}

# 올바른 접근
print("수학 점수:", scores["math"])

# 잘못된 접근 - KeyError 발생
# "science"라는 키는 딕셔너리에 없습니다.
# 주석을 해제하고 실행해보세요.
# print("과학 점수:", scores["science"])

# 해결 방법:
# 1. in 키워드로 키의 존재 여부를 미리 확인합니다.
key_to_find = "science"
if key_to_find in scores:
    print(f"{key_to_find} 점수:", scores[key_to_find])
else:
    print(f"{key_to_find} 점수는 존재하지 않습니다.")

# 2. .get() 메서드를 사용합니다.
# .get()은 키가 없으면 에러 대신 None을 반환하거나, 지정된 기본값을 반환합니다.
science_score = scores.get("science")
print("과학 점수 (get 사용):", science_score) # None 출력

science_score_default = scores.get("science", "N/A") # 기본값 "N/A"
print("과학 점수 (get + 기본값):", science_score_default)