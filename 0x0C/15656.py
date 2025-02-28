n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

arr = []

def dfs():
    if len(arr) == m:
        print(*arr)
        return

    for i in range(n):
        arr.append(nums[i])
        dfs()
        arr.pop()

dfs()