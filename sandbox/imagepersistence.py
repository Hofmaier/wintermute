import numpy
import pyfits

def writefits(image, filename):
    """save image in fitsformat.

    image is a list of 640 x 480  integers. it contains intensity values of an image.
    """
    n = numpy.array(image)
    matrix = n.reshape(480, 640)
    int32matrix = numpy.int8(matrix)
    hdu = pyfits.PrimaryHDU(int32matrix)
    hdu.writeto(filename)
