from fractions import gcd
m = []
gcdd = 0
b = int(input())
c = int(input())

gcdd = gcd(b, c)
while True:
  a = int(input())
  if a == 0:
    break
  gcdd = gcd(gcdd, a)

print(gcdd)
