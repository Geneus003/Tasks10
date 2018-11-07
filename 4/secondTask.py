n = int(input())

def findSum(k):
  k = str(k)
  sumka = 0
  for i in range(len(k)):
    sumka += int(k[len(k)-i - 1])

  return sumka

while len(str(n)) != 1:
  n = findSum(n)

print(n)
