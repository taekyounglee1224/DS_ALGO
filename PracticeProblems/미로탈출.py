"""
영철이는 N * M 크기의 직사각형 미로에 갇혀 있다. 미로에는  여러 마리의 괴물들이 있어
이를 피해 탈출해야 한다. 영철이의 위치는(1,1)이고 미로의 출구는 (N, M) 의 위치에 존재한다
한 번에 한 칸씩 이동할 수 있다.
이때 괴물이 있는 곳은 0으로, 없는 부분은 1로 표시된다. 
미로는 반드시 탈출할 수 있는 형태이다.
영철이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. (시작과 끝 포함)

입력 예] 
5 6
101010
111111
000001
111111
111111
"""


from collections import deque

def bfs(n, m):
    # 미로 입력을 함수 내에서 받음
    maze = [input() for _ in range(n)]
    
    move_x = [0, 0, 1, -1]
    move_y = [1, -1, 0, 0]

    queue = deque([(0, 0)])

    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    count = 1  
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if x == n-1 and y == m-1:
                return count

            for i in range(4):
                next_x = x + move_x[i]
                next_y = y + move_y[i]

                if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y] and maze[next_x][next_y] == '1':
                    visited[next_x][next_y] = 1
                    queue.append((next_x, next_y))
        count += 1

    return -1  # 도착점에 도달할 수 없는 경우

# n과 m을 입력받음
n, m = map(int, input().split())
print(bfs(n, m))