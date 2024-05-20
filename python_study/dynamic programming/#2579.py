#계단 수 입력
n = int(input())

#계단 세팅
stair = [0]*301
for i in range(n):
    stair[i] = int(input())

#점수를 담아둘 리스트
point_set = [0]*301
#1칸인 경우
point_set[0] = stair[0]
#2칸인 경우
point_set[1] = stair[0]+stair[1]
#3칸인 경우
point_set[2] = max(stair[0]+stair[2], stair[1]+stair[2])

#4칸이상인 경우
for i in range(3, n):
#n-3칸까지의 최대값과 최종 두계단의 합과 n-2칸까지의 합과 최종 계단 둘중 큰 값을 point_set[n]에 저장
    point_set[i] = max(point_set[i-3] + stair[i-1] + stair[i], point_set[i-2]+stair[i])

#인덱스로 호출하므로 n개의 계단이면 n-1을 출력
print(point_set[n-1])