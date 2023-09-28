mport random

n = []

for i in range(10):
        n.append(random.randint(0, 10))

print(n)

for i in n:
        if n.count(i) > 1:
            print(i)