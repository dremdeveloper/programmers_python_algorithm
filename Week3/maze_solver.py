# 제목: 그래프 탐색을 이용한 간단한 미로 찾기

# 미로 찾기는 그래프 탐색을 활용할 수 있는 아주 재미있는 예제예요.
# 미로의 각 칸을 그래프의 '노드'로, 상하좌우로 이동할 수 있는 길을 '엣지'로 생각하면
# BFS를 이용해 출발점에서 도착점까지의 최단 경로를 찾을 수 있습니다.

from collections import deque

def solve_maze(maze, start, end):
    """
    BFS를 이용해 2D 미로의 최단 경로를 찾습니다.
    
    Args:
        maze: 0은 길, 1은 벽인 2D 리스트
        start: 시작 좌표 (row, col)
        end: 도착 좌표 (row, col)
        
    Returns:
        경로(좌표 리스트) 또는 경로가 없으면 None
    """
    rows, cols = len(maze), len(maze[0])
    
    # 큐에는 (좌표, 현재까지의 경로 리스트)를 저장합니다.
    queue = deque([(start, [start])])
    visited = {start}
    
    # 이동할 수 있는 네 방향 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (r, c), path = queue.popleft()

        # 도착점에 도달했다면 경로를 반환합니다.
        if (r, c) == end:
            return path
        
        # 네 방향으로 이동을 시도합니다.
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # 다음 위치가 미로 범위 안에 있고, 벽이 아니며, 아직 방문하지 않았다면
            if 0 <= nr < rows and 0 <= nc < cols and \
               maze[nr][nc] == 0 and (nr, nc) not in visited:
                
                visited.add((nr, nc))
                # 새로운 경로를 만들어 큐에 추가합니다.
                new_path = path + [(nr, nc)]
                queue.append(((nr, nc), new_path))
                
    # 큐가 비워질 때까지 도착점에 도달하지 못하면 경로가 없는 것입니다.
    return None

if __name__ == '__main__':
    # 0: 길, 1: 벽
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    start_pos = (0, 0)
    end_pos = (4, 4)

    path = solve_maze(maze, start_pos, end_pos)

    if path:
        print(f"미로 탈출 경로를 찾았습니다 (최단 경로):")
        print(path)
    else:
        print("미로 탈출 경로를 찾을 수 없습니다.")