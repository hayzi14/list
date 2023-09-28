import random
n = []
for i in range(10):

        n.append(random.randint(0, 100))

a = n.copy()

maximum = n.index(max(n))

minimum = n.index(min(n))

a[maximum] = min(n)


a[minimum] = max(n)

print(n)
print(a)