num = int(input())  #학생 수 입력
slist = []          #학생 스펙 리스트
anslist=[]          #덩치 등수 리스트

for i in range(num):
    w, h = map(int, input().split())    #무게와 키를 입력받음
    slist.append((w, h))                #학생 스펙 리스트에 입력함

#브루트포스 알고리즘 진행
for a in slist:      #등수 지정할 학생 지정
    rank = 1         #초기 등수는 1로 시작
    for b in slist:                 #비교대상 학생 지정
        if a[0]<b[0] and a[1]<b[1]: 
            rank+=1         #비교대상보다 덩치가 작으면 등수 상승
    anslist.append(rank)            #등수를 덩치 등수 리스트에 입력

print(*anslist)         #출력할때는 []와 ,를 제외시키고 내용만 출력