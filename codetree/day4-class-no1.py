n, m = map(int, input().split())

a = [0]
b = [0]

# A의 입력
for _ in range(n):
    direction, time = input().split()
    time = int(time)

    for t in range(time):
        dx = 1 if direction == 'R' else -1
        a.append(a[-1] + dx)

# B의 입력
for _ in range(m):
    direction, time = input().split()
    time = int(time)

    for t in range(time):
        dx = 1 if direction == 'R' else -1
        b.append(b[-1] + dx)

# 같아지는 시점 찾기
for t in range(1, len(a)):
    if a[t] == b[t]:
        print(t)
        exit()

print(-1)