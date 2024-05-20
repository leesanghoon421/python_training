a = int(input())
num_list = [0,1]

for i in range(2, a+1):
    num = num_list[i-1] + num_list[i-2]
    num_list.append(num)
print(num_list[num])
