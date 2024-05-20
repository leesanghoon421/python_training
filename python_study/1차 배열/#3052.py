array1=[]
for i in range(10):
    n=int(input())
    array1.append(n%42)
result=set(array1)
#print(result)
print(len(result))