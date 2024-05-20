num_list=[1,1,1,2,2]

n = int(input())

for i in range(n):
    a = int(input())
    for j in range(len(num_list), a):
        new_num=num_list[j-1]+num_list[j-5]
        num_list.append(new_num)
    print(num_list[a-1])

'''
--------실제 파도반 수열 점화식 이용--------
pdb = [0 for i in range(101)]
pdb[1] = 1
pdb[2] = 1
pdb[3] = 1
for i in range(0, 98):
    pdb[i + 3] = pdb[i] + pdb[i + 1]
t = int(input())
for i in range(t):
    n = int(input())
    print(pdb[n])
'''