# Exchange output of encrypt to input of decrypt

# load text
with open("text/ART-ENC-output08.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("text/ART-DEC-input08.txt", "w", encoding="utf-8") as f:
    for line in lines:
        items = line.split(" ")
        file_name = items[0]
        art = items[1]
        art_number = int(items[2])
        period = int(items[3])

        if art == "+":
            art = "-"
        else:
            art = "+"

        f.write(f"{file_name} {art} {art_number} {period}\n")
