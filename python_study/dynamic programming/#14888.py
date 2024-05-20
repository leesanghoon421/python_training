import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())        #숫자 개수
num = list(map(int, input().split()))       #숫자 리스트
oper_num = list(map(int, input().split()))  #각 연산자 수가 담긴 리스트

oper_list = ['+', '-', '*', '/']    #연산자 리스트
oper = []

for i in range(len(oper_num)):
    for _ in range(oper_num[i]):
        oper.append(oper_list[i])

max = -1000000000   #max값이 업데이트 되는것에 방해가 되지 않도록 최소값으로 초기화
min = 1000000000    #min값이 업데이트 되는것에 방해가 되지 않도록 최대값으로 초기화

#연산하는 함수 정의
def calculation():
    global max, min
    #case문을 이용하여 조건에 따라 앞에서부터 연산진행
    for case in permutations(oper, N - 1):
        ans = num[0]
        for r in range(1, N):
            if case[r-1] == '+':
                ans += num[r]
            elif case[r-1] == '-':
                ans -= num[r]
            elif case[r-1] == '*':
                ans *= num[r]
            elif case[r-1] == '/':
                ans = int(ans/num[r])

        if ans > max:
            max = ans
        if ans < min:
            min = ans
    print(max)
    print(min)

calculation()