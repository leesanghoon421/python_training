import sys
input = sys.stdin.readline

n = int(input())
line = 1

#n이 line보다 클때까지 반복하여 n이 몇번째 line인지,
#그 line에서 n이 몇번째 수인지 조사
while n > line:
    n -= line
    line += 1

#n이 포함된 line이 짝수 라인인지 홀수 라인인지에 따라 구분
if line % 2 == 0:
    numer = n
    denom = line - n + 1
else:
    numer = line - n + 1
    denom = n

print(numer,'/',denom, sep="") #sep=""이용하여 문자간 공백 제거