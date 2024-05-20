n = int(input())
cnt = 0

for i in range(1,n+1):
    check = list(map(int,str(i)))
    cnt += check.count(3)
    cnt += check.count(6)
    cnt += check.count(9)

print(cnt)