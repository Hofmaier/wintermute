
from pyraf import iraf
from iraf import images
from iraf import noao
from iraf import imred
from iraf import ccdred
from iraf import ccdhedit

class CalibrationFrames:
    def __init__(self):
        self.inputFolder = ""
        self.outputFile = ""
        self.avaragedDark = ""
        self.avaragedBias = ""
        self.avaragedFlat = ""
    def createAverageBias(self):
        iraf.zerocombine(input=self.inputFolder,output=self.avaragedBias)

    def createAverageDark(self):
        iraf.darkcombine(input=self.inputFolder,process="No",output=self.avaragedDark)

    def createAverageFlat(self):
                iraf.flatcombine(input=self.inputFolder,process="No",output=self.avaragedFlat)

# Possible Values for headerType are: zero, dark, flat
    def setFitsHeader(self, headerType):
        iraf.ccdhedit(self.inputFolder, parameter="IMAGETYP", value = headerType)

    def processImagesWithCalibration(self):
        iraf.ccdproc(images="NGC1.fit",zerocor="yes",darkcor="yes",flatcor="yes",zero="masterbias.fit",flat="masterflat.fit",dark="masterdark.fit",output="lala.fit",fixpix="No",ccdtype="none")

    def stackImages(self):
        imcombine(input=self.inputFolder,output=self.outputFile)

