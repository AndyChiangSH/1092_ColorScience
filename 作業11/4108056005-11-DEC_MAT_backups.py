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

        # b_sum = 0
        # g_sum = 0
        # r_sum = 0

        # for i in range(H):
        #     for j in range(V):
        #         b_sum += img[i, j, 0]
        #         g_sum += img[i, j, 1]
        #         r_sum += img[i, j, 2]

        # b_mean = b_sum/float(H*V)
        # g_mean = g_sum/float(H*V)
        # r_mean = r_sum/float(H*V)

        # print("b_mean = ", b_mean)
        # print("g_mean = ", g_mean)
        # print("r_mean = ", r_mean)

        # Part1: Mean of Image
        mi = img.mean(axis=0).mean(axis=0)
        # print(mi)
        # print(mi[0])

        # for i, col in enumerate(['b', 'g', 'r']):
        #     hist = cv2.calcHist([img], [], None, [256], [0, 256])
        #     plt.plot(hist[i], color=col)
        #     plt.xlim([0, 256])

        # plt.show()

        # Part2: Variance of Histogram
        vh = list()
        for chn in range(3):
            h_sum = 0
            hist = cv2.calcHist([img], [chn], None, [256], [0, 256])
            for i in range(256):
                for j in range(256):
                    h_sum += pow(hist[i]-hist[j], 2)

            vh.append((h_sum/(2*H*V))[0])

        # print(vh)

        # Part3: Shannon Entropy
        se = list()
        for chn in range(3):
            s_sum = 0.0
            hist = cv2.calcHist([img], [chn], None, [256], [0, 256])
            for i in range(256):
                pz = hist[i]/float(H*V)
                if hist[i] != 0:
                    s_sum += pz*(math.log(pz, 2))

            se.append(-(s_sum))

        # print(se[0][0])

        # 0:Blue 1:Green 2:Red
        return [mi[2], mi[1], mi[0], vh[2], vh[1], vh[0], se[2][0], se[1][0], se[0][0]]


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

    # rel_path = "11-Images/Decry_image/"+d_images[0]
    # print(rel_path)
    # image_process(rel_path)

    with open('output09.csv', 'w', newline='') as csvfile:
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

        with open('output09_en.csv', 'w', newline='') as csvfile:
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

        with open('output09_de.csv', 'w', newline='') as csvfile:
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
