import math                         #삼각함수와 pi를 이용하기 위해 math 모듈 import
import matplotlib.pyplot as plt     #pip install matplotlib을 통하여 미리 module install

N = int(input())        #예삿값을 구하기 위한 N을 입력
INF = 10000             #1번에서 N값이 10000이상이면 N이 무한대인 x(t)와의 차이를 육안으로 구별하기 힘듬을 확인
t = 0               
graph = []          #empty 리스트 생성

def x_hat_n(t):       #x_hat_n(t)의 결과를 구하는 sigma 함수 define
    n = 1           #n -> 1~N
    sum = 0.0
    while n < N:    #n이 N보다 작은 경우에 
        sum += (4.0 / math.pi) * (1 / n) * math.sin(n * math.pi * float(t))     #x(t)식 계산
        n += 2      #n에 홀수값 대입
    return sum

def x(t):       #x(t)의 결과를 구하는 sigma 함수 define
    n = 1           #n -> 1~INF
    sum = 0.0
    while n < INF:    #n -> INF
        sum += (4.0 / math.pi) * (1 / n) * math.sin(n * math.pi * float(t))     #x(t)식 계산
        n += 2      #n에 홀수값 대입
    return sum

def e_n(t):     #x(t)와 x_hat_n(t)의 차를 구하는 e_n(t)함수 define
    result = x(t) - x_hat_n(t)
    return result

while t <= 2000:             #t를 0.005로 설정하면 계산상 오류가 발생할 수 있어 t를 0~2000, 5씩증가로 잡아줌
    graph.append(e_n(t * 0.001)) #미리 만들어둔 graph 리스트에 결과 값 입력 (1000배 해둔 t에 0.001배)
    t += 5                  #5씩 증가(실제로는 0.005)

#|eN(t)| 최대값 조사
print(graph[198])
print(graph[199])
print(graph[200])
print(graph[201])
print(graph[202])

#module을 이용하여 그래프 그리기
plt.title("e_n(t)") 
plt.plot(graph)
plt.show()