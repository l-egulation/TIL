'''
2011년 11월 11일 11시 11분에서 시작하여 2011년 11월 a일 b시 c분까지 몇 분이 걸리는지를 계산

제한조건
# 11 <= A <= 14
# 0 <= B <= 23
# 0 <= C <= 59

입력
# 첫 번째 줄에 A, B, C가 공백을 사이에 두고 주어집니다.

출력
# 첫 번째 줄에 해당하는 값을 출력합니다. 단, a일 b시 c분이 11일 11시 11분보다 더 앞서다면 -1을 출력합니다.

input example
# 12 13 14

output example
# 1563

제한
# Time Limit : 1000ms
# Memory Limit : 80MiB

'''

a, b, c = map(int, input().split())

# Please write your code here.
day, hour, minute = 11, 11, 11
result_min = 0

# 처음부터 2011년 11월 11일 11시 11분 보다 과거인지 확인해야함
is_past = False
# 일 > 시 > 분으로 순차적으로 비교해야함
# 아니면 빠그리나서 과거 판정 불가
if a < 11:
    is_past = True
elif a == 11 and b < 11:
    is_past = True
elif a == 11 and b == 11 and c < 11:
    is_past = True

if is_past:
    print(-1)
else:
    while True:
        if day == a and hour == b and minute == c:
            break
        
        result_min += 1
        minute += 1

        if minute == 60:
            hour += 1
            minute = 0
        
        if hour == 24:
            day += 1
            hour = 0
        
    print(result_min)

'''
간단한 방식
시간 복잡도 = O(1)

a, b, c = map(int, input().split())

# 1. 시작 시간을 '분' 단위로 환산
# (2011년 11월은 고정이므로 무시해도 됩니다)
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