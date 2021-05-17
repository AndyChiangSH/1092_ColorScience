# Color science hw11 - Encryption Metrics-1
import os
import cv2
import matplotlib.pyplot as plt
import math
import csv


def image_process(img_path):

    img = cv2.imread(img_path)

    if img is None:
        print("Can't read this image...")
    else:
        # image shape: (H, V, rgb)
        H, V, channels = img.shape

        # Part1: Mean of Image
        mi = img.mean(axis=0).mean(axis=0)

        # Part2: Variance of Histogram
        vh = list()
        for chn in range(3):
            hist = cv2.calcHist([img], [chn], None, [256], [0, 256])
            h_sum = 0
            for i in range(256):
                h_sum += pow(hist[i][0], 2)

            vh.append((h_sum/256.0)-pow((H*V/256.0), 2))

        # Part3: Shannon Entropy
        se = list()
        for chn in range(3):
            s_sum = 0.0
            hist = cv2.calcHist([img], [chn], None, [256], [0, 256])

            for i in range(256):
                if hist[i][0] != 0:
                    pz = hist[i][0]/float(H*V)
                    s_sum += pz*(math.log(pz, 2))

            se.append(-(s_sum))

        # 0:Blue 1:Green 2:Red
        return [mi[2], mi[1], mi[0], vh[2], vh[1], vh[0], se[2], se[1], se[0]]


if __name__ == "__main__":
    # relative pathname of Decry_images
    dir_path = r"11-Images/Decry_image/"
    d_images = next(os.walk(dir_path))[2]
    # print(d_images)

    # relative pathname of Encry_images
    dir_path = r"11-Images/Encry_image/"
    e_images = next(os.walk(dir_path))[2]
    # print(e_images)

    # relative pathname of Origi_images
    dir_path = r"11-Images/Origi_image/"
    o_images = next(os.walk(dir_path))[2]
    # print(o_images)

    with open('output11.csv', 'w', newline='') as csvfile:
        # build CSV writer
        writer = csv.writer(csvfile)

        # write headers
        writer.writerow(["No", "Images", "MIR", "MIG", "MIB",
                         "VHR", "VHG", "VHB", "SER", "SEG", "SEB"])

        for i in range(len(o_images)):
            rel_path = "11-Images/Origi_image/"+o_images[i]
            print(rel_path)
            result = image_process(rel_path)
            ans = [(i+1), o_images[i], "%.2f" % result[0], "%.2f" % result[1], "%.2f" % result[2], "%.2f" % result[3],
                   "%.2f" % result[4], "%.2f" % result[5], "%.6f" % result[6], "%.6f" % result[7], "%.6f" % result[8]]
            # print(ans)

            writer.writerow(ans)

        with open('output11_en.csv', 'w', newline='') as csvfile:
            # build CSV writer
            writer = csv.writer(csvfile)

            # write headers
            writer.writerow(["No", "Images", "MIR", "MIG", "MIB",
                             "VHR", "VHG", "VHB", "SER", "SEG", "SEB"])

            for i in range(len(e_images)):
                rel_path = "11-Images/Encry_image/"+e_images[i]
                print(rel_path)
                result = image_process(rel_path)
                ans = [(i+1), e_images[i], "%.2f" % result[0], "%.2f" % result[1], "%.2f" % result[2], "%.2f" % result[3],
                       "%.2f" % result[4], "%.2f" % result[5], "%.6f" % result[6], "%.6f" % result[7], "%.6f" % result[8]]
                # print(ans)

                writer.writerow(ans)

        with open('output11_de.csv', 'w', newline='') as csvfile:
            # build CSV writer
            writer = csv.writer(csvfile)

            # write headers
            writer.writerow(["No", "Images", "MIR", "MIG", "MIB",
                             "VHR", "VHG", "VHB", "SER", "SEG", "SEB"])

            for i in range(len(d_images)):
                rel_path = "11-Images/Decry_image/"+d_images[i]
                print(rel_path)
                result = image_process(rel_path)
                ans = [(i+1), d_images[i], "%.2f" % result[0], "%.2f" % result[1], "%.2f" % result[2], "%.2f" % result[3],
                       "%.2f" % result[4], "%.2f" % result[5], "%.6f" % result[6], "%.6f" % result[7], "%.6f" % result[8]]
                # print(ans)

                writer.writerow(ans)
