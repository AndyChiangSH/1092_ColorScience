# Color science hw11 - Encryption Metrics-1
import os

# relative pathname of Decry_images
dirPath = r"11-Images/Decry_image/"
d_images = next(os.walk(dirPath))[2]
print(d_images)

# relative pathname of Encry_images
dirPath = r"11-Images/Encry_image/"
e_images = next(os.walk(dirPath))[2]
print(e_images)

# relative pathname of Origi_images
dirPath = r"11-Images/Origi_image/"
o_images = next(os.walk(dirPath))[2]
print(o_images)
