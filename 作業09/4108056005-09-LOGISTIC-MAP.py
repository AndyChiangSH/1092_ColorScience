# Color science hw09 - Logistic map

from decimal import Decimal
import statistics
import random
import csv

# read input file
with open("input09.txt", "r") as file:
    var = file.readline().split(" ")

x0 = float(var[0])
r = float(var[1])
M = int(var[2])
seed = int(var[3])

# print(x0, r, M, seed)

# Foolproof for r
if r > 3.56995 and r <= 4:
    # run logistic map
    logi = []
    prex = x0
    for i in range(M):
        x = r*prex*(1-prex)

        # Round to six decimal places
        # d = Decimal(str(x))
        # d = float(round(d, 6))

        logi.append(x)
        prex = x

    # i = 1
    # for s in logi:
    #     print(i, s)
    #     i += 1

    # calculate mean of logi
    logi_mean = statistics.mean(logi)
    # print(logi_mean)

    # calculate standard of logi
    logi_std = statistics.pstdev(logi)
    # print(logi_std)

    # run default random
    rand = []
    random.seed(seed)
    for i in range(M):
        x = random.random()
        rand.append(x)

    # i = 1
    # for s in rand:
    #     print(i, s)
    #     i += 1

    # calculate mean of rand
    rand_mean = statistics.mean(rand)
    # print(rand_mean)

    # calculate standard of rand
    rand_std = statistics.pstdev(rand)
    # print(rand_std)

    with open('output09.csv', 'w', newline='') as csvfile:
        # build CSV writer
        writer = csv.writer(csvfile)

        # write headers
        writer.writerow(["x0", "r", "M", "seed"])
        writer.writerow([x0, r, M, seed])

        # write logi and rand
        for i in range(M):
            writer.writerow([i+1, logi[i], rand[i]])

        # write mean and standard
        writer.writerow(["mean", logi_mean, rand_mean])
        writer.writerow(["std", logi_std, rand_std])

else:
    print("r is not in range(3.56995~4)!")
