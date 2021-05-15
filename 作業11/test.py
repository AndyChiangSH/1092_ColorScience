import os
dirPath = r"D: \雲端\NCHU\大二\大二下\色彩科學導論\作業\作業11\11-Images\Decry_image"
result = [f for f in os.listdir(
    dirPath) if os.path.isfile(os.path.join(dirPath, f))]
print(result)
