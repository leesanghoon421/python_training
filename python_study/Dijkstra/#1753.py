import sys
import heapq
input = sys.stdin.readline  #시간초과 방지
INF = 10000000000       #무한을 상징

V,E = map(int, input().split())     #정점, 간선 개수 입력
K = int(input())                    #시작 정점 입력
graph = [[] * (V+1) for _ in range(V+1)]    #그래프 초기화
for _ in range(E):          #간선 정보 입력
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) #u->v경로의 가중치w

distance = [INF]*(V+1)      #최단 거리 테이블 무한으로 초기화

q = []      #우선순위 큐로 이용할 array
def dijkstra(start):        #Dijkstra Algorithm
    distance[start] = 0     #start->start를 0으로 설정
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)     #최단거리가 가장 짧은 노드의 정보pop
        #현재 노드와 연결된 다른 노드들과의 distance 확인
        for i, weight in graph[now]:  #i에 인덱스 weight에 원소 입력
            cost = dist + weight
            if cost < distance[i]:   #현재 노드를 거치는게 더 짧은 경우
                distance[i] = cost   #distance에 새로운 cost 갱신
                heapq.heappush(q,(cost,i)) #그후에 queue에 push

dijkstra(K)        #다익스트라 알고리즘 수행

for i in distance[1:]:  #최단거리 테이블 조사
    if i != INF:
        print(i)
    else:
        print("INF")