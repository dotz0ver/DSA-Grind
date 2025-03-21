N = int(input())
buildings = [int(input()) for _ in range(N)]
stack = []
result = 0

for height in buildings:
    while stack:
        if stack[-1] <= height:
            stack.pop()
        else:
            break
    result += len(stack)
    stack.append(height)

print(result)