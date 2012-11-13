from pyraf import iraf
from iraf import noao
from iraf import imred
from iraf import ccdred


def createAverageBias(biasImagesList):
    biasString = getIrafString(biasImagesList)
    iraf.zerocombine(input=biasString,output="averagedBias",process="No",reject="none")

def createAverageDark(darkImagesList):
    darkString = getIrafString(darkImagesList)
    iraf.darkcombine(input=darkString,process="No",output="averagedDark")

def createAverageFlat(flatImagesList):
    flatString = getIrafString(flatImagesList)
    iraf.darkcombine(input=flatString,process="No",output="averagedFlat")

#Possible values for imageType=zero, dark, flat
def changeHeaderFormat(imageList, imageType):
    imageString = getIrafString(imageList)
    iraf.ccdhedit(imageString, parameter="IMAGETYP",value=imageType)

def calibrateImages(imageList, masterBias, masterDark, masterFlat, outputFile):
    calibrateString = getIrafString(imageList)
    iraf.ccdproc(images=calibrateString, zerocor="yes", darkcor="yes",flatcor="yes",zero=masterBias,dark=masterDark,flat=masterFlat,output=outputFile,fixpix="No",ccdtype="none",overscan="no")

def stackImages(imageList, outputFile):
    stackString = getIrafString(imageList)
    imcombine(input=stackString,output=outputFile)

def getIrafString(imageList):
    imageString = imageList.pop()
    for image in imageList:
        imageString = imageString + "," + image
    return imageString

def proccessImages(inputImageList, outputImageList, biasImageList, darkImageList, flatImageList):
    outputString = getIrafString(outputImageList)
    masterBias = createAverageBias(biasImageList)
    masterDark = createAverageDark(darkImageList)
    masterFlat = createAverageFlat(flatImageList)
    calibrateImageList(inputImageList, masterBias, masterDark, masterFlat, outputString)




