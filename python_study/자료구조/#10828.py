#스택
import sys
input = sys.stdin.readline
n=int(input())

num_list=[]

for i in range(n):
    command = input()
    if command.startswith("push "):
        splitted_list = command.split()
        value = int(splitted_list[1])
        num_list.append(value)
    elif command == "pop":
        if len(num_list) == 0:
            print(-1)
        else:    
            a = num_list.pop()
            print(a)
    elif command == "size":
        print(len(num_list))
    elif command == "empty":
        if len(num_list) == 0:
            print(1)
        else:
            print(0)
    elif command == "top":
        if len(num_list) == 0:
            print(-1)
        else:
            print(num_list[-1])