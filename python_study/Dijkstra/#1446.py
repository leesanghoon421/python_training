import heapq
import sys
input = sys.stdin.readline

INF = 1000000000
sc_num, total_distance = map(int,input().split())
graph = [[] for _ in range(total_distance+1)]
distance = [INF] * (total_distance+1)

#거리 1로 초기화
for i in range(total_distance):
    graph[i].append((i+1, 1))

#지름길 있는 경우에 업데이트
for _ in range(sc_num):
    sc_start, sc_end, sc_length = map(int,input().split())
    #지름길 도착 위치가 총 길이 보다 길면 고려하지 않음
    if sc_end > total_distance:
        continue
    graph[sc_start].append((sc_end,sc_length))

#다익스트라 알고리즘 기본 함수 이용
def dijkstra(start):
    queue = []
    distance[start] = 0                 #시작 값은 0으로 설정
    heapq.heappush(queue,(0,start))     #시작 노드부터 탐색

    while queue:    #queue에 남은 노드가 없으면 반복문 종료
        cur_distance, cur_destination = heapq.heappop(queue)    #탐색할 노드와 거리 가져옴
        #현재 거리가 기존의 거리보다 크면 고려하지 않음
        if cur_distance > distance[cur_destination]:
            continue

        for i in graph[cur_destination]:
            cost = cur_distance + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost, i[0]))

dijkstra(0)
print(distance[total_distance])