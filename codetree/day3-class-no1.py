n = int(input())
location_lst = [list(map(int, input().split())) for _ in range(n)]

# 제한 조건에 -100 ~ 100 이므로 201칸 정도의 영역 생성
area = [[0]*201 for _ in range(201)]

for locations in location_lst:
    # 색 위치 정보가 담긴 리스트를 순회하면서 꼭짓점 위치 할당
    x1, y1, x2, y2 = locations

    for x in range(x1, x2):
        for y in range(y1, y2):
            area[x][y] = 1

answer = sum(r.count(1) for r in area)

print(answer)