T = int(input())

for tc in range(1, T+1):
    lst = list(input())

    '''
    스택에 왼쪽 괄호를 저장해두고 오른쪽 괄호를 만날때마다 스택에서 마지막 요소를 꺼내서 검증
    > 맞는 짝이라면 성공, 아니라면 실패
    
    스택에 남아있어도 실패
    > 짝이 안맞아서 남는 것

    스택은 후입선출이기에 괄호의 짝 검사가 가능
    > 괄호는 가장 늦게 나온 괄호가 나중에 닫힐때는 먼저 나오기 때문
    '''
    
    # 빈 스택 만들기
    stack = []

    # 처음엔 성공이라고 가정하고 틀렸을 때 0으로 변경
    result = 1

    for word in lst:
        # 왼쪽 괄호를 만나면 스택에 삽입
        if word == '(' or word == '{':
            stack.append(word)

        # 오른쪽 괄호를 만나면 짝을 검사
        elif word == ')':
            # 스택이 비었거나 마지막 요소가 짝이 아니라면 결과를 실패로 바꾸고 break
            if not stack or stack.pop() != '(':
                result = 0
                #이미 실패라 다 볼 필요가 없음
                break

        elif word == '}':
            if not stack or stack.pop() != '{':
                result = 0
                break

    # 마지막까지 조사해서 스택에 괄호가 남아있으면 실패
    if stack:
        result = 0

    print(f'#{tc} {result}')