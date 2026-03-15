N = int(input())

for _ in range(N):
    lst = list(map(str, input().split()))

    for _ in range(2):
        x = lst.pop(0)
        lst.append(x)

    print(' '.join(lst))