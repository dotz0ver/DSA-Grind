N = int(input())
top = list(map(int, input().split()))
stack = []
result = [0] * N

for i in range(N):
    while stack:
        if stack[-1][0] < top[i]:
            stack.pop()
        else:
            result[i] = stack[-1][1]
            break
    stack.append((top[i], i + 1))

print(*result)