n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

arr = []

def dfs(start):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(start, n):
        arr.append(nums[i])
        dfs(i + 1)
        arr.pop()

dfs(0)