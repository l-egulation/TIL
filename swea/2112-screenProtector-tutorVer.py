'''
싀발

'어디가 단어가 들어갈 수 있을까?' 문제에서 연속된 것 찾는 것에 하위호환 로직

조합 문제
'''
def test_film():
    for c in range(W):
        count = 0
        before = -1
        for r in range(D):
            if films[r][c] != before:
                count = 1
            else:
                count += 1
                if count >= K:
                    break

            before = films[r][c]

        if count < K:
            return False

    return True

# count : 지금까지 고른 숫자 개수
# idx : 다음의 탐색 시작 인덱스
def comb(count, idx):
    global answer

    if test_film():
        answer = count

    if count >= answer-1:
        return

    for i in range(idx, D):
        backup = films[i]
        films[i] = A
        comb(count+1, idx+1)
        films[i] = B
        comb(count+1, idx+1)
        films[i] = backup

T = int(input())
# W보다 길어도 어짜피 W이상 순회를 안하기 때문에
# 최댓값으로 만들어둠
A = [0]*20
B = [1]*20

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]

    answer = K

    comb(0, 0)

    print(f'#{tc} {answer}')