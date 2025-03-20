from collections import Counter

N = input()

counter = Counter(N)

count_6_9 = counter.get('6', 0) + counter.get('9', 0)
counter['6'] = counter['9'] = (count_6_9 // 2) + (count_6_9 % 2)

max_set = max(counter.values())

print(max_set)