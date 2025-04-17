N = int(input())
A = set(map(int, input().split()))

M = int(input())
target = list(map(int, input().split()))

for t in target:
    print(1 if t in A else 0)