T = int(input())

for tc in range(1, T+1):
    lst = list(input())

    '''
    이건 뭐 어케 푸노 ㅅㅂ

    일단 괄호 양 끝 길이만큼 막대가 존재
    > () 는 2짜리 막대
    > 괄호를 열고 닫을 때까지가 막대의 길이. 단, ()는 안됨
    )의 개수가 곧 막대의 개수
    뒤에서 부터 확인하면서 ) 다음에 () 레이저 확인하고, ( 가 있을 때까지 .......
    한 막대길이 안에 레이저 수를 확인 > 레이저 수 + 1 = 그 막대가 잘린 개수
    하나의 막대 길이 안에 몇 개의 레이저가 있나 확인하는게 중요
    > 어케함?
    괄호가 열리고 레이저가 나오면 열린 개수 만큼 막대 수 증가
    단, 괄호가 닫히면 더 이상 막대 수 증가 X
    '''
    
    '''
    열린 괄호 ( 수 를 계속 확인하고(막대 개수 확인) 레이저가 하나 나올 때 마다 열린 괄호 수(막대 개수) 만큼 잘린 막대 수 +1
    그리고 닫힌 괄호 ) 가 나올때 마다 열린 괄호 수(막대 개수) -1 하고 **닫힌 괄호 수 만큼 잘린 막대 수 +1** > 이제 막대가 끝나서 남은 끄트머리도 잘린거라서
    
    레이저를 어떻게 파악하냐가 중요
    괄호가 열리고 바로 닫히면 레이저
    > 괄호가 열리고 바로 닫힐 때 마다 레이저 수 +1 

    1. '(' 있을 때마다 stick_num += 1
    2. '(' 바로 뒤에 ')'오면 stick_num -= 1, laser_num +1, answer_num += stick_num
    3. ')' 있울 때마다 stick_num -= 1, answer_num += 1
    '''

    stick_num, laser_num, answer_num = 0, 0, 0

    for i in range(len(lst)):
        
        if lst[i] == '(':
            stick_num += 1
        elif lst[i-1] == '(' and lst[i] == ')':
            stick_num -= 1
            laser_num +1
            answer_num += stick_num
        elif lst[i] == ')':
            stick_num -= 1
            answer_num += 1

    print(f'#{tc} {answer_num}')