n = input()
con = round(len(n) / 2)

print(n[con + len(n) % 2: len(n)], end = "")
print(n[0: con + len(n) % 2]) 
