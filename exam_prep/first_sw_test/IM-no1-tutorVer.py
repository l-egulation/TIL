numbers = [3, 5, 3]

answer = 0

for a in range(len(numbers)):
    for b in range(len(numbers)):
        # if문은 없는게 연산수가 적음
        if a == b:
            continue
        answer += numbers[a] % numbers[b]