MOD = 1000000009

def solve():
    wrong = N - M
    
    # 2배 보너스 없이 채울 수 있는 최대 용량
    safe_capacity = (wrong + 1) * (K - 1)

    # 1. 보너스를 한 번도 안 받을 수 있는 경우
    if M <= safe_capacity:
        return M % MOD

    # 2. 보너스를 무조건 받아야 하는 경우
    # 폭탄(가장 큰 뭉치)을 맨 앞에 배치해서 작은 점수일 때 2배
    safe_sum = (wrong * (K - 1)) % MOD
    bomb_count = M - (wrong * (K - 1))
    
    d = bomb_count // K
    r = bomb_count % K
    
    # K * (2^(d+1) - 2) + r 공식 적용
    bomb_score = (K * (pow(2, d + 1, MOD) - 2 + MOD)) % MOD
    bomb_score = (bomb_score + r) % MOD

    return (bomb_score + safe_sum) % MOD

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    answer = solve()

    print(f'{answer}')