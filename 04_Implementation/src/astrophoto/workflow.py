import os.path
import imp
from astrophoto import camerainterface

class Session:
    def __init__(self, factory=None):
        if factory == None:
            factory = ProjectFactory()
        self.projectFactory = factory
        self.currentProject = None
        self.workspace = Workspace()
        self.adapterList = []
        self.telescopeList = []

    def createProject(self, name):
        project = Project(name)
        self.currentProject = project
        return project

    def createCameraConfiguration(self, name, interface):
        cameraConfiguration = createCameraConfiguration(name, interface, self.currentProject)
        self.workspace.cameraconfigurations.append(cameraConfiguration)
        return cameraConfiguration

    def getInterfaceNames(self):
        return camerainterface.getInterfaceNames()

    def createOpticalSystem(self, name, adapter, telescope):
        self.opticalSystem = Opticalsystem(name, adapter, telescope)

    def createAdapter(self, name):
        adapter = Adapter(name)
        self.adapterList.append(adapter)
        return adapter

    def createTelescope(self, name):
        telescope = Telescope(name)
        self.telescopeList.append(telescope)
        return telescope

class CameraConfiguration:
    def __init__(self, name, camera):
        self.name = name
        self.camera = camera
        self.spectralchannels = []

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
    camera = createCamera(interface)
    cameraConfiguration = CameraConfiguration(name, camera)
    spectralchannel = SpectralChannel()
    spectralchannel.name = 'rgb'
    cameraConfiguration.spectralchannels.append(spectralchannel)
    return cameraConfiguration

def createCamera(interface):
    """used for unittesting.

    This function will be replace with a mock. Get rid of camerainterfacedependency.
    """
    return camerainterface.createCamera(interface)

class SpectralChannel:
    def __init__(self):
        self.name = ''

class Shotdescription:
    pass

class Telescope:
    def __init__(self, name):
        self.name = name

class Adapter:
    def __init__(self, name):
        self.name = name

class Opticalsystem:
    def __init__(self, name, adapter, telescope):
        self.name = name
        self.adapter = adapter
        self.telescope = telescope

