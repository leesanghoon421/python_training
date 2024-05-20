t=int(input())
for i in range(t):
    r,s=input().split()
    word = ""
    for i in s:
        word += int(r)*i
    print(word)