n = int(input())
k = int(input())
m = int(input())

year = 0
while n <= m:
  n += n*k/100
  year += 1
print(year)
