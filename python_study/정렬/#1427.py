number = int(input())
a = []
for i in str(number):
    a.append(int(i))
a.sort(reverse=True)
for x in a:
    print(x, end="")