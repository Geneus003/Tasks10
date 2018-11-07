n = int(input())

def fact(k):
    factorial = 1
    for i in range(1, k+1):
        factorial *= i

    return factorial

s = 0
for i in range(1, n+1):
    s += ((i*i) / fact(i))

print("%8.3f"%s)
