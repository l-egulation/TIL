'''
열 하나 잡고 아래로 열 순회하면서 count
> 그 저번에 십자 퍼즐할 때처럼 count 쌓고 초기화하고 그거 쓰먼될 듯

각 열을 체크하고, 0 또는 1이 K번 이상 연속 되었다면 통과

통과가 안된 열에 대해서 가능성이 높은 문자로 가능성이 높은 열로 바꾸고 싶음
> 이걸 어떻게 하는지 생각이 안남

그럼 0번째 행부터 하나씩 다 바꿔?
> 진짜 순회를 말도 안되게 많이해야함

코드가 아닌 직접 문제를 풀 때 생각하는 로직을 코드로 구현

1. 각 열을 순회하면서 K만큼 연속되나 체크
2. 연속이 안되는 열에서 어떤 문자가 몇 번 반복되었는지 확인
3. 반복된 횟수가 K랑 얼마나 차이나는지 확인
4. 바꾸면 바로 연속되는 행을 찾고, 그 행을 어떤 문자로 바꾸면 될지 판별
    4-1. 다른 열에서 K번 이상 연속된 수가 있나 확인
    4-2. 바꾸면 바로 연속이 되는 행에서 바꿀 문자가 그 행에 얼마나 많은지와, 바꿔도 영향이 없을지를 확인
    4-3. 가중치를 따져서 바꿈
5. 바꾸고 난 뒤 다시 1~4 반복
6. 최종적으로 다 모든 열에서 같은 문자가 K번 이상 연속된다면, 몇 개의 행의 문자를 바꿨는지 출력

-----------------------------------------------------------------

# 회고록

그냥 0번째 행부터 하나씩 다 쳐 바꾸지 좀 싀발람아
안되면 완탐해 개이색기야
자꾸 안되는걸 쳐 잡고 있으니까 못 풀지 싀이발 하
접어 걍 싸탈해

'''

def is_pass():
    for c in range(W):
        passed_col = False
        count = 1

        if K == 1:
            continue

        for r in range(1, D):
            if films[r][c] == films[r-1][c]:
                count += 1
            else:
                count = 1

            if count >= K:
                passed_col = True
                break

        if not passed_col:
            return False

    return True

T = int(input())

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]

    answer = K

    print(f'#{tc} {answer}')