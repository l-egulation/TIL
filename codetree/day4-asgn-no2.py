import sys

data = sys.stdin.read().split()
if not data:
    exit()

N, M = int(data[0]), int(data[1])
idx = 2

pos_A = [0]
curr = 0
for _ in range(N):
    t = int(data[idx])
    d = data[idx+1]
    v = 1 if d == 'R' else -1
    for _ in range(t):
        curr += v
        pos_A.append(curr)
    idx += 2

pos_B = [0]
curr = 0
for _ in range(M):
    t = int(data[idx])
    d = data[idx+1]
    v = 1 if d == 'R' else -1
    for _ in range(t):
        curr += v
        pos_B.append(curr)
    idx += 2

max_time = max(len(pos_A), len(pos_B))
while len(pos_A) < max_time:
    pos_A.append(pos_A[-1])
while len(pos_B) < max_time:
    pos_B.append(pos_B[-1])

count = 0

for i in range(1, max_time):
    if pos_A[i] == pos_B[i] and pos_A[i-1] != pos_B[i-1]:
        count += 1

print(count)