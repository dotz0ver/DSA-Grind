n = int(input())
times = list(map(int, input().split()))

times.sort()

total = 0
acc = 0

for time in times:
    acc += time
    total += acc

print(total)