import os.path
import imp
from astrophoto import camerainterface

class Session:
    def __init__(self, factory=None):
        if factory == None:
            factory = ProjectFactory()
        self.projectFactory = factory
        self.currentProject = ""

    def createProject(self, name):
        self.projectFactory.createProject(name)

    def createCameraConfiguration(self, name, interface):
        cameraConfiguration = createCameraConfiguration(name, interface, self.currentProject)
        return cameraConfiguration

class CameraConfiguration:
    def __init__(self, name, camera):
        self.name = name
        self.camera = camera

class ProjectFactory:
    pass

class Project:
    def __init__(self, name):
        self.name = name
        self.cameraConfiguration = None

def createCameraConfiguration(name, interface, project):
    print(project)
    camera = createCamera(interface)
    cameraConfiguration = CameraConfiguration(name, camera)
    project.cameraConfiguration = cameraConfiguration
    return cameraConfiguration

def getInterfaceNames():
    print('getInterfaceNames')
    imModules = getInterfaceImplModules()
    names = []
    for interfaceImpl in imModules:
        name = interfaceImpl.getInterfaceName()
        names.append(name)
    return names

def createCamera(interface):
    return camerainterface.createCamera(interface)
