import os.path
import imp
from astrophoto import camerainterface
import persistence

class Session:
    def __init__(self):
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
    def __init__(self, name, camera=None):
        self.name = name
        self.camera = camera
        self.interface = ''
        self.imageTypes = []
        self.spectralchannels = []
        if camera is not None:
            self.initImageTypes()

    def initImageTypes(self):
        for form in self.camera.formats:
            if(form == 'RGB Bayer'):
                newImageType = ImageType()
                bayer_red_if = ImagingFunction()
                bayer_red = SpectralChannel('bayer_red')
                bayer_red_if.spectralchannel = bayer_red
                self.spectralchannels.append(bayer_red)
                newImageType.imagingfunctions.append(bayer_red_if)

                bayer_green_if = ImagingFunction()
                bayer_green_if.spectralchannel = SpectralChannel('bayer_green')
                newImageType.imagingfunctions.append(bayer_green_if)

                bayer_blue_if = ImagingFunction()
                bayer_blue_if.spectralchannel = SpectralChannel('bayer_blue')

                self.imageTypes.append(newImageType)

class ImagingFunction:
    pass

class ImageType:
    def __init__(self):
        self.imagingfunctions = []
        self.isSpectralVariable = 'False'

class Project:
    def __init__(self, name):
        self.name = name
        self.cameraconfiguration = None
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
    self.camerainterface = interface
    camera = createCamera(interface)
    cameraConfiguration = CameraConfiguration(name, camera)

    project.cameraConfiguration = cameraConfiguration
    return cameraConfiguration

def createCamera(interface):
    """used for unittesting.

    This function will be replace with a mock. Get rid of camerainterfacedependency.
    """
    return camerainterface.createCamera(interface)

class SpectralChannel:
    def __init__(self, name=''):
        self.identifier = name

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


class PersistenceFacade:

    def __init__(self):
        self.database = self.getDatabase()
        self.database.initschema()

    def insertproject(self, name):
        self.database.insertproject(name)

    def insertcameraconfiguration(self, cameraconfig, project):
        self.database.insertcameraconfiguration( cameraconfig.name, project.name, cameraconfig.camerainterface )

    def getDatabase(self):
        self.database = persistence.Database()
        return self.database

    def loadcameraconfig(self, tupel):
        interface = tupel[1]
        camera = createCamera(interface)
        cameraconfig = CameraConfiguration(tupel[0], camera)
        return cameraconfig

    def loadproject(self, projectname):
        project = Project(projectname)
        cameraconfigtupel = self.database.getCameraconfigOf(projectname)
        cameraconfig = self.loadcameraconfig(cameraconfigtupel)
        project.cameraconfiguration = cameraconfig
        return project

    def loadprojects(self):
        projects = []
        projecttupels = self.database.getprojects()
        projects = [self.loadproject(projecttupel[0]) for projecttupel in projecttupels]
        return projects
