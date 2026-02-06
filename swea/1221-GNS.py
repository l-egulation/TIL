words = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
words_dict = {}

T = int(input())

'''
문자를 숫자로 바꾸고, 숫자를 다시 문자로 바꾼다.
그럼 일단 words_lst에 있는 문자를 words에 있는 문자의 인덱스로 스위칭
> words는 정렬이 되있으니까 여기에 해당하는 인덱스로 바꾸면 words_lst가 숫자로 바뀔 것임
그 후에 숫자를 다시 words의 인덱스에 해당하는 문자로 스위칭
'''

for tc in range(1, T+1):
    trash, N = input().split()
    N = int(N)
    words_lst = list(input().split())

    # 문자 > 숫자
    for i in range(len(words_lst)):
        words_lst[i] = words.index(words_lst[i])
    
    words_lst.sort()

    # 숫자 > 문자
    for i in range(len(words_lst)):
        words_lst[i] = words[words_lst[i]]

    print(f'#{tc}')
    print(*words_lst)