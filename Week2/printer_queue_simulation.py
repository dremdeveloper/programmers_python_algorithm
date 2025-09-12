# printer_queue_simulation.py
# 제목: 큐(Queue)를 이용한 프린터 대기열 시뮬레이션

import time
import random
from collections import deque

class Printer:
    def __init__(self):
        self.queue = deque()

    def add_job(self, document_name):
        """프린터 대기열에 새로운 인쇄 작업을 추가합니다."""
        print(f"[{time.strftime('%H:%M:%S')}] '{document_name}' 작업 추가됨. 대기열: {len(self.queue) + 1}개")
        self.queue.append(document_name)

    def run(self):
        """프린터 작동을 시작합니다."""
        print("\n--- 프린터 작동 시작 ---")
        while True:
            if self.queue:
                # 대기열에서 가장 오래된 작업을 꺼냅니다 (Dequeue)
                current_job = self.queue.popleft()
                print(f"[{time.strftime('%H:%M:%S')}] '{current_job}' 인쇄 시작...")
                
                # 인쇄하는 데 시간이 걸리는 것을 시뮬레이션
                print_time = random.randint(1, 4)
                time.sleep(print_time)
                
                print(f"[{time.strftime('%H:%M:%S')}] '{current_job}' 인쇄 완료! ({print_time}초 소요)")
            else:
                print(f"[{time.strftime('%H:%M:%S')}] 프린터 대기 중... (대기열 비어있음)")
                time.sleep(2)
                # 실제 환경에서는 계속 실행되지만, 예제를 위해 종료 조건을 추가
                if random.random() < 0.1:
                    print("\n--- 프린터 작동 중지 ---")
                    break

# 시뮬레이션 실행
printer = Printer()
printer.add_job("보고서.docx")
printer.add_job("중간고사_자료.pdf")
printer.add_job("여행사진.jpg")

# 별도의 스레드에서 프린터 실행 (실제로는 이렇게 구현)
# 여기서는 간단히 순차적으로 실행
printer.run()