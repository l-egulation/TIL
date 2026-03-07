bracket = list(input())

# 빈 스택 만들기
stack = []
# 결과 값
result = 0
# 분배법칙을 위한 임시 변수
temp = 1

for i in range(len(bracket)):
    if bracket[i] == '(':
        stack.append(bracket[i])
        temp *= 2

    elif bracket[i] == '[':
        stack.append(bracket[i])
        temp *= 3

    elif bracket[i] == ')':
        # 스택이 비어있거나 짝이 맞지 않으면 실패
        if not stack or stack[-1] != '(':
            result = 0
            break

        # 바로 앞이 '(' 였다면 온전한 괄호쌍이므로 결과에 더함
        if bracket[i-1] == '(':
            result += temp

        # 괄호가 닫혔으므로 스택에서 빼고 temp를 2로 나눔
        stack.pop()
        temp //= 2

    elif bracket[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if bracket[i-1] == '[':
            result += temp
        stack.pop()
        temp //= 3

# 모든 검사가 끝난 후 스택에 괄호가 남아있다면 잘못된 괄호열!
if stack:
    print(0)
else:
    print(result)