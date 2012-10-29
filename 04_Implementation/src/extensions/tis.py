import astrophoto
from astrophoto import camerainterface

class TISCamera(camerainterface.Camera):
    def __init__(self):
        self.name = 'tis interface'
        self.imageTypes = [camerainterface.ImageType.Bayermatrix, camerainterface.ImageType.RGB_Image]
        
    def getInterfaceName(self):
        return getInterfaceName()
    
    def getImageTypes(self):
        self.imageTypes = [camerainterface.ImageType.Bayermatrix]
        return self.imageTypeList

def getInterfaceName():
    return 'The Imaging Source'

def createCameraControl():
    return TISCamera()


