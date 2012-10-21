import camerainterface

class CameraInterfaceMock(camerainterface.Camera):
    def __init__(self):
        self.name = 'interfacemock'

def getInterfaceName():
    return 'The Imaging Source'

def createCameraControl():
    return CameraInterfaceMock()
