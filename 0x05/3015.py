import sys
input = sys.stdin.readline

N = int(input())
stack = []
answer = 0

for _ in range(N):
    height = int(input())
    cnt = 1

    while stack and stack[-1][0] <= height:
        h, c = stack.pop()
        answer += c
        if h == height:
            cnt += c

    if stack:
        answer += 1

    stack.append((height, cnt))

print(answer)