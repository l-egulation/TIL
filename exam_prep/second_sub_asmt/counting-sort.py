data = list(map(int, input().split()))

'''
카운팅 정렬은 "카운팅, 누적, 역순"만 기억하면 됨

카운팅 정렬은 리스트의 각 요소들이 몇 개씩 있는지 확인하고
이를 누적합 한 뒤, 뒤에서부터 차례로 요소를 정렬하는 것


'''

def counting_sort(lst):
    count = [0] * (max(lst)+1)
    temp = [0] * len(lst)

    for i in range(len(lst)):
        count[lst[i]] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    for i in range(len(lst)):
        count[lst[i]] -= 1
        temp[count[lst[i]]] = lst[i]
    
    return temp

result = counting_sort(data)
print(result)