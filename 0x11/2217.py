n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes.sort(reverse=True)

max_w = 0
for i in range(n):
    # 가장 약한 로프 * 로프 개수
    w = ropes[i] * (i + 1)
    max_w = max(max_w, w)

print(max_w)