import os.path
import imp
import uuid
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


    def createShotDescription(self, nrOfShots, duration, project, imagetype):
        shotDescription = createShotdescription(nrOfShots, duration, project, imagetype)
        return shotDescription

class CameraConfiguration:
    def __init__(self, name, camera=None):
        self.name = name
        self.camera = camera
        self.interface = ''
        self.imagingfunctions = {}
        self.hasFilterWheel = False

    def initImageTypes(self):
        for form in self.camera.formats:
            if(form == 'RGB Bayer'):
                rawbayer = 'RAW Bayer'
                imagetypegroup = []

                bayer_red_if = ImagingFunction()
                bayer_red_if.spatialfunction = 'bayer_red'
                bayer_red_if.spectralchannel =  SpectralChannel('bayer_red')
                imagetypegroup.append(bayer_red_if)

                bayer_green_if = ImagingFunction()
                bayer_green_if.spatialfunction = 'bayer_green'
                bayer_green_if.spectralchannel = SpectralChannel('bayer_green')
                imagetypegroup.append(bayer_green_if)

                bayer_blue_if = ImagingFunction()
                bayer_blue_if.spatialfunction = 'bayer_blue'
                bayer_blue_if.spectralchannel = SpectralChannel('bayer_blue')
                imagetypegroup.append(bayer_blue_if)

                self.imagingfunctions[rawbayer]=imagetypegroup

def createCameraConfiguration(name, interface, project):
    camerainterface = interface
    camera = createCamera(interface)
    cameraConfiguration = CameraConfiguration(name, camera)
    cameraConfiguration.initImageTypes()
    cameraConfiguration.interface = interface
    project.cameraConfiguration = cameraConfiguration
    return cameraConfiguration

class ImagingFunction:
    def __init__(self):
        self.spatialfunction = ''
        self.spectralchannel = None

class Project:
    def __init__(self, name):
        self.name = name
        self.cameraconfiguration = None
        self.shotdescriptions = []
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
        self.persFacade.loadcameraconfigurations()
        self.persFacade.loadprojects()
        for cameraconfiguration in self.persFacade.configdict.values():
            self.cameraconfigurations.append(cameraconfiguration)
        for project in self.persFacade.projectdict.values():
            self.projectList.append(project)

def createCameraConfiguration(name, interface, project):
    camerainterface = interface
    camera = createCamera(interface)
    cameraConfiguration = CameraConfiguration(name, camera)
    cameraConfiguration.initImageTypes()
    cameraConfiguration.interface = interface
    project.cameraconfiguration = cameraConfiguration
    print("createCamera Config: " + cameraConfiguration.name)
    return cameraConfiguration

def createCamera(interface):
    """used for unittesting.

    This function will be replace with a mock. Get rid of camerainterfacedependency.
    """
    return camerainterface.createCamera(interface)

class SpectralChannel:
    def __init__(self, name=''):
        self.identifier = name
        self.uuid = ''

class Shotdescription:
    def __init__(self, duration, imagetype):
        self.shots = []
        self.imagetype = imagetype
        self.duration = duration
        self.cameraconfiguration = None

    def capture(self):
        if self.imagetype == 'RAW Bayer':
            for shot in self.shots:
                image = self.cameraconfiguration.camera.capture(self.duration, self.imagetype)
                shot.images.append(image)

    def setNrOfShots(self, nrOfShots):
        self.shots = [Shot() for i in range(nrOfShots)]

def createShotdescription(nrOfShots, duration, project, imagetype):
    shotdesc = Shotdescription(duration, imagetype)
    shotdesc.cameraconfiguration = project.cameraconfiguration
    shotdesc.setNrOfShots(nrOfShots)
    project.shotdescriptions.append(shotdesc)
    return shotdesc

class Shot:
    def __init__(self):
        self.images = []

class Image:
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
        self.configdict = {}
        self.projectdict = {}

    def persistproject(self, project):
        self.database.insertproject(project.name)

    def persistcameraconfiguration(self, cameraconfig, project):
        configid = self.database.insertcameraconfiguration( cameraconfig.name, cameraconfig.interface )
        imagingfunctions = cameraconfig.imagingfunctions
        imagetypes = list(imagingfunctions.keys())
        for imagetype in imagetypes:
            imagingfunctionsOfimagetype = imagingfunctions[imagetype]
            for imgfunc in imagingfunctionsOfimagetype:
                spectraluuid = imgfunc.spectralchannel.uuid
                self.database.insertimagingfunction(spectraluuid, imgfunc.spatialfunction, imagetype, configid)
        self.database.addConfigToProject(project.name, configid)

    def persistshotdescription(self, shotdesc, project):
        projid = self.database.getProjectIdFor(project.name)
        self.database.insertshotdescription(shotdesc.duration, shotdesc.imagetype, projid[0])

    def getDatabase(self):
        self.database = persistence.Database()
        return self.database

    def loadcameraconfigurations(self):
        configtuples = self.database.getimagingfunctions()
        cameraconfigs = [self.loadcameraconfig(*configtupel)for configtupel in configtuples]

    def loadcameraconfig(self, rowid, name, interface, spectraluuid, spatialfunc, imgtype):
        if rowid not in self.configdict:
            camera = createCamera(interface)
            newcameraconfig = CameraConfiguration(name, camera)
            newcameraconfig.interface = interface
            self.configdict[rowid] = newcameraconfig

        imgfunc = ImagingFunction()
        spectral = SpectralChannel()
        spectral.uuid = spectraluuid
        imgfunc.spectralchannel = spectral
        imgfunc.spatialfunction = spatialfunc
        camconfig = self.configdict[rowid]
        imgfuncdict = camconfig.imagingfunctions
        if imgtype not in imgfuncdict:
            imgfuncdict[imgtype] = []

        imgfuncdict[imgtype].append(imgfunc)

        print('loadcameraconfig(): nr of config loaded ' + str(len(self.configdict.keys())))

    def loadproject(self, projectid, name, camconfigrowid):
        project = Project(name)
        if camconfigrowid in self.configdict:
            print('loadproject(): projconfig: ' + str(camconfigrowid))
            project.cameraconfiguration = self.configdict[camconfigrowid]

        self.projectdict[projectid] = project
        project.shotdescriptions = [self.loadshotdesc(*t) for t in self.database.getShotDescFor(projectid)]
        return project


    def loadshotdesc(self, shotdescid, duration, imgtype, poject):
        return Shotdescription(duration, imgtype)

    def loadprojects(self):
        projects = []
        projecttuples = self.database.getprojects()
        projects = [self.loadproject(*projecttuple) for projecttuple in projecttuples]
        return projects

    def persistOpticalSystem(self, opticalSystem, project):
        rowId = self.database.insertopticalsystem(opticalSystem)
        self.database.addOpticalSystemToProject(rowId, project.name)

    def persistAdapter(self, adapter):
        self.database.insertAdapter(adapter.name)

    def persistTelescope(self, telescope):
        self.database.insertTelescope(telescope.name)

    def loadopticalsystem(self, tupel):
        return Opticalsystem("", Adapter(tupel[0]), Telescope(tupel[1]))
