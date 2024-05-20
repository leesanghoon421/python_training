#for문을 이용한 방법1
n = int(input())
number = input()
result = 0

for i in range (n):
    result += int(number[i])
print(result)

#for문을 이용한 방법2
n = input()
nums = input()
total = 0
for i in nums :
    total += int(i)
print(total)

#for문을 이용하지 않고 sum함수를 이용하여 더욱더 간결한 코드작성가능
n = input()

print(sum(map(int, input())))