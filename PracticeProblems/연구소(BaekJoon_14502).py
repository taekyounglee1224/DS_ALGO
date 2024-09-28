"https://www.acmicpc.net/problem/14502"

"""
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 
다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N x M인 직사각형으로 나타낼 수 있으며, 직사각형은 1 x 1 크기의 정사각형으로 나누어져 있다. 
연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.

2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

바이러스가 퍼진 뒤의 모습은 아래와 같아진다.

2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.
"""

def virus(lab, N, M):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    spread_lab = [row[:] for row in lab]
    queue = []

    for i in range(N):
        for j in range(M):
            if spread_lab[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and spread_lab[nx][ny] == 0:
                spread_lab[nx][ny] = 2
                queue.append((nx, ny))
    
    return sum(row.count(0) for row in spread_lab)

def set_walls(lab, N, M, wall_count, start, count):
    if count == 3:
        return virus(lab, N, M)
    
    max_safe_area = 0
    for i in range(start, N * M):
        x, y = i // M, i % M
        if lab[x][y] == 0:
            lab[x][y] = 1
            safe_area = set_walls(lab, N, M, wall_count + 1, i + 1, count + 1)
            max_safe_area = max(max_safe_area, safe_area)
            lab[x][y] = 0  # 벽 제거하고 원상태로 복원

    return max_safe_area

def solve(N, M, lab):
    return set_walls(lab, N, M, 0, 0, 0)

# 입력 받기
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

print(solve(N, M, lab))
