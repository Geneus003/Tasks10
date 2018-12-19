def from10ToP(ch, p):
  res, k = 0, 1
  while ch > 0:
    res += k * (ch % p)
    k *= 10
    ch //= p
  print(res)

def fromPTo10(ch, p):
  ch = str(ch)
  print(int(ch, p))

def from8To2(ch):
  ch = int(ch, 8)
  ch = bin(ch)
  print(ch[2:])
  
ch = int(input())
p = int(input())
from10ToP(ch, p)
ch = int(input())
p = int(input())
fromPTo10(ch, p)

ch = input()
from8To2(ch)
