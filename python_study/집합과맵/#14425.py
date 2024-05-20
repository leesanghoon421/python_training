import sys
N, M = map(int, input().split())
words = dict()
cnt = 0
for i in range(N):
    a = sys.stdin.readline()
    words[a] = True
for j in range(M):
    b = sys.stdin.readline()
    if b in words.keys():
        cnt+=1
print(cnt) 