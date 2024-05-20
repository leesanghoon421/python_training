import sys
input = sys.stdin.readline

n = int(input())    # 수열의 크기 입력
num_list = list(map(int,input().split()))   # 수열을 이루는 숫자 입력
# dp 리스트 생성
dp = [0 for _ in range(n)]
# 이중 for문을 이용하여 증가수열 관리
for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
    
print(max(dp))  # 최대 증가수열의 크기 출력