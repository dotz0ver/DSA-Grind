n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

visited = [False] * n
arr = []

def dfs():
    if len(arr) == m:
        print(*arr)
        return

    for i in range(n): # 입력된 배열 인덱스 사용
        if not visited[i]:
            visited[i] = True
            arr.append(nums[i])
            dfs()
            arr.pop()
            visited[i] = False

dfs()