n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# 모든 좌표가 양수가 되도록 오프셋 설정 (-100 -> 0)
# -100 ~ 100으로 생각하고 리스트를 만들어도 실제로는 인덱스로 0 ~ 200까지임
# 그래서 for문의 범위를 정할때 직관적으로 start와 end가 보이면서 실제 인덱스로는 정확히 들어가기 위해서 offset을 사용함
OFFSET = 100
# 문제의 제한 조건에 2 ≤ N ≤ 100 / -100 ≤ x1 ≤ x2 ≤ 100 이 있는데
# -100 ~ 100 범위를 커버하기 위해 넉넉히 200칸 이상의 리스트 생성 
lst = [0] * 201

for start, end in segments:
    # 오프셋을 더해 인덱스 계산
    # 문제에서 끝 점에서 닿는 경우는 겹치는 것으로 생각하지 않는다고 되있음
    # (2, 4), (4, 6)은 끝 점만 닿는거라 사실상 한 점임 => 끝점 무시
    # 그래서 range(start, end)를 쓰면 end 지점은 칠하지 않으므로 '끝점이 닿는 경우'를 자동으로 무시

    for i in range(start + OFFSET, end + OFFSET):
        lst[i] += 1

# 나머지는 전 문제와 동일하게 구성

result = max(lst)
print(result)