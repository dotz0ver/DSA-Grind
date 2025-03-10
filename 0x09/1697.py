from collections import deque

n, k = map(int, input().split())
MAX = 100001

visited = [0] * MAX

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[x])
            return
        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx < MAX and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                queue.append(nx)

bfs()