# Color science hw10 - Determining Secret Keys for 2D Arnold Cat Map
from decimal import *
import random
import math

getcontext().prec = 21

# read input.txt
with open("input10.txt", "r") as file:
    line = file.readline().split(" ")
    x0 = Decimal(line[0])
    rx = Decimal(line[1])

    line = file.readline().split(" ")
    y0 = Decimal(line[0])
    ry = Decimal(line[1])

    line = file.readline().split(" ")
    seed = int(line[0])
    N = int(line[1])

    line = file.readline()
    L = Decimal(line)

# print(x0)
# print(rx)
# print(y0)
# print(ry)
# print(seed)
# print(N)
# print(L)

# calculate R1, R2, R3
random.seed(seed)
R1 = int(random.random()*N+1)
R2 = int(random.random()*N+1)
R3 = int(random.random()*N+1)

# print(R1)
# print(R2)
# print(R3)

# calculate xn, yn
xn = x0
for i in range(R1):
    xn = rx*xn*(1-xn)

yn = y0
for i in range(R2):
    yn = ry*yn*(1-yn)

# print(xn)
# print(yn)

# calculate a, b
a = R1 + math.ceil(xn/L)
b = R2 + math.ceil(yn/L)

# print(a)
# print(b)

# write file
with open("output10.txt", "w") as file:
    file.write(f"{x0} {rx}\n")
    file.write(f"{y0} {ry}\n")
    file.write(f"{seed} {N}\n")
    file.write(f"{L}\n")
    file.write(f"{R1} {R2} {R3}\n")
    file.write(f"{xn} {yn}\n")
    file.write(f"{a} {b}\n")
