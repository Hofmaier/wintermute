import os
import imp

moduledict = {}

def getModule(interface):
    module = moduledict[interface]
    return module

class Camera:
    def getImageTypes(self):
        imageTypes = []
        return imageTypes

class ImageType:
    Bayermatrix = 1
    RGB_Image = 2
    toStr = {Bayermatrix:'Bayer-Matrix', RGB_Image:'RGB-Image'}

def createCamera(interface):
    interfacemodule = getModule(interface)
    camera = interfacemodule.createCameraControl()
    return camera

def getInterfaceImplFiles():
    extensionlist = []
    for root, dirs, files in os.walk('extensions/'):
        for file in files:
            if file.endswith('.py'):
                extensionlist.append(file)

    return extensionlist

def getExtensionModule(file):
    print('getExtionsionModules')
    filestr = str(file)
    path = 'extensions/' + filestr
    fin = open(path, 'rb')
    module = imp.load_source(filestr, path, fin)
    return module

def getInterfaceImplModules():
    sourcefiles = getInterfaceImplFiles()
    interfaceModules = []
    for sourcefile in sourcefiles:
        module = getExtensionModule(sourcefile)
        interfaceModules.append(module)
        concreteModuleName = module.getInterfaceName()
        moduledict[concreteModuleName] = module
    return interfaceModules

def getInterfaceNames():
    print('getInterfaceNames')
    imModules = getInterfaceImplModules()
    names = moduledict.keys()
    return names

