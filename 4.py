import random
n = []

for i in range(10):
        n.append(random.randint(0, 100))
print(n)

a = 0
b = 1

for i in n:
        a += i
        b *= i

print(a)
print(b)