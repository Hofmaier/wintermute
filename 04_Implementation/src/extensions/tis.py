import astrophoto
from astrophoto import camerainterface
import unicap

class TISCamera(camerainterface.Camera):
    def __init__(self):
        self.name = 'tis interface'
        self.formats = ['RGB Bayer']
        self.imageTypes = [camerainterface.ImageType.Bayermatrix, camerainterface.ImageType.RGB_Image]

    def getInterfaceName(self):
        return getInterfaceName()

    def getImageTypes(self):
        self.imageTypes = [camerainterface.ImageType.Bayermatrix]
        return self.imageTypes

    def capture(self, duration, imagetype):
        return unicap.capture()

def getInterfaceName():
    return 'The Imaging Source'

def createCameraControl():
    return TISCamera()
