# 4108056005 江尚軒 - Arnold's Cat Map(Decrypting)

from PIL import Image
import numpy as np
import os

# load text
with open("text/ART-DEC-input08.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("text/ART-DEC-output08.txt", "w", encoding="utf-8") as f:
    pass

for line in lines:
    items = line.split(" ")
    file_name = items[0]
    art = items[1]
    art_number = int(items[2])
    period = int(items[3])
    new_file_name = file_name.split("_")[1]

    print(file_name)
    # print(new_file_name)

    # choose the shortest path
    back = period-art_number
    if art_number > back:
        art_number = back
        if art == "+":
            art = "-"
        else:
            art = "+"

    print(f"{art}{art_number}")

    # load image
    im = np.array(Image.open(f"encrypt/{file_name}"))
    N = im.shape[0]

    # create x and y components of Arnold's cat mapping
    y, x = np.meshgrid(range(N), range(N))
    if art == "+":
        xmap = (x+y) % N
        ymap = (x+2*y) % N
    else:
        xmap = (2*x-y) % N
        ymap = (-x+y) % N

    for i in range(art_number):
        im = im[xmap, ymap]

    if not os.path.exists("decrypt"):
        os.mkdir("decrypt")
    result = Image.fromarray(im)
    result.save(f"decrypt/{new_file_name}")

    with open("text/ART-DEC-output08.txt", "a", encoding="utf-8") as f:
        f.write(f"{new_file_name}\n")
