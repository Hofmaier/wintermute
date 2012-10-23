import camerainterface

class TISCamera(camerainterface.Camera):
    def __init__(self):
        self.name = 'tis interface'
        
    def getInterfaceName(self):
        return getInterfaceName()
    
    def getImageTypes(self):
        self.imageTypeList = [camerainterface.ImageType.Bayermatrix]
        return self.imageTypeList

def getInterfaceName():
    return 'The Imaging Source'

def createCameraControl():
    return TISCamera()


