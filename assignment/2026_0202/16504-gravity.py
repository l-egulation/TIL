T = int(input())

for test_case in range(1, T + 1):
    width = int(input())
    num_lst = list(map(int, input().split()))

    max_drop = 0

    for i in range(width):
        current_drop = 0

        for j in range(i+1, width):
            if num_lst[i] > num_lst[j]:
                current_drop += 1

        if current_drop > max_drop:
            max_drop = current_drop

    print(f"#{test_case} {max_drop}")