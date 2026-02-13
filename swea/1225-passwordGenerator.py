from collections import deque

for tc in range(1, 11):
    _ = int(input())
    numbers = deque(map(int, input().split()))

    found = False
    while not found:
        for i in range(1, 6):
            number = numbers.popleft() - i

            if number <= 0:
                number = 0
                numbers.append(number)
                found = True
                break

            numbers.append(number)

    print(f'#{tc}', end=' ')
    print(*list(numbers))