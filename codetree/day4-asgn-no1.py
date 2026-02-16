import sys

data = sys.stdin.read().split()
if not data:
    exit()

N, M = int(data[0]), int(data[1])
idx = 2

A_pos = []
curr = 0
for _ in range(N):
    v, t = int(data[idx]), int(data[idx+1])
    for _ in range(t):
        curr += v
        A_pos.append(curr)
    idx += 2

B_pos = []
curr = 0
for _ in range(M):
    v, t = int(data[idx]), int(data[idx+1])
    for _ in range(t):
        curr += v
        B_pos.append(curr)
    idx += 2

count = 0
leader = 0

total_time = min(len(A_pos), len(B_pos))

for i in range(total_time):
    if A_pos[i] > B_pos[i]:
        curr_leader = 1
    elif A_pos[i] < B_pos[i]:
        curr_leader = 2
    else:
        continue

    if leader != 0 and leader != curr_leader:
        count += 1
    
    leader = curr_leader

print(count)