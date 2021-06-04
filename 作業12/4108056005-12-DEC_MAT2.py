# Color science hw12 - Encryption Metrics-2
import os
import cv2
import matplotlib.pyplot as plt
import math
import csv


def diff(ori, enc):
    if ori == enc:
        return 0
    else:
        return 1


def image_process(ori_path, enc_path):

    ori_img = cv2.imread(ori_path)
    enc_img = cv2.imread(enc_path)

    if ori_img is None or enc_img is None:
        print("Can't read this image...")
    else:
        # image shape: (H, V, rgb)
        H, V, channels = ori_img.shape

        # Part 1: find NPCR
        npcr = list()
        for c in range(channels):
            cnt = 0
            for i in range(H):
                for j in range(V):
                    cnt += diff(ori_img[i, j, c], enc_img[i, j, c])

            npcr.append(cnt*100/float(H*V))

        # Part 2: find UACI
        uaci = list()
        for c in range(channels):
            cnt = 0
            for i in range(H):
                for j in range(V):
                    cnt += abs(int(ori_img[i, j, c])-int(enc_img[i, j, c]))

            uaci.append(cnt*100/float(H*V*255))

        # 0:Blue 1:Green 2:Red
        return npcr[2], npcr[1], npcr[0], uaci[2], uaci[1], uaci[0]


if __name__ == "__main__":

    # relative pathname of Origi_images
    dir_path = r"12-Images/Origi_image/"
    o_images = next(os.walk(dir_path))[2]
    # print(o_images)

    # relative pathname of Encry_images
    dir_path = r"12-Images/Encry_image/"
    e_images = next(os.walk(dir_path))[2]
    # print(e_images)

    with open('output12.csv', 'w', newline='') as csvfile:
        # build CSV writer
        writer = csv.writer(csvfile)

        # write headers
        writer.writerow(["No", "ORI Image", "ENC Image", "NPCR(R)",
                         "NPCR(G)", "NPCR(B)", "UACI(R)", "UACI(G)", "UACI(B)"])

        # read each image
        for i in range(len(o_images)):
            ori_path = "12-Images/Origi_image/"+o_images[i]
            print(ori_path)
            enc_path = "12-Images/Encry_image/"+e_images[i]
            print(enc_path)
            # the fuction return a tuple of NPCP and UACI
            result = image_process(ori_path, enc_path)
            ans = [(i+1), o_images[i], e_images[i], "%.4f" % result[0], "%.4f" % result[1],
                   "%.4f" % result[2], "%.4f" % result[3], "%.4f" % result[4], "%.4f" % result[5]]
            print(ans)

            # write a row in list data type
            writer.writerow(ans)
