a,b,c=map(int,input().split())
cnt = 0

while True:
    cnt += 1
    if b>=c:
        print(-1)
        break
    if a+(b*cnt) < c*cnt:
        print(cnt)
        break