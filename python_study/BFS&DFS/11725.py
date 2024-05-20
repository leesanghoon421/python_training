import sys
sys.setrecursionlimit(10**9)    # 재귀의 깊이 제한을 풀어줌
input=sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n+1)]  # 빈 2차원 리스트 graph생성
checked=[0 for _ in range(n+1)] # 0으로 채워진 2차원 리스트 checked생성
answer=[1 for _ in range(n+1)]  # 1으로 채워진 2차원 리스트 answer생성

# dfs 인접노드 체크 함수
def dfs(node):
    checked[node]=1 # 체크하는 노드를 체크완료 표시로 1을 입력
    for i in graph[node]:
        if checked[i] == 0: # 인접노드가 0(미확인)이면
            answer[i]=node  # 해당 노드에 대한 answer를 입력 노드로 설정하여 입력노드가 인접노드의 상위 노드임을 나타냄
            dfs(i)  #재귀 호출
    return

for i in range(n-1):
    node1,node2=map(int,input().split())
    # 인접목록 graph를 업데이트
    graph[node1].append(node2)  # node1의 이웃 목록에 node2를 추가
    graph[node2].append(node1)  # node2의 이웃 목록에 node1를 추가

# 1을 루트로 지정하여 dfs 함수 실행
dfs(1)

# 2부터 answer list의 길이만큼 반복
for i in range(2,len(answer)):
    print(answer[i])