N, M = map(int, input().split())

numbers = []
for num in range(1, N+1):
    numbers.append(num)

pick_number = []
visited = [0] * N

def permutation(count):
    if count == M:
        print(*pick_number)
        return
    
    for i in range(len(numbers)):
        if visited[i]:
            continue
        
        visited[i] = 1
        pick_number.append(numbers[i])
        permutation(count+1)
        visited[i] = 0
        pick_number.pop()

permutation(0)