import sys

input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())
    area = [list(map(str, input().strip())) for _ in range(H)]
    _ = int(input())
    commands = list(map(str, input().strip()))

    curr_r, curr_c = -1, -1
    dr, dc = 0, 0

    info = {
        "U" : ("^", -1, 0),
        "R" : (">", 0, 1),
        "D" : ("v", 1, 0),
        "L" : ("<", 0, -1)
    }

    # 초기 탱크 위치 및 방향 찾기
    flag = False
    for r in range(H):
        for c in range(W):
            if area[r][c] in "^v<>":
                curr_r, curr_c = r, c
                # 현재 탱크 모양에 따른 dr, dc 초기화
                if area[r][c] == "^": dr, dc = -1, 0
                elif area[r][c] == "v": dr, dc = 1, 0
                elif area[r][c] == "<": dr, dc = 0, -1
                elif area[r][c] == ">": dr, dc = 0, 1
                flag = True
                break
        if flag:
            break

    for cmd in commands:
        if cmd == "S":
            # 포탄 발사 로직
            k = 1
            while True:
                nr, nc = curr_r + (dr * k), curr_c + (dc * k)
                # 맵 밖으로 나가면 소멸
                if not (0 <= nr < H and 0 <= nc < W):
                    break

                # 벽돌 벽 : 평지로 만들고 소멸
                if area[nr][nc] == "*":
                    area[nr][nc] = "."
                    break

                # 강철 벽 : 그냥 소멸
                elif area[nr][nc] == "#":
                    break

                # 평지나 물이면 계속 전진
                k += 1

        else:
            shape, tank_r, tank_c = info[cmd]
            # 방향 전환 및 모양 변경 > 무조건 수행
            dr, dc = tank_r, tank_c
            area[curr_r][curr_c] = shape

            # 이동
            nr, nc = curr_r + dr, curr_c + dc
            # 맵 범위 내이고 평지(.)인 경우에만 이동
            if 0 <= nr < H and 0 <= nc < W and area[nr][nc] == ".":
                # 기존 위치 평지화
                area[curr_r][curr_c] = "."
                # 좌표 갱신
                curr_r, curr_c = nr, nc
                # 새 위치에 탱크 배치
                area[curr_r][curr_c] = shape

    print(f'#{tc}', end=' ')
    for row in area:
        print(''.join(row))