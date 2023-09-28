n = int(input(' число = '))  

b = []

for i in range(n):
    a = int(input('число '))
    b.append(a)

del b[1::2]

print(b)