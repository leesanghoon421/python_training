#물이 새는 곳의 개수 n과 테이프의 길이 l을 입력받음
n,l = map(int,input().split())
#물이 새는 위치인 pos를 list에 입력받음
pos = list(map(int,input().split()))

#물이 새는 위치가 정렬이 안되어있을 수 있으니 정렬을 해줌
pos.sort()
#양옆으로 0.5만큼 커버해야하니 start를 pos[0]보다 0.5만큼 왼쪽으로 잡음
start = pos[0] - 0.5
count = 1   #카운터 설정(테이프 개수)

#for문 이용하여 그리디 알고리즘 실행
for i in range(1, len(pos)):
#기존의 테이프로 다음 새는 곳이 커버가 된다면 새로운 테이프 이용
    if start + l >= pos[i] + 0.5:
        continue
#커버가 안되면 스타트 포인트를 새로 설정해주고 counting 진행
    else:
        start = pos[i] - 0.5
        count += 1

print(count)