from collections import defaultdict

N = int(input())
arr = [input().strip() for _ in range(N)]

dict = defaultdict(int)

for r in range(N):
    for c in range(N):
        dict[arr[r][c]] += 1

sorted_keys = sorted(dict.keys())
max_alphabet = max(sorted_keys, key=dict.get)
max_value = dict[max_alphabet]
count = N**2 - max_value

print(count, max_alphabet)