# Color science hw11 - Encryption Metrics-1
import os
import cv2
import math
import csv
import numpy as np

if __name__ == "__main__":

    with open('01_Airplane_R.csv', 'w', newline='') as csvfile:
        # build CSV writer
        writer = csv.writer(csvfile)

        img = cv2.imread("13-Images/Origi_image/01_Airplane.bmp")

        if img is None:
            print("Can't read this image...")
        else:
            print(img[:, :, 2])
            writer.writerows(img[:, :, 2])

    with open('01_Airplane_G.csv', 'w', newline='') as csvfile:
        # build CSV writer
        writer = csv.writer(csvfile)

        img = cv2.imread("13-Images/Origi_image/01_Airplane.bmp")

        if img is None:
            print("Can't read this image...")
        else:
            print(img[:, :, 1])
            writer.writerows(img[:, :, 1])

    with open('01_Airplane_B.csv', 'w', newline='') as csvfile:
        # build CSV writer
        writer = csv.writer(csvfile)

        img = cv2.imread("13-Images/Origi_image/01_Airplane.bmp")

        if img is None:
            print("Can't read this image...")
        else:
            print(img[:, :, 0])
            writer.writerows(img[:, :, 0])
