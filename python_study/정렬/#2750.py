N=int(input())
list1=[]

for i in range(N):
    list1.append(int(input()))
list1.sort()

for i in range(N):
    print(list1[i])