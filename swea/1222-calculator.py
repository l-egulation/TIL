import sys

input = sys.stdin.readline

def solve(tc):
    _ = input() # 문자열 길이 (사용하지 않음)
    expression = input().strip()
    
    # --- 1단계: 중위 표기법 -> 후위 표기법 변환 ---
    stack = []
    postfix = ""
    
    # isp(in-stack priority): 스택 안에서의 우선순위
    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    # icp(in-coming priority): 스택 밖(입력)에서의 우선순위
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

    for char in expression:
        # 1. 숫자라면 바로 추가
        if '0' <= char <= '9':
            postfix += char
        
        # 2. 닫는 괄호라면 여는 괄호를 만날 때까지 pop
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop() # 남아있는 '(' 제거
            
        # 3. 연산자(괄호 포함)라면 우선순위 비교
        else:
            # 스택 탑의 isp가 현재 문자의 icp보다 크거나 같으면 pop
            while stack and isp[stack[-1]] >= icp[char]:
                postfix += stack.pop()
            stack.append(char)
            
    while stack:
        postfix += stack.pop()

    # --- 2단계: 후위 표기법 계산 (이 부분은 이전과 동일합니다!) ---
    calc_stack = []
    for char in postfix:
        if '0' <= char <= '9':
            calc_stack.append(int(char))
        else:
            op2 = calc_stack.pop()
            op1 = calc_stack.pop()
            if char == '+': calc_stack.append(op1 + op2)
            elif char == '-': calc_stack.append(op1 - op2)
            elif char == '*': calc_stack.append(op1 * op2)
            elif char == '/': calc_stack.append(op1 / op2)

    print(f"#{tc} {calc_stack[0]}")

# SWEA 형식에 맞게 10번 반복
for tc in range(1, 11):
    solve(tc)