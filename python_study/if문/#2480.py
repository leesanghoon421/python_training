a,b,c=map(int,input().split())

if a==b==c:
    print(10000+1000*a)
elif a==b!=c:
    print(1000+100*a)
elif a!=b==c:
    print(1000+100*b)
elif a==c!=b:
    print(1000+100*a)
else:
    print(100*max(a,b,c))
