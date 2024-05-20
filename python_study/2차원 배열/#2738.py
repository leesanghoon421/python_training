a, b = map(int, input().split())

list1=[]
list2=[]

for i in range (a):
    x=list(map(int, input().split()))
    list1.append(x)
    
for i in range (a):
    y=list(map(int, input().split()))
    list2.append(y)
    
for row in range (a):
    for col in range (b):
        print(list1[row][col]+list2[row][col], end=' ')
    print()