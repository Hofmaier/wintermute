import os.path
import imp
from astrophoto import camerainterface

class Session:
    def __init__(self, factory=None):
        if factory == None:
            factory = ProjectFactory()
        self.projectFactory = factory
        self.currentProject = None

    def createProject(self, name):
        project = Project(name)
        self.currentProject = project
        return project

    def createCameraConfiguration(self, name, interface):
        cameraConfiguration = createCameraConfiguration(name, interface, self.currentProject)
        return cameraConfiguration

    def getInterfaces():
        return camerainterface.getInterfaceNames()

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

def createCamera(interface):
    """used for unittesting.

    This function will be replace with a mock. Get rid of camerainterfacedependency.
    """
    return camerainterface.createCamera(interface)
