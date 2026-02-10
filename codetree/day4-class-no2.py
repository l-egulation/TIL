N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# 각 학생의 패널티를 저장하는 배열
counts = [0 for _ in range(N + 1)]

for s in student:
    counts[s] += 1

    if counts[s] >= K:
        print(s)
        exit()

print(-1)