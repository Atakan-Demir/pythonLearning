import random
d={}
k = 0
for i in range(1,4):
    for j in range(1,4):
        d[i,j] = random.randint(1,9)

        k += 1
        if k > 3:
            print()
            k = 1
        print("%3d   " % d[i, j], end="")


print()
print()
print("*****************")
print()

s={}
k = 0
for i in range(1,4):
    for j in range(1,4):
        s[i,j] = random.randint(1,9)

        k += 1
        if k > 3:
            print()
            k = 1
        print("%3d   " % s[i, j], end="")


print()
print()
print("+++++++++++++++++")
print()

t={}
k = 0
for i in range(1,4):
    for j in range(1,4):
        t[i,j] = d[i,j] + s[i,j]

        k += 1
        if k > 3:
            print()
            k = 1
        print("%3d   " % t[i, j], end="")


