import sys
input = sys.stdin.readline

n, m = map(int,input().split())

pkm_list={}                     #딕셔너리 타입을 이용하여 포켓몬 도감 구성

for i in range(1, n+1):         #n개의 포켓몬을 도감에 기록
    pkmon = input().rstrip()    #우측 공백 제거
    #key로 value를 찾는 경우와 value로 key를 찾는 경우가 모두 존재하니 두가지 방향으로 저장
    pkm_list[i] = pkmon         
    pkm_list[pkmon] = i

for i in range(m):              #m개의 문제 풀이
    ans = input().rstrip()      #우측 공백 제거
    if ans.isdigit():           #ans string이 숫자로만 구성되어있는 경우
        print(pkm_list[int(ans)])   #ans를 integer type으로 바꿔주고 조사하여 value출력
    else:
        print(pkm_list[ans])        #ans를 string type 그대로 조사하여 key출력