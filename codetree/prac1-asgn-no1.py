N, K = map(int, input().split())
lst = list(map(int, input().split()))

count = 0

for i in range(N):
    start = max(0, i - K)
    end = min(N, i + K + 1)
    
    window = lst[start:end]
    
    if max(window) <= lst[i]:
        count += 1

print(count)