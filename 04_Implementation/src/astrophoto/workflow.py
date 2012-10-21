import os.path
import imp

class Session:
    def __init__(self, factory=None):
        if factory == None:
            factory = ProjectFactory()
        self.projectFactory = factory

    def createProject(self, name):
        self.projectFactory.createProject(name)

    def createCameraConfiguration(self, name, interface):
        pass

class CameraConfiguration:
    def __init__(self, name):
        self.name = name

class ProjectFactory:
    pass

class Project:
    def __init__(self, name):
        self.name = name

def createCameraConfiguration(name, interface, project):
    cameraConfiguration = CameraConfiguration(name)

def getInterfaceNames():
    print('getInterfaceNames')
    imModules = getInterfaceImplModules()
    names = []
    for interfaceImpl in imModules:
        name = interfaceImpl.getInterfaceName()
        names.append(name)
    return names

