# 제목: 그리디(Greedy) 알고리즘을 위한 정렬 후 반복 처리

# 그리디 알고리즘은 '매 순간 최적이라고 생각되는 선택'을 하는 방식으로
# 최종적인 해답에 도달하는 기법입니다.
# 많은 그리디 문제는 주어진 데이터를 특정 기준에 따라 정렬한 뒤,
# 순서대로 처리하며 답을 구하는 패턴을 가집니다.

# 예제: 회의실 배정 문제
# 한 회의실을 사용할 여러 회의의 시작 시간과 종료 시간이 주어졌을 때,
# 가장 많은 수의 회의를 진행할 수 있는 경우를 찾는 문제.
# -> 해결책: 종료 시간이 빠른 순서대로 정렬하고, 겹치지 않는 회의를 선택한다.

def max_meetings(schedule):
    # 1. 회의를 종료 시간(x[1]) 기준으로 오름차순 정렬
    sorted_schedule = sorted(schedule, key=lambda x: x[1])

    count = 0
    last_end_time = 0
    selected = []

    # 2. 정렬된 회의를 순서대로 확인
    for start, end in sorted_schedule:
        # 이전 회의가 끝난 시간 이후에 시작하는 회의라면 선택
        if start >= last_end_time:
            count += 1
            last_end_time = end
            selected.append((start, end))

    return count, selected

# (시작 시간, 종료 시간)
meetings = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11)]
count, result = max_meetings(meetings)

print(f"최대 회의 수: {count}")
print(f"선택된 회의: {result}")