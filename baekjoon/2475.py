num_lst = list(map(int, input().split()))

result = 0

for num in num_lst:
    result += num**2

print(result%10)