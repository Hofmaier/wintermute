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

extensionmodule = [('tis','The Imaging Source'),('mockinterface','CamerainterfaceMock')]

def load():
    for module in extensionmodule:
        modulefilename = module[0]
        displayname = module[1]
        moduletuple = imp.find_module(modulefilename, ['extensions'])
        modulemock = imp.load_module(modulefilename, *moduletuple)
        moduledict[displayname] = modulemock

