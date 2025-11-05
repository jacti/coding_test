

def solution(n, times):
    
    def search(l, r, v):
        # print(l, r, v)
        if l == r:
            return l
        n = 0
        mid = (l + r)//2
        for t in times:
            n += mid//t
        if n >= v:
            return search(l,mid,v)
        else:
            return search(mid+1,r,v)
    
    answer = search(0, n*max(times), n)
    
    return answer