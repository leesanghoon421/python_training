n = int(input())        #색종이 수 입력
num_list = [[0] * 100 for _ in range(100)]  #0으로 채워진 100 by 100 2차원 배열 생성

for _ in range(n):      #색종이 수 만큼 반복
    x,y=map(int,input().split())    #색종이의 좌하단 점 입력
    
    #색종이의 좌하단 점으로부터 우상단으로 10 by 10 색종이가 걸치는 좌표의 값을 1로 설정
    for i in range(10):             
        for j in range(10):
            num_list[x+i][y+j] = 1

ans = 0     #결과 값을 0으로 세팅

#열을 기준으로 값이 1인 좌표들을 counting하여 그 수만큼 ans에 더해줌
for a in num_list:
    ans+=a.count(1)
        
print(ans)