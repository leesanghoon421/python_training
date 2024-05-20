import sys
from itertools import accumulate    #누적합 이용하기 위한 module import

input=sys.stdin.readline    #시간초과 방지

num,eat=map(int,input().split())    #파이의 수와 먹을 개수
taste=list(map(int,input().split()))    #맛있는 정도 list

sum=[0]+list(accumulate(taste))    # 0을 빼는 상황을 위해 0번 인덱스에 0입력 

Max=0   #Max를 0으로 설정하고 반복문 진입

for start in range(num):
    #조사 구간이 선형리스트 내부일때
    if start+eat<=num:
        Max = max(Max, sum[start + eat] - sum[start])
    #조사 구간이 선형리스트를 넘을때
    else:
        Max = max(Max, sum[num] - sum[start] + sum[(start + eat) - num])

print(Max)