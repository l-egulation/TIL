import sys

input = sys.stdin.readline

info = {
        "U" : ("^", -1, 0),
        "R" : (">", 0, 1),
        "D" : ("v", 1, 0),
        "L" : ("<", 0, -1)
    }

tank_chars = "^v<>"
tank_dir = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())
    area = [list(map(str, input().strip())) for _ in range(H)]
    _ = int(input())
    commands = list(map(str, input().strip()))

    curr_r, curr_c = -1, -1
    dr, dc, shape = 0, 0, ""

    # 초기 탱크 위치 및 방향 찾기
    flag = False
    for r in range(H):
        for c in range(W):
            if area[r][c] in tank_chars:
                curr_r, curr_c = r, c
                shape = area[r][c]
                dr, dc = tank_dir[shape]

                # 이동이 자유롭게 하기 위해 탱크 위치를 평지로 만듦
                area[r][c] = "."
                flag = True
                break
        if flag:
            break

    for cmd in commands:
        if cmd == "S":
            nr, nc = curr_r + dr, curr_c +dc
            # 포탄 발사 로직
            while 0 <= nr < H and 0 <= nc < W:
                if area[nr][nc] == "*":
                    area[nr][nc] = "."
                    break
                elif area[nr][nc] == "#":
                    break
                nr += dr
                nc += dc

        else:
            shape, tank_r, tank_c = info[cmd]
            # 방향 전환 및 모양 변경 > 무조건 수행
            dr, dc = tank_r, tank_c
            nr, nc = curr_r + dr, curr_c + dc

            if 0 <= nr < H and 0 <= nc < W and area[nr][nc] == ".":
                curr_r, curr_c = nr, nc

    area[curr_r][curr_c] = shape

    print(f"#{tc} " + "".join(area[0]))
    for i in range(1, H):
        print("".join(area[i]))