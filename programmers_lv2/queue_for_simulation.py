# 제목: 큐(Queue)를 이용한 시간 경과 시뮬레이션
from collections import deque

# 큐는 선입선출(FIFO) 구조로, 순서대로 작업을 처리하는 시뮬레이션에 적합합니다.
# 예: 프린터 대기열, 프로세스 스케줄링 등

# (작업 이름, 걸리는 시간) 튜플
tasks = [("문서1", 2), ("문서2", 4), ("문서3", 1)]
printer_queue = deque(tasks)

time = 0
print("프린터 작업 시뮬레이션 시작")
while printer_queue:
    # 대기열에서 다음 작업 가져오기
    task_name, task_time = printer_queue.popleft()
    print(f"시각 {time}: '{task_name}' 인쇄 시작 (소요 시간: {task_time}초)")
    # 작업 시간만큼 시간 경과
    time += task_time
    print(f"시각 {time}: '{task_name}' 인쇄 완료")

print("\n모든 작업 완료!")