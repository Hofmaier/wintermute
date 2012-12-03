import os
import imp

moduledict = {}

def getModule(interface):
    module = moduledict[interface]
    return module

class Camera:
    def getFormats(self):
        self.imageTypes = []
        return self.imageTypes

    def getImageTypesAsStr(self):
        names = [ImageType.toStr[imagetype] for imagetype in self.imageTypes]
        return names

    def capture(self, gain, shutter):
        pass

class ImageType:
    Bayermatrix = 1
    RGB_Image = 2
    toStr = {Bayermatrix:'Bayer-Matrix', RGB_Image:'RGB-Image'}
    
def createCamera(interface):
    interfacemodule = getModule(interface)
    camera = interfacemodule.createCameraControl()
    print('createCamera ' + interface)
    return camera

def getInterfaceNames():
    print('getInterfaceNames')
  #  imModules = getInterfaceImplModules()
    names = moduledict.keys()
    return names

def load():
    moduletuple = imp.find_module('mockinginterface', ['extensions'])
    modulemock = imp.load_module('mockinginterface', *moduletuple)
    moduledict['CamerainterfaceMock'] = modulemock
    moduletuple = imp.find_module('tis', ['extensions'])
    modulemock = imp.load_module('tis', *moduletuple)
    moduledict['The Imaging Source'] = modulemock
    
