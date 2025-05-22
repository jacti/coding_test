n = int(input())

def sol(n):
    if n <100:
        return n
    elif n == 1000:
        return 144
    else:
        count = 99
        for i in range(100,n+1):
            arr = []
            for _ in range(3):
                arr.append(i%10)
                i//=10
            if arr[1] - arr[0] == arr[2] - arr[1]:
                count +=1
        return count
        
print(sol(n))