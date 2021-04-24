import struct


def deci2bina(deci):

    sgn_len, exp_len, mant_len = 1, 8, 23

    if deci >= 2 ** (sgn_len + exp_len + mant_len):
        raise ValueError(
            "Number deci is longer than prescribed parameters allows")

    return "0"+"{:031b}".format(deci)   # return string of binary


if __name__ == '__main__':
    with open("sideinfodeci.txt", "r") as fin:  # read file
        decis = fin.readlines()

    with open("sideinfobina.txt", "w") as fout: # write file
        for deci in decis:
            m = struct.unpack('I', struct.pack('f', float(deci)))[0]    # convert floar into unsigned integer
            b = deci2bina(m)
            print(b)
            fout.write(b+"\n")
