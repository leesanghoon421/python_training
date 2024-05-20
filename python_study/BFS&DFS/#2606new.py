import sys
input=sys.stdin.readline

num=int(input())    # 컴퓨터의 수 입력
net_num=int(input())    # 연결된 컴퓨터쌍의 수
net = [[] for i in range(num + 1)] # 연결 상태 저장할 list
check = [] # 탐색할 컴퓨터 배열
pc = [0] * (num + 1) # 탐색한 컴퓨터 방문 확인용 배열

for i in range(net_num):
	a, b = map(int, input().split())
	net[a].append(b)    # a에는 b와 연결되었음을 저장
	net[b].append(a)    # b에는 a와 연결되었음을 저장

check.append(1) # 가장 먼저 탐색할 1번 컴퓨터 check에 삽입

while check: # check 리스트 전체 조사
    tmp = check.pop(0) # 탐색할 컴퓨터 pop해서 tmp에 담아둠
    pc[tmp] = 1 # 탐색완료
    for i in net[tmp]: # 연결된 컴퓨터 전수조사
        if pc[i] != 1: # 탐색하지 않은 경우 탐색 진행
            pc[i] = 1 # 탐색완료
            check.append(i) # check 리스트에 삽입
           #print(check) check 리스트 출력하여 중간 과정 확인
#print(net) net list 출력하여 중간 과정 확인
#print(pc) pc list 출력하여 중간 과정 확인 
print(pc.count(1)-1) # 1번 컴퓨터가 감염시킨 컴퓨터 수 출력