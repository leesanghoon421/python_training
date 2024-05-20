#deque class를 collections module에서 import
from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

def bfs(maze, start):
    queue = deque([start])
    n = len(maze)
    m = len(maze[0])
    distances = [[-1 for _ in range(m)] for _ in range(n)]
    distances[start[0]][start[1]] = 1

    while queue:
        #이전에 다룬 위치를 x,y로 설정하고 queue에서 꺼내줌
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            #새로운 위치인 new_x와 new_y를 이용하여 조사
            new_x, new_y = x + dx, y + dy
            #maze 내부이고 지나갈 수 있는 길(maze == 1)이고 지정된 위치이고 지나간적 없는 길(distances == -1)
            if (0 <= new_x < n) and (0 <= new_y < m) and (maze[new_x][new_y] == 1) and (distances[new_x][new_y] == -1):
                #해당위치의 distances의 크기를 이전 위치 보다 1 큰값으로 설정
                distances[new_x][new_y] = distances[x][y] + 1
                #queue에 해당 위치 좌표를 대입
                queue.append((new_x, new_y))
    #n,m위치의 distances값을 return, index여서 0부터 시작하므로 1씩 빼줌
    return distances[n-1][m-1]

print(bfs(maze, (0, 0)))