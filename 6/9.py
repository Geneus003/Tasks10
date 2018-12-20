import math
def main():
  def square(a, b, c, d, e, f):
    ab = Len(a, b, c, d)
    bc = Len(c, d, e, f)
    ca = Len(a, b, e, f)

    p = (ab+bc+ca)/2

    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))


  def Len(a, b, c, d):
    r1 = a - c
    r2 = d - b

    print(math.sqrt(r1**2 + r2**2))

  a, b, c, d = input().split(" ")
  a, b, c, d = int(a), int(b), int(c), int(d)
  Len(a, b, c, d)

  a, b, c, d, e, f = input().split(' ')
  a, b, c = int(a), int(b), int(c)
  d, e, f = int(d), int(e), int(f)
  square(a, b, c, d, e, f)

if __name__ == "__main__":
  main()
