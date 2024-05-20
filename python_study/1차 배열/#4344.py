'''
from array import array


num=int(input())


for i in range(num):
    a=int(input())
    i=[]
    for j in range(a):
        array1=[]
        score=int(input())
        array1.append(score)
    sum1=array1.sum()
    everage1=sum1/a
    for k in range(a):
        if score>everage1:
            i.append(score)
    print('0.3f' %len(i)/a)
    '''
  

num = int(input())

for i in range(num):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:])/scores[0]
    
    cnt = 0
    for j in scores[1:]:
        if j > avg:
            cnt += 1
            
    per = (cnt/scores[0])*100
    print('%.3f' %per + '%')