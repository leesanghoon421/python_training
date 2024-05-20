import math

while True:
    n = int(input())
    if n == 0:
        break
    
    prime_num = 0
    
    for i in range(n+1, n*2+1):
        if i == 1:
            continue
        elif i == 2:
            prime_num += 1
            continue
        else:
            for j in range(2, int(math.sqrt(i)+1)):
                if i % j == 0:
                    break
            else:
                prime_num += 1
    print(prime_num)