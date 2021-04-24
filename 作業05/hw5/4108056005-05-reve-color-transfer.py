# USAGE
# python 4108056005-05-reve-color-transfer.py --result ult1.png --rsource yrcsou.png

# import the necessary packages
import numpy as np
import argparse
import cv2


def color_transfer(result, clip=True, preserve_paper=True):
    """
    Transfers the color distribution from the result to the target
    image using the mean and standard deviations of the L*a*b*
    color space.

    This implementation is (loosely) based on to the "Color Transfer
    between Images" paper by Reinhard et al., 2001.

    Parameters:
    -------
    result: NumPy array
            OpenCV image in BGR color space (the result image)
    target: NumPy array
            OpenCV image in BGR color space (the target image)
    clip: Should components of L*a*b* image be scaled by np.clip before 
            converting back to BGR color space?
            If False then components will be min-max scaled appropriately.
            Clipping will keep target image brightness truer to the input.
            Scaling will adjust image brightness to avoid washed out portions
            in the resulting color transfer that can be caused by clipping.
    preserve_paper: Should color transfer strictly follow methodology
            layed out in original paper? The method does not always produce
            aesthetically pleasing results.
            If False then L*a*b* components will scaled using the reciprocal of
            the scaling factor proposed in the paper.  This method seems to produce
            more consistently aesthetically pleasing results 

    Returns:
    -------
    transfer: NumPy array
            OpenCV image (w, h, 3) NumPy array (uint8)
    """
    # convert the images from the RGB to L*ab* color space, being
    # sure to utilizing the floating point data type (note: OpenCV
    # expects floats to be 32-bit, so use that instead of 64-bit)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2LAB).astype("float32")

    # read sideinfodeci.txt
    with open("sideinfodeci.txt", "r") as file:
        infos = file.readlines()

    lMeanSrc = float(infos[0])
    aMeanSrc = float(infos[1])
    bMeanSrc = float(infos[2])
    lStdSrc = float(infos[3])
    aStdSrc = float(infos[4])
    bStdSrc = float(infos[5])
    lMeanTar = float(infos[6])
    aMeanTar = float(infos[7])
    bMeanTar = float(infos[8])
    lStdTar = float(infos[9])
    aStdTar = float(infos[10])
    bStdTar = float(infos[11])

    # subtract the means from the target image
    (l, a, b) = cv2.split(result)
    l -= lMeanTar
    a -= aMeanTar
    b -= bMeanTar

    if preserve_paper:
        # scale by the standard deviations using paper proposed factor
        l = (lStdSrc / lStdTar) * l
        a = (aStdSrc / aStdTar) * a
        b = (bStdSrc / bStdTar) * b
    else:
        # scale by the standard deviations using reciprocal of paper proposed factor
        l = (lStdSrc / lStdTar) * l
        a = (aStdSrc / aStdTar) * a
        b = (bStdSrc / bStdTar) * b

    # add in the result mean
    l += lMeanSrc
    a += aMeanSrc
    b += bMeanSrc

    # clip/scale the pixel intensities to [0, 255] if they fall
    # outside this range
    l = _scale_array(l, clip=clip)
    a = _scale_array(a, clip=clip)
    b = _scale_array(b, clip=clip)

    # merge the channels together and convert back to the RGB color
    # space, being sure to utilize the 8-bit unsigned integer data
    # type
    rsource = cv2.merge([l, a, b])
    rsource = cv2.cvtColor(rsource.astype("uint8"), cv2.COLOR_LAB2BGR)

    # return the color transferred image
    return rsource


def image_stats(image):
    """
    Parameters:
    -------
    image: NumPy array
            OpenCV image in L*a*b* color space

    Returns:
    -------
    Tuple of mean and standard deviations for the L*, a*, and b*
    channels, respectively
    """
    # compute the mean and standard deviation of each channel
    (l, a, b) = cv2.split(image)
    (lMean, lStd) = (l.mean(), l.std())
    (aMean, aStd) = (a.mean(), a.std())
    (bMean, bStd) = (b.mean(), b.std())

    # return the color statistics
    return (lMean, lStd, aMean, aStd, bMean, bStd)


def _min_max_scale(arr, new_range=(0, 255)):
    """
    Perform min-max scaling to a NumPy array

    Parameters:
    -------
    arr: NumPy array to be scaled to [new_min, new_max] range
    new_range: tuple of form (min, max) specifying range of
            transformed array

    Returns:
    -------
    NumPy array that has been scaled to be in
    [new_range[0], new_range[1]] range
    """
    # get array's current min and max
    mn = arr.min()
    mx = arr.max()

    # check if scaling needs to be done to be in new_range
    if mn < new_range[0] or mx > new_range[1]:
        # perform min-max scaling
        scaled = (new_range[1] - new_range[0]) * \
            (arr - mn) / (mx - mn) + new_range[0]
    else:
        # return array if already in range
        scaled = arr

    return scaled


def _scale_array(arr, clip=True):
    """
    Trim NumPy array values to be in [0, 255] range with option of
    clipping or scaling.

    Parameters:
    -------
    arr: array to be trimmed to [0, 255] range
    clip: should array be scaled by np.clip? if False then input
            array will be min-max scaled to range
            [max([arr.min(), 0]), min([arr.max(), 255])]

    Returns:
    -------
    NumPy array that has been scaled to be in [0, 255] range
    """
    if clip:
        scaled = np.clip(arr, 0, 255)
    else:
        scale_range = (max([arr.min(), 0]), min([arr.max(), 255]))
        scaled = _min_max_scale(arr, new_range=scale_range)

    return scaled


def show_image(title, image, width=300):
    # resize the image to have a constant width, just to
    # make displaying the images take up less screen real
    # estate
    r = width / float(image.shape[1])
    dim = (width, int(image.shape[0] * r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    # show the resized image
    cv2.imshow(title, resized)


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


# main
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--result", required=True,
                help="Path to the result image")
ap.add_argument("-c", "--clip", type=str2bool, default='t',
                help="Should np.clip scale L*a*b* values before final conversion to BGR? "
                "Approptiate min-max scaling used if False.")
ap.add_argument("-p", "--preservePaper", type=str2bool, default='t',
                help="Should color transfer strictly follow methodology layed out in original paper?")
ap.add_argument("-rs", "--rsource",
                help="Path to the reverse source image (optional)")
args = vars(ap.parse_args())

# load the images
result = cv2.imread(args["result"])

# transfer the color distribution from the source image
# to the target image
rsource = color_transfer(
    result, clip=args["clip"], preserve_paper=args["preservePaper"])

# check to see if the output image should be saved
if args["rsource"] is not None:
    cv2.imwrite(args["rsource"], rsource)

# show the images and wait for a key press
show_image("Result", result)
show_image("Reverse Sourse", rsource)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("---END of this program---")
