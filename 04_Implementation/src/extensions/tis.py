from astrophoto import camerainterface
from camerainterface import ImageType

class TISCamera(camerainterface.Camera):
    def __init__(self):
        self.name = 'tis interface'
        self.imageTypes = [ImageType.Bayermatrix, ImageType.RGB_Image]
        
    def getInterfaceName(self):
        return getInterfaceName()
    
    def getImageTypes(self):
        self.imageTypes = [camerainterface.ImageType.Bayermatrix]
        return self.imageTypeList

def getInterfaceName():
    return 'The Imaging Source'

def createCameraControl():
    return TISCamera()


