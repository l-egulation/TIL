from collections import deque

for tc in range(1, 11):
    _ = int(input())
    numbers = list(map(int, input().split()))

queue = deque()

print(numbers)

for number in numbers:
    print(number)

