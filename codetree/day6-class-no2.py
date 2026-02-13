n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

mapper = {
    'U': 0,
    'D': 2,
    'R': 1,
    'L': 3
}

d = mapper[d]

for _ in range(t):
    nr = r + dr[d]
    nc = c + dc[d]

    if nr < 1 or nr > n or nc < 1 or nc > n:
        d = (d+2) % 4
    else:
        r = nr
        c = nc

print(r, c)