# queue_with_two_stacks.py
# 제목: 두 개의 스택을 이용한 큐 구현

class QueueWithTwoStacks:
    """
    두 개의 스택을 사용하여 큐의 Enqueue와 Dequeue 기능을 구현한 클래스입니다.
    """
    def __init__(self):
        # 데이터를 넣는 스택
        self.in_stack = []
        # 데이터를 빼는 스택
        self.out_stack = []

    def enqueue(self, item):
        """큐의 뒷부분에 데이터를 추가합니다."""
        print(f"Enqueue: {item}")
        self.in_stack.append(item)

    def dequeue(self):
        """큐의 앞부분에서 데이터를 제거하고 반환합니다."""
        # out_stack이 비어있다면, in_stack의 모든 요소를 out_stack으로 옮긴다.
        # 이 과정에서 in_stack에 쌓인 데이터의 순서가 역전되어 큐의 순서가 된다.
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        # out_stack에서 데이터를 꺼내면 FIFO 순서가 된다.
        if not self.out_stack:
            raise IndexError("큐가 비어있습니다.")
            
        dequeued_item = self.out_stack.pop()
        print(f"Dequeue: {dequeued_item}")
        return dequeued_item
    
    def __str__(self):
        # 현재 큐의 상태를 보기 쉽게 표현
        return f"Current Queue: {list(reversed(self.out_stack)) + self.in_stack}"

# 사용 예시
q = QueueWithTwoStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)

q.dequeue()
print(q)

q.enqueue(4)
print(q)

q.dequeue()
q.dequeue()
print(q)
q.dequeue()
print(q)