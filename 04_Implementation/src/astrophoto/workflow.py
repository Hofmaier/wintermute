import os.path
import imp
import camerainterface

class Session:
    def __init__(self, factory=None):
        if factory == None:
            factory = ProjectFactory()
        self.projectFactory = factory
        self.currentProject = None
        self.workspace = Workspace()

    def createProject(self, name):
        project = Project(name)
        self.currentProject = project
        return project

    def createCameraConfiguration(self, name, interface):
        cameraConfiguration = createCameraConfiguration(name, interface, self.currentProject)
        self.workspace.cameraconfigurations.append(cameraConfiguration)
        return cameraConfiguration

    def getInterfaces(self):
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

class Workspace:
    def __init__(self):
        self.cameraconfigurations = []

def createCameraConfiguration(name, interface, project):
    print(project)
    camera = createCamera(interface)
    cameraConfiguration = CameraConfiguration(name, camera)
    return cameraConfiguration

def createCamera(interface):
    """used for unittesting.

    This function will be replace with a mock. Get rid of camerainterfacedependency.
    """
    return camerainterface.createCamera(interface)

