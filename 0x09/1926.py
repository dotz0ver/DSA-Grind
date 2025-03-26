from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    area = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    area += 1
    return area

max_area = 0
count = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            count += 1
            max_area = max(max_area, bfs(i, j))

print(count)
print(max_area)