arr = list(map(int, input().split()))
target = int(input())

start = end = 0
count = 0
current_sum = 0

while True:
    if current_sum >= target:
        if current_sum == target:
            count += 1
        current_sum -= arr[start]
        start += 1
    elif end == len(arr):
        break
    else:
        current_sum += arr[end]
        end += 1

print(count)