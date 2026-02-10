n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

'''
일단 시작 점이 있어야함
> 왼쪽으로 얼마, 오른쪽으로 얼마 가려면 뭐가 있어야 가지

그리고 한 번 이동한 후 현재 위치를 기록해야 됨
'''

lst = [0] * 2001
OFFSET = 1000

start = 0

for i in range(n):
    if dir[i] == 'L':
        end = start - x[i]
        for j in range(start+OFFSET-1, end+OFFSET-1, -1):
            lst[j] += 1

        start = end

    elif dir[i] == 'R':
        end = start + x[i]
        for j in range(start+OFFSET, end+OFFSET):
            lst[j] += 1

        start = end

ans = sum(1 for count in lst if count >= 2)
print(ans)