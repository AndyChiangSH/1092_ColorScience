# Color science hw11 - Encryption Metrics-1
import os
import cv2
import math
import csv
import numpy as np


def get_ctap(img, mode):
    # print(img)

    H, V = img.shape

    # print(f"H = {H}")
    # print(f"V = {V}")

    if mode == "HD":
        x_img = img[0:V, 0:H-1].flatten()
        y_img = img[0:V, 1:H].flatten()
    elif mode == "VD":
        x_img = img[0:V-1, 0:H].flatten()
        y_img = img[1:V, 0:H].flatten()
    else:
        x_img = img[0:V-1, 0:H-1].flatten()
        y_img = img[1:V, 1:H].flatten()

    # print(x_img)
    # print(y_img)

    x_mean = np.mean(x_img)
    y_mean = np.mean(y_img)

    # print(f"x_mean = {x_mean}")
    # print(f"y_mean = {y_mean}")

    x_var = np.var(x_img)
    y_var = np.var(y_img)

    # print(f"x_var = {x_var}")
    # print(f"y_var = {y_var}")

    cov = np.cov(x_img, y_img)[0][1]

    # print(f"cov = {cov}")

    corre = cov/float(math.sqrt(x_var*y_var))

    # print(f"corre = {corre}")

    return x_mean, y_mean, x_var, y_var, cov, corre


def image_process(img_path):

    img = cv2.imread(img_path)

    if img is None:
        print("Can't read this image...")
    else:
        HD_R = get_ctap(img[:, :, 2], "HD")
        HD_G = get_ctap(img[:, :, 1], "HD")
        HD_B = get_ctap(img[:, :, 0], "HD")
        VD_R = get_ctap(img[:, :, 2], "VD")
        VD_G = get_ctap(img[:, :, 1], "VD")
        VD_B = get_ctap(img[:, :, 0], "VD")
        DD_R = get_ctap(img[:, :, 2], "DD")
        DD_G = get_ctap(img[:, :, 1], "DD")
        DD_B = get_ctap(img[:, :, 0], "DD")

        # 0:Blue 1:Green 2:Red
        return HD_R, HD_G, HD_B, VD_R, VD_G, VD_B, DD_R, DD_G, DD_B


if __name__ == "__main__":

    # ans = image_process("13-Images/Origi_image/01_Airplane.bmp")
    # for a in ans:
    #     for b in a:
    #         print("%.2f" % b, end=", ")
    #     print()

    # relative pathname of Origi_images
    dir_path = r"13-Images/Origi_image/"
    o_images = next(os.walk(dir_path))[2]
    # print(o_images)

    # relative pathname of Encry_images
    dir_path = r"13-Images/Encry_image/"
    e_images = next(os.walk(dir_path))[2]
    # print(e_images)

    with open('output13.csv', 'w', newline='') as csvfile:
        # build CSV writer
        writer = csv.writer(csvfile)

        # write headers
        writer.writerow(["Image Name", "Mode", "Channel", "MEAN(X)", "MEAN(Y)",
                         "VAR(X)", "VAR(Y)", "COV(X,Y)", "Correlation(X,Y)"])

        for i in range(len(o_images)):
            rel_path = "13-Images/Origi_image/"+o_images[i]
            print(rel_path)
            result = image_process(rel_path)
            for j, r in enumerate(result):
                if j % 3 == 0:
                    channel = "R"
                elif j % 3 == 1:
                    channel = "G"
                else:
                    channel = "B"

                if j >= 6:
                    mode = "DD"
                elif j >= 3:
                    mode = "VD"
                else:
                    mode = "HD"

                ans = [o_images[i], mode, (channel+" Channel"), "%.2f" % r[0], "%.2f" % r[1], "%.2f" % r[2],
                       "%.2f" % r[3], "%.2f" % r[4], "%.6f" % r[5]]
                # print(ans)
                writer.writerow(ans)

            rel_path = "13-Images/Encry_image/"+e_images[i]
            print(rel_path)
            result = image_process(rel_path)
            for j, r in enumerate(result):
                if j % 3 == 0:
                    channel = "R"
                elif j % 3 == 1:
                    channel = "G"
                else:
                    channel = "B"

                if j >= 6:
                    mode = "DD"
                elif j >= 3:
                    mode = "VD"
                else:
                    mode = "HD"

                ans = [e_images[i], mode, (channel+" Channel"), "%.2f" % r[0], "%.2f" % r[1], "%.2f" % r[2],
                       "%.2f" % r[3], "%.2f" % r[4], "%.6f" % r[5]]
                # print(ans)
                writer.writerow(ans)
