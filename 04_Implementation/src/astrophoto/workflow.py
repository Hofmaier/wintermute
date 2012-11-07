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

    def createProject(self, name):
        project = Project(name)
        self.workspace.projectList.append(project)
        self.currentProject = project
        return project

    def createCameraConfiguration(self, name, interface):
        cameraConfiguration = createCameraConfiguration(name, interface, self.currentProject)
        self.workspace.cameraconfigurations.append(cameraConfiguration)
        return cameraConfiguration

    def getInterfaceNames(self):
        return camerainterface.getInterfaceNames()

    def createOpticalSystem(self, name, adapter, telescope):
        opticalSystem = Opticalsystem(name, adapter, telescope)
        self.workspace.opticalSystemList.append(opticalSystem)
        return opticalSystem

    def createAdapter(self, name):
        adapter = Adapter(name)
        self.workspace.adapterList.append(adapter)
        return adapter

    def createTelescope(self, name):
        telescope = Telescope(name)
        self.workspace.telescopeList.append(telescope)
        return telescope

    def createShotDescription(self):
        shotDescription = Shotdescription()
        self.currentProject.shotDescriptionList.append(shotDescription)
        return shotDescription

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
        self.shotDescriptionList = []
        self.opticalSystem = None

class Workspace:
    def __init__(self):
        self.cameraconfigurations = []
        self.adapterList = []
        self.telescopeList = []
        self.opticalSystemList = []
        self.projectList = []

def createCameraConfiguration(name, interface, project):
    camera = createCamera(interface)
    cameraConfiguration = CameraConfiguration(name, camera)
    spectralchannel = SpectralChannel()
    spectralchannel.name = 'rgb'
    cameraConfiguration.spectralchannels.append(spectralchannel)
    project.cameraConfiguration = cameraConfiguration
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
    def __init__(self):
        pass
    def setProperties(self, nrOfShots, duration, imageTyp):
        self.duration = duration
        self.imageTyp = imageTyp
        self.shotList = []
        i = 0
        for i in range(nrOfShots):
            shot = Shot()
            shotDescription.shotList.append(shot)

class Shot:
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

