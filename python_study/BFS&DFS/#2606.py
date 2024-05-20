import sys
input=sys.stdin.readline

num=int(input())    # 컴퓨터의 수 입력
net=int(input())    # 연결된 컴퓨터쌍의 수
pc=[0 for _ in range(num+1)]    # 컴퓨터수+1개의 0으로 이루어진 pc리스트 생성
pc[1]=1     # 감염시킬 1번 컴퓨터를 1로 세팅

for i in range(net):
    a,b=map(int,input().split())
    if (pc[a]==1 or pc[b]==1):  # 연결된 컴퓨터중 한대라도 감염되어있다면
        # 전부 감염됨
        pc[a]=1
        pc[b]=1
# 1번 컴퓨터로 인해 감염된 컴퓨터의 수 출력
print(pc.count(1)-1)