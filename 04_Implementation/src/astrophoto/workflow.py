import os.path
import imp



class Session:
    def __init__(self, factory=None):
        if factory == None:
            factory = ProjectFactory()
        self.projectFactory = factory

    def createProject(self, name):
        self.projectFactory.createProject(name)

    def createCameraConfiguration(name, interface):
        cameraConfiguration = new CameraConfiguration()

class CameraConfiguration:
    pass

class ProjectFactory:
    pass

class Project:
    pass


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
       
    return interfaceModules

def getInterfaceNames():
    print('getInterfaceNames')
    imModules = getInterfaceImplModules()
    names = []
    for interfaceImpl in imModules:
        name = interfaceImpl.getInterfaceName()
        names.append(name)
    return names

