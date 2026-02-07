N, M = map(int, input().split())

numbers = []
for num in range(1, N+1):
    numbers.append(num)

pick_number = []

def combination(count, idx):
    if count == M:
        print(*pick_number)
        return
    
    for i in range(idx, len(numbers)):
        pick_number.append(numbers[i])

        combination(count+1, i+1)

        pick_number.pop()

combination(0, 0)