#N,M 입력
N,M=map(int,input().split())

#빈 리스트 만들어둠
s = []

#dfs기반의 함수
def dfs():
    #s의 길이가 M이되면 입력중지하고 출력해줌
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    #s의 길이가 M이 아닌경우 N회 반복
    for i in range(1, N + 1):
        if i in s:  #이미 존재하는 수인 경우 넘어감
            continue
        s.append(i) #리스트에 수 입력
        dfs()       #재귀호출
        s.pop()     #재귀호출 종료되면 제거
        
dfs()   #함수실행