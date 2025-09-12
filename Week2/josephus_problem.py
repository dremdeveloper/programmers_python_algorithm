# josephus_problem.py
# 제목: 큐(Queue)를 이용한 요세푸스(Josephus) 문제 풀이

from collections import deque

def josephus_problem(n, k):
    """
    N명의 사람이 원을 이루고 앉아있고, K번째 사람을 계속해서 제거할 때
    최후에 남는 사람의 번호를 찾습니다.

    Args:
      n: 총 사람의 수
      k: 제거될 사람의 순서

    Returns:
      마지막으로 남은 사람의 번호
    """
    # 1부터 N까지의 사람들을 큐에 넣습니다.
    queue = deque(range(1, n + 1))
    
    print(f"N={n}, K={k} 요세푸스 문제 시작")
    print(f"초기 큐: {list(queue)}")

    while len(queue) > 1:
        # K-1명의 사람을 큐의 맨 앞에서 빼서 맨 뒤로 보냅니다.
        for _ in range(k - 1):
            person = queue.popleft()
            queue.append(person)
        
        # K번째 사람을 큐에서 제거합니다.
        removed_person = queue.popleft()
        print(f"-> {removed_person}번 제거. 현재 큐: {list(queue)}")

    # 큐에 마지막으로 남은 한 명을 반환합니다.
    return queue[0]

# 7명의 사람, 3번째 사람을 계속 제거
n_val = 7
k_val = 3
last_survivor = josephus_problem(n_val, k_val)
print(f"\n최종 생존자: {last_survivor}")