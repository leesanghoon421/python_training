#n번째 영화의 제목
n=int(input())          #n입력
cnt=0                   #counter변수 0으로 초기화
num=666                 #666부터 전수조사를 위해 num을 666으로 초기화

while True:
    #num을 string으로 바꿔서 666이 포함이 되어있으면 counting진행
    if "666" in str(num):
        cnt+=1
    #counter가 입력한 n과 일치하면 num을 출력
    if cnt==n:
        print(num)
        break  #목표값을 찾으면 전수조사 종료
    num+=1     #반복문이 진행될때마다 num을 1씩커지게해서 전수조사 진행