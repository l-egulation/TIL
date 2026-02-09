'''
"조건부 시작 및 1분 단위 시뮬레이션"

1. 예외 처리 (과거 확인):
    목표 시간(a일 b시 c분)이 기준 시간(11일 11시 11분)보다 앞서는지 먼저 확인
    일(day) -> 시(hour) -> 분(minute) 순서대로 꼼꼼하게 비교하여 하나라도 작으면 바로 -1을 출력할 준비

2. 시뮬레이션 로직:
    기준 시간부터 1분씩 더해가며 목표 시간에 도달할 때까지 무한 루프(while True)를 돌림
    "60분이 되면 1시간이 올라가고", "24시간이 되면 1일이 올라가는" 실제 시계의 원리를 if문으로 구현

"총 분(total minutes)"을 한 번에 계산하는 수학적 방식 대신, 실제 시간이 흐르는 과정을 코드로 재현
'''

# 목표 일(a), 시(b), 분(c)을 입력받음
a, b, c = map(int, input().split())

# 기준이 되는 2011년 11월 11일 11시 11분을 변수에 저장
day, hour, minute = 11, 11, 11
# 총 몇 분이 지났는지 저장할 변수
result_min = 0

# 목표 시간이 기준 시간보다 과거인지 체크할 깃발(Flag) 변수
is_past = False

# 과거인지 확인하는 조건문 (일 -> 시 -> 분 순서로 비교)
if a < 11: # 11일보다 전이면 과거
    is_past = True
elif a == 11 and b < 11: # 11일인데 11시보다 전이면 과거
    is_past = True
elif a == 11 and b == 11 and c < 11: # 11일 11시인데 11분보다 전이면 과거
    is_past = True

# 과거라면 -1을 출력
if is_past:
    print(-1)
# 과거가 아니라면(현재 또는 미래라면) 계산을 시작
else:
    while True:
        # 현재 시뮬레이션 중인 시간이 목표 시간(a, b, c)과 같아지면 멈춤
        if day == a and hour == b and minute == c:
            break
        
        # 아직 목표 시간이 아니면 1분을 더함
        result_min += 1
        minute += 1

        # 60분이 다 찼다면? 0분으로 초기화하고 1시간을 올림
        if minute == 60:
            hour += 1
            minute = 0
        
        # 24시간이 다 찼다면? 0시로 초기화하고 1일을 올림
        if hour == 24:
            day += 1
            hour = 0
            
    # 반복이 끝나고 쌓인 총 분(result_min)을 출력
    print(result_min)

'''
간단한 방식
시간 복잡도 = O(1)

a, b, c = map(int, input().split())

# 1. 시작 시간을 '분' 단위로 환산
# (2011년 11월은 고정이므로 무시)
start_total = (11 * 24 * 60) + (11 * 60) + 11

# 2. 목표 시간을 '분' 단위로 환산
target_total = (a * 24 * 60) + (b * 60) + c

# 3. 차이 계산
diff = target_total - start_total

# 4. 결과 출력
if diff < 0:
    print(-1)
else:
    print(diff)
'''