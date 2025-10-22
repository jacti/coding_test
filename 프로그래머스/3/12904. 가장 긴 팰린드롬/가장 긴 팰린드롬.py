# 일단 완전 탐색으로 ㄱㄱ

def solution(s):
    answer = 1
    N = len(s) -1
    for i in range(1,N):
        count = 1
        l, r = i-1, i+1
        while l >= 0 and r <= N:
            if s[l] != s[r]:
                break
            count +=2
            l -=1
            r +=1
            
        if count > answer:
            answer = count
            
    for l in range(N):
        r = l+1
        count = 0
        while l >= 0 and r <= N:
            if s[l] != s[r]:
                break
            count +=2
            l -=1
            r +=1
            
        if count > answer:
            answer = count

    return answer