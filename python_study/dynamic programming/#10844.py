import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]

# 1부터 9까지의 수로 첫번째 배열을 채움
for i in range(1,10):
    dp[1][i] = 1

# dp[n자리 수][n자리 숫자일 때 해당 index 앞에 올 수 있는 일의 자리 수]
# 2 자리수부터 시작
for i in range(2, n+1):
    for j in range(10): # index기반으로 전부 조사
        # 뒷자리가 0일 때는 이전에 한가지 경우의 합으로 구함
        if j == 0 : dp[i][j] = dp[i-1][j+1]
        # 뒷자리가 9일 때는 이전에 한가지 경우의 합으로 구함
        elif j == 9 : dp[i][j] = dp[i-1][j-1]
        # 뒷자리가 2~8일 때는 이전에 두가지 경우의 합으로 구함
        else : dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

# overflow를 막기 위해 문제에서 요구한대로 1000000000으로 나눈 나머지를 출력
print(sum(dp[n]) % 1000000000)