import random


list_rand = []
a = 0
for i in range(20):
    a += 10
    rx = random.randint(10,1000)
    ry = random.randint(10,500)
    list_rand.append(((rx + a),(ry + a)))
print(list_rand)