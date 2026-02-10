n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
lst = [0] * 101

for start, end in segments:
    
    for i in range(start , end+1):
        lst[i] += 1

result = max(lst)

print(result)