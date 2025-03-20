S = input()
lst = [0] * 26

for char in S:
    if 'a' <= char <= 'z':
        lst[ord(char) - ord('a')] += 1

print(*lst)