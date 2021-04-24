import struct


def bina2deci(bina):
    sgn_len, exp_len, mant_len = 1, 8, 23

    sign = (bina & (2 ** sgn_len - 1) * (2 ** (exp_len + mant_len))
            ) >> (exp_len + mant_len)
    exponent_raw = (bina & ((2 ** exp_len - 1) * (2 ** mant_len))) >> mant_len
    mantissa = bina & (2 ** mant_len - 1)

    sign_mult = 1
    if sign == 1:
        sign_mult = -1

    if exponent_raw == 2 ** exp_len - 1:  # Could be Inf or NaN
        if mantissa == 2 ** mant_len - 1:
            return float('nan')  # NaN

        return sign_mult * float('inf')  # Inf

    exponent = exponent_raw - (2 ** (exp_len - 1) - 1)

    if exponent_raw == 0:
        mant_mult = 0  # Gradual Underflow
    else:
        mant_mult = 1

    for b in range(mant_len - 1, -1, -1):
        if mantissa & (2 ** b):
            mant_mult += 1 / (2 ** (mant_len - b))

    return "{:.4f}".format(sign_mult * (2 ** exponent) * mant_mult)


if __name__ == '__main__':
    with open("sideinfobina.txt", "r") as fin:  # read file
        binas = fin.readlines()

    with open("sideinfodeci.txt", "w") as fout:  # write file
        for bina in binas:
            d = bina2deci(int(bina, 2))  # convert binary to decimal
            print(d)
            fout.write(d+"\n")
