import math                         #삼각함수와 pi를 이용하기 위해 math 모듈 import
import matplotlib.pyplot as plt     #pip install matplotlib을 통하여 미리 module install

N = int(input())        #예삿값을 구하기 위한 N을 입력
t = 0               
graph = []          #빈 리스트 생성

def sigma(t):       #x_hat_n(t)의 결과를 구하는 sigma 함수 정의
    n = 1           #n -> 1~N
    sum = 0.0
    while n < N:    #n이 N보다 작은 경우에 
        sum += (4.0 / math.pi) * (1 / n) * math.sin(n * math.pi * float(t))     #x(t)식 계산
        n += 2      #n에 홀수값 대입
    return sum


while t <= 2000:             #t를 0.005로 설정하면 계산상 오류가 발생할 수 있어 t를 0~2000, 5씩증가로 잡아줌
    graph.append(sigma(t * 0.001))   #미리 만들어둔 graph 리스트에 결과 값 입력 (1000배 해둔 t에 0.001배)
    t += 5                  #5씩 증가(실제로는 0.005)


#module을 이용하여 그래프 그리기
plt.title("x_hat_n(t)") 
plt.plot(graph)
plt.show()