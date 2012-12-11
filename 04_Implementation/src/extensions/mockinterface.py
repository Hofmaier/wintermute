import astrophoto
from astrophoto import camerainterface

class Camerainterfacemock(camerainterface.Camera):
    def __init__(self):
        self.name = 'interfacemock'
        self.formats = 'RGB Bayer'

    def getInterfaceName(self):
        return getInterfaceName()

    def getFormats(self):
        self.imageTypeList = ['RGB Bayer']
        return self.imageTypeList
    
def getInterfaceName():
    return 'Interface Mock'

def createCameraControl():
    return Camerainterfacemock()
