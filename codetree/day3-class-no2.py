# 제한 조건에 -1000 ~ 1000 이므로 201칸 정도의 영역 생성
area = [[0]*2001 for _ in range(2001)]

x1, y1, x2, y2 = map(int, input().split())
for x in range(x1, x2):
    for y in range(y1, y2):
        area[x][y] = 1

x1, y1, x2, y2 = map(int, input().split())
for x in range(x1, x2):
    for y in range(y1, y2):
        area[x][y] = 1

x1, y1, x2, y2 = map(int, input().split())
for x in range(x1, x2):
    for y in range(y1, y2):
        area[x][y] = 0

answer = sum(r.count(1) for r in area)

print(answer)