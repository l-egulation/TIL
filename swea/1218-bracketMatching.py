for tc in range(1, 11):
    N = int(input())
    N_lst = list(input())

    '''
    괄호 검사 코드와 변경된 것은 거의 없음
    > 그냥 괄호 종류가 늘어난 만큼 조건문도 추가

    그래서 이번엔 딕셔너리 형태로 비교해서 짧게 만듦
    딕셔너리에 짝끼리 묶어두고 꺼내서 비교
    '''
    
    # 빈 스택 만들기
    stack = []

    # 처음엔 성공이라고 가정하고 틀렸을 때 0으로 변경
    result = 1

    # 짝 딕셔너리 만들기
    pairs = {
        ')': '(',
        '}': '{',
        ']': '[',
        '>': '<'
        }
    # 왼쪽 괄호들만 모아두기
    open_brackets = '({[<'

    for word in N_lst:
        # 왼쪽 괄호라면
        if word in open_brackets:
            # 스택에 추가
            stack.append(word)
        
        # 오른쪽 괄호라면
        elif word in pairs:
            # 스택이 비어있거나
            # 스택의 마지막 요소를 꺼내고 딕셔너리에서 현재 닫는 괄호의 짝(pairs[word])을 바로 찾아 비교
            if not stack or stack.pop() != pairs[word]:
                result = 0
                break

    print(f'#{tc} {result}')