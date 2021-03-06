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
        logi.append(x)
        prex = x

    # calculate mean of logi
    logi_mean = statistics.mean(logi)

    # calculate standard of logi
    logi_std = statistics.pstdev(logi)

    # run default random
    rand = []
    random.seed(seed)
    for i in range(M):
        x = random.random()
        rand.append(x)

    # calculate mean of rand
    rand_mean = statistics.mean(rand)

    # calculate standard of rand
    rand_std = statistics.pstdev(rand)

    with open('output09.csv', 'w', newline='') as csvfile:
        # build CSV writer
        writer = csv.writer(csvfile)

        # write headers
        writer.writerow(["x0", "r", "M", "seed"])
        writer.writerow([x0, r, M, seed])

        # write logi and rand
        for i in range(M):
            writer.writerow([i+1, "%.6f" % logi[i], "%.6f" % rand[i]])

        # write mean and standard
        writer.writerow(["mean", "%.6f" % logi_mean, "%.6f" % rand_mean])
        writer.writerow(["std", "%.6f" % logi_std, "%.6f" % rand_std])

else:
    print("r is not in range(3.56995~4)!")
