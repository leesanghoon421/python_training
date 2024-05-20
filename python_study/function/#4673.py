base_num = set(range(1,10001))
generated_num = set()
add=0
for j in range(1, 10001):
    for i in str(j):
        j += int(i)
    generated_num.add(j)
    
self_num = sorted(base_num - generated_num)

for j in self_num:
    print(j)