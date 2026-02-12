'''
min_ans = min(min_ans, current_sum)
> 일단 이거 써야함

왜 DFS로 하라하는지 알 것 같긴함
이용권마다 금액이 다르니까
1일권 통일, 1달권 통일, 조합해서, ...
이런식으로 하게되면
DFS로 1일권 몇 개 선택, 1달권 몇 개 선택, ... 밀고 가다가 전에 최솟값보다 크면 백트레킹하고

visited는 써야하나?
> 어떻게 써야될지도 감이 안옴
'''
'''
DP로 푸는게 뭘까
'''

# month에서 실제 월에서 -1
def dfs(month, fee):
    global answer

    if fee >= answer:
        return

    if month >= 12:
        if answer > fee:
            answer = fee
        return
    
    # 일권
    dfs(month+1, fee + day_fee*days[month])
    # 월권
    dfs(month+1, fee + month_fee)
    # 3개월권
    dfs(month+3, fee + quater_fee)

T = int(input())

for tc in range(1, T+1):
    # answer = float('inf')
    # 이 문제의 최댓값은 1년 이용권

    day_fee, month_fee, quater_fee, answer = map(int, input().split())
    days = list(map(int, input().split()))

    # '월 - 1'이 idx값
    dfs(0, 0)

    print(f'#{tc} {answer}')