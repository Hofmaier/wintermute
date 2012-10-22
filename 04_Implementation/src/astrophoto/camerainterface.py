moduledict = {}

def getModule(interface):
    module = moduledict[interface]
    return module

class Camera:
    pass

class ImageType:
    Bayermatrix = 1
    toStr = {Bayermatrix:'Bayer-Matrix'}

def createCamera(interface):
    interfacemodule = getModule(interface)
    camera = interfacemodule.createCameraControl()
    return camera


def getInterfaceImplFiles():
    extensionlist = []
    for root, dirs, files in os.walk('/home/lukas/wintermute/04_Implementation/src/extensions/'):
        for file in files:
            if file.endswith('.py'):
                extensionlist.append(file)

    return extensionlist

def getExtensionModule(file):
    print('getExtionsionModules')
    filestr = str(file)
    path = '/home/lukas/wintermute/04_Implementation/src/extensions/' + filestr
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
        moduleDict[concreteModuleName] = module
    return interfaceModules

def getInterfaceNames():
    print('getInterfaceNames')
    imModules = getInterfaceImplModules()
    names = moduleDict.keys()
    return names


