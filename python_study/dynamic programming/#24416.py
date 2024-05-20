n = int(input())
cnt2 = 1

def fib2(n):
    global cnt2
    f = [1,1] + [0]*(n-1)
    for i in range(2,n-1):
        f[i] = f[i - 1] + f[i - 2]
        cnt2 = cnt2 + 1
    return cnt2

print(n-2, fib2(n))