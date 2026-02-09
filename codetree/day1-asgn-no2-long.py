m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
day_of_the_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

'''
날짜 계산을 크게 세 가지 상황(같은 달, 미래의 달, 과거의 달)으로 나누어 접근

계산 로직:
    1. 같은 달(m1 == m2): 단순히 일(d)의 차이만 구해서 요일을 계산
    2. 미래의 달(m1 < m2): 
        (현재 달의 남은 일수) + (중간에 낀 달들의 일수 합) + (목표 달의 일수)를 모두 더해 간격을 구함
    3. 과거의 달(m1 > m2): 
        반대로 과거로 거슬러 올라가는 일수를 구한 뒤, 전체 요일(7)에서 빼주는 방식으로 역방향 인덱스를 찾음
'''

# 두 날짜의 월, 일을 입력받음
m1, d1, m2, d2 = map(int, input().split())

# 요일 이름과 각 달의 일수를 리스트로 정의
day_of_the_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 같은 달일 경우의 처리
if m1 == m2:
    # 미래의 날짜라면?
    if d1 <= d2:
        # 두 날짜의 차이를 7로 나눈 나머지를 인덱스로 사용 (순방향)
        print(day_of_the_week[abs(d1-d2) % 7])
    # 과거의 날짜라면?
    else:
        # 차이만큼 뒤로 가야 하므로 7에서 나머지를 빼줌 (역방향)
        print(day_of_the_week[7 - (abs(d1-d2) % 7)])

# 두 번째 날짜가 더 미래의 달일 경우
elif m1 < m2:
    # 바로 다음 달인 경우
    if m2 - m1 == 1:
        # (m1달의 남은 일수 + m2달의 현재 일수)를 7로 나눈 나머지 출력
        print(day_of_the_week[((month[m1]-d1) + d2) % 7])
    # 여러 달 뒤인 경우
    else:
        # (m1달의 남은 일수 + 중간 달들의 전체 일수 합 + m2달의 현재 일수)를 계산
        print(day_of_the_week[((month[m1]-d1) + sum(month[m1+1:m2]) + d2) % 7])

# 두 번째 날짜가 더 과거의 달일 경우
else:
    # 바로 전 달인 경우
    if m1 - m2 == 1:
        # 전 달에서 거슬러 올라온 일수를 구하고 7에서 빼서 역방향 계산
        print(day_of_the_week[7 - (((month[m2]-d2) + d1) % 7)])
    # 여러 달 전인 경우
    else:
        # (m2달의 남은 일수 + 중간 달들의 전체 일수 합 + m1달의 현재 일수)만큼 거슬러 올라감
        print(day_of_the_week[7 - (((month[m2]-d2) + sum(month[m2+1:m1]) + d1) % 7)])