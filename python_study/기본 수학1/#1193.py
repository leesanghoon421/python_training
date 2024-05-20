import sys
input = sys.stdin.readline

numer_list = []
denom_list = []
numer = 1
denom = 1
trigger = 0

n = int(input())

for i in range(n):
    numer_list.append(numer)
    denom_list.append(denom)
    if (numer == 1) and (trigger == 0):
        denom += 1
        trigger = 1
    elif (denom == 1) and (trigger== 0):
        numer += 1
        trigger = 1
    else:
        if (numer + denom) % 2 == 1:
            numer += 1
            denom -= 1
            if denom == 1:
                trigger = 0
        else:
            numer -= 1
            denom += 1
            if numer == 1:
                trigger = 0
                

print(str(numer_list[n-1]) + '/' + str(denom_list[n-1]))