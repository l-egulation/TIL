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

    # 누적합이 최솟값보다 크다면 return
    if fee >= answer:
        return

    # 12개월치를 다 계산했다면
    if month >= 12:
        # 누적합(최솟값)이 연간 이용권 보다 작다면
        if answer > fee:
            # 정답에 최솟값 할당
            answer = fee
        return
    
    # 1일 이용권 구매시
    dfs(month+1, fee + daily_fee*days[month])
    # 1개월 이용권 구매시
    dfs(month+1, fee + monthly_fee)
    # 3개월 이용권 구매시
    dfs(month+3, fee + quater_fee)

'''
1일 이용권으로 진행하다가 누적합이 연간 이용권보다 더 커지면
백트레킹해서 1개월 이용권 구매로 넘아가는 느낌
'''

T = int(input())

for tc in range(1, T+1):
    daily_fee, monthly_fee, quater_fee, answer = map(int, input().split())
    days = list(map(int, input().split()))

    # '월 - 1'이 idx값
    dfs(0, 0)

    print(f'#{tc} {answer}')