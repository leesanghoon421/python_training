def fibonacci(a):
    if a <= 1:
        return a
    return fibonacci(a-1) + fibonacci(a-2)

a = int(input())
print(fibonacci(a))