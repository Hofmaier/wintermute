
from pyraf import iraf
from iraf import noao
from iraf import imred
from iraf import ccdred
from iraf import ccdhedit

class CalibrationFrames:
    def __init__(self):
        self.inputFolder = ""
        self.outputFile = ""
    def createAverageBias(self):
        iraf.zerocombine(input=self.inputFolder,output=self.outputFile)

#    def createAverageFlat(self):
        

# Possible Values for headerType are: zero, dark, flat
    def setFitsHeader(self, headerType):
        iraf.ccdhedit(self.inputFolder, parameter="IMAGETYP", value = headerType)
