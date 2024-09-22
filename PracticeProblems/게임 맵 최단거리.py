"https://school.programmers.co.kr/learn/courses/30/lessons/1844"

"""
ROR 게임은 두 팀으로 나누어서 진행하며, 상대 팀 진영을 먼저 파괴하면 이기는 게임입니다. 
따라서, 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다.

검은색 부분은 벽으로 막혀있어 갈 수 없는 길이며, 흰색 부분은 갈 수 있는 길입니다. 
캐릭터가 움직일 때는 동, 서, 남, 북 방향으로 한 칸씩 이동하며, 게임 맵을 벗어난 길은 갈 수 없습니다.

만약, 상대 팀이 자신의 팀 진영 주위에 벽을 세워두었다면 상대 팀 진영에 도착하지 못할 수도 있습니다. 
예를 들어, 다음과 같은 경우에 당신의 캐릭터는 상대 팀 진영에 도착할 수 없습니다.

게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요. 
단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.

제한사항
- maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수입니다.
- n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
- maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
- 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.
"""


from collections import deque

def bfs(maps):
    n = len(maps)        
    m = len(maps[0])  

    queue = deque([(0, 0, 1)])  # 초기화
    visited = [[False] * m for i in range(n)]
    visited[0][0] = True 

    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        x, y, dist = queue.popleft()

        
        if x == n - 1 and y == m - 1:
            return dist

        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    return -1  # 경로가 없는 경우


n, m = map(int, input().split())
maps = [list(map(int, list(input().strip()))) for i in range(n)]  # 각 줄을 정수형 리스트로 변환

print(bfs(maps))







