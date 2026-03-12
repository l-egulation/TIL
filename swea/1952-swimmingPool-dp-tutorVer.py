T = int(input())

for tc in range(1, T+1):
    day_cost, month_cost, quarter_cost, answer = map(int, input().split())
    plans = list(map(int, input().split()))

    dp = [0]*12
    dp[0] = min(day_cost*plans[0], month_cost)
    for current in range(1, 12):
        dp[current] = dp[current-1]+min(day_cost*plans[current], month_cost)
        if current-2 >= 0:
            dp[current] = min(dp[current], dp[current-3]+quarter_cost)

    answer = min(answer, dp[11])

    print(f'#{tc} {answer}')