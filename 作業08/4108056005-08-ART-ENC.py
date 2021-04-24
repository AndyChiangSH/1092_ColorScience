# 4108056005 江尚軒 - Arnold's Cat Map(Encrypting)

from PIL import Image
import numpy as np
import os

# load text
with open("text/ART-ENC-input08.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("text/ART-ENC-output08.txt", "w", encoding="utf-8") as f:
    pass

for line in lines:
    items = line.split(" ")
    file_name = items[0]
    art = items[1]
    art_number = int(items[2])
    new_file_name = f"ART{art}{art_number}_{file_name}"

    print(file_name)

    # load image
    im = np.array(Image.open(f"image/{file_name}"))
    ori = im
    N = im.shape[0]

    # create x and y components of Arnold's cat mapping
    y, x = np.meshgrid(range(N), range(N))
    if art == "+":
        xmap = (x+y) % N
        ymap = (x+2*y) % N
    else:
        xmap = (2*x-y) % N
        ymap = (-x+y) % N

    for i in range(N+1):
        im = im[xmap, ymap]
        if i+1 == art_number:
            if not os.path.exists("encrypt"):
                os.mkdir("encrypt")
            result = Image.fromarray(im)
            result.save(f"encrypt/{new_file_name}")
        if np.array_equal(im, ori):
            break

    period = i+1
    print(period)

    with open("text/ART-ENC-output08.txt", "a", encoding="utf-8") as f:
        f.write(f"{new_file_name} {art} {art_number} {period}\n")
