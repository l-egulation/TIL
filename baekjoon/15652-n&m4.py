N, M = map(int, input().split())

numbers = []
for num in range(1, N+1):
    numbers.append(num)

pick_number = []

def combination_with_repetition(count, idx):
    if count == M:
        print(*pick_number)
        return
    
    for i in range(idx, len(numbers)):
        pick_number.append(numbers[i])

        combination_with_repetition(count+1, i)

        pick_number.pop()

combination_with_repetition(0, 0)