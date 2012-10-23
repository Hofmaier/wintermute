from astrophoto import camerainterface

class Camerainterfacemock(camerainterface.Camera):
    def __init__(self):
        self.name = 'interfacemock'

    def getInterfaceName(self):
        return getInterfaceName()

    def getImageTypes(self):
        self.imageTypeList = [camerainterface.ImageType.Bayermatrix]
        return self.imageTypeList
    
def getInterfaceName():
    return 'Interface Mock'

def createCameraControl():
    return Camerainterfacemock()
