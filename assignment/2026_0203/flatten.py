def counting_sort(lst):
    k = max(lst)
    counts = [0] * (k+1)
    box_lst = [0] * len(lst)

    for i in range(len(lst)):
        counts[lst[i]] += 1
    
    for i in range(1 ,k+1):
        counts[i] += counts[i-1]

    for i in range(len(lst)-1, -1, -1):
        counts[lst[i]] -= 1
        box_lst[counts[lst[i]]] = lst[i]

    return box_lst

def bubble_sort(lst):
    N = len(lst)

    for i in range(N-1, 0, -1) :
        for j in range(i) :
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]
    
    return lst

for tc in range(1, 11):
    dunp_num = int(input())
    origin_lst = list(map(int, input().split()))

    print(origin_lst)

    box_lst = counting_sort(origin_lst)

    while dunp_num > 0:
        box_lst[-1] -= 1
        box_lst[0] += 1

        box_lst = bubble_sort(box_lst)
        
        dunp_num -= 1
    
    print(f'#{tc} {box_lst[-1] - box_lst[0]}')