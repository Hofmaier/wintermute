import os.path
import imp
from astrophoto import camerainterface
from astrophoto import persistence

class Session:
    def __init__(self):
        self.currentProject = None
        self.workspace = Workspace()

    def createProject(self, name):
        project = Project(name)
        self.workspace.projectList.append(project)
        self.currentProject = project
        print("project created")
        return project

    def createCameraConfiguration(self, name, interface):
        cameraConfiguration = createCameraConfiguration(name, interface, self.currentProject)
        print("haaaaaalo" + interface)
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
        print("adding Adapter: " + name)
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
        self.imagetypes = []
        self.imagingfunctions = {}
        if camera is not None:
            self.initImageTypes()

    def initImageTypes(self):
        for form in self.camera.formats:
            if(form == 'RGB Bayer'):
                rawbayer = 'RAW Bayer'
                imagetypegroup = []

                bayer_red_if = ImagingFunction()
                bayer_red_if.spectralchannel =  SpectralChannel('bayer_red')
                imagetypegroup.append(bayer_red_if)

                bayer_green_if = ImagingFunction()
                bayer_green_if.spectralchannel = SpectralChannel('bayer_green')
                imagetypegroup.append(bayer_green_if)

                bayer_blue_if = ImagingFunction()
                bayer_blue_if.spectralchannel = SpectralChannel('bayer_blue')
                imagetypegroup.append(bayer_blue_if)

                self.imagetypes.append(rawbayer)

                self.imagingfunctions[rawbayer]=imagetypegroup

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
        self.adapterList = []
        self.telescopeList = []
        self.opticalSystemList = []
        self.persFacade = PersistenceFacade()
        self.cameraconfigurations = []
        self.projectList = []

    def load(self):
        camerainterface.getInterfaceNames()
        self.projectList = self.persFacade.loadprojects()
        self.cameraconfigurations = self.persFacade.cameraconfigurations

def createCameraConfiguration(name, interface, project):
    camerainterface = interface
    camera = createCamera(interface)
    cameraConfiguration = CameraConfiguration(name, camera)
    cameraConfiguration.interface = interface
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
            self.shotList.append(shot)

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
        self.cameraconfigurations = []

    def insertproject(self, project):
        rowId = self.persistOpticalSystem(project.opticalSystem.adapter, project.opticalSystem.telescope)
        self.database.insertproject(project.name, rowId)

    def persistcameraconfiguration(self, cameraconfig, project):
        self.database.persistcameraconfiguration( cameraconfig.name, project.name, cameraconfig.interface )

    def persistOpticalSystem(self, adapter, telescope):
        return self.database.insertopticalsystem(adapter.name, telescope.name)

    def persistAdapter(self, adapter):
        self.database.insertAdapter(adapter.name)

    def persistTelescope(self, telescope):
        self.database.insertTelescope(telescope.name)

    def persistOpticalSystem(self, adapter, telescope):
        self.database.insertOpticalSystem(adapter.name, telescope.name)

    def getDatabase(self):
        self.database = persistence.Database()
        return self.database

    def loadcameraconfig(self, tupel):
        interface = tupel[1]
        camera = createCamera(interface)
        cameraconfig = CameraConfiguration(tupel[0], camera)
        cameraconfig.interface = interface
        self.cameraconfigurations.append(cameraconfig)
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
