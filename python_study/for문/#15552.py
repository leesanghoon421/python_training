import sys

a = int(input())
for i in range(a):
        x,y = map(int, sys.stdin.readline().split())
        print(x+y)