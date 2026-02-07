N, M = map(int, input().split())

numbers = []
for num in range(1, N+1):
    numbers.append(num)

pick_number = []

def permutation_with_repetition(count):
    if count == M:
        print(*pick_number)
        return
    
    for i in range(len(numbers)):
        pick_number.append(numbers[i])

        permutation_with_repetition(count+1)

        pick_number.pop()

permutation_with_repetition(0)