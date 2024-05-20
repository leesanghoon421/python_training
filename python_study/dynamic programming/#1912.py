n=int(input())

num = list(map(int,input().split()))

sum_list=[num[0]]

for i in range(len(num) - 1):
    sum_list.append(max(sum_list[i] + num[i + 1], num[i + 1]))
    
print(max(sum_list))