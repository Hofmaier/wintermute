import os
import os.path
import imp
import uuid
from astrophoto import camerainterface
from astrophoto import persistence
import copy

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

    def capture(self, shotdesc):
        shotdesc.capture()
        self.workspace.persFacade.writefits(shotdesc, self.currentProject)

    def capturebias(self, cameraconfiguration):
        pass

    def capturedark(self, shotdescription):
        pass

    def captureflat(self, shotdescription):
        self.workspace.captureflat(shotdescription)


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

    def capturebias(self):
        duration = 0
        shotdesc = createShotdescription(1, duration)
        shotdesc.cameraconfiguration = self
        img = Image()
        img.signal = shotdesc.capture()
        
        return shotdesc

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
        self.flats = []

    def load(self):
        camerainterface.load()
        camerainterface.getInterfaceNames()
        self.persFacade.loadcameraconfigurations()
        self.persFacade.loadAdapters()
        self.persFacade.loadTelescopes()
        self.persFacade.loadopticalsystems()
        self.persFacade.loadprojects()
        for cameraconfiguration in self.persFacade.configdict.values():
            self.cameraconfigurations.append(cameraconfiguration)
        for project in self.persFacade.projectdict.values():
            self.projectList.append(project)
        for adapter in self.persFacade.adapterdict.values():
            self.adapterList.append(adapter)
        for telescope in self.persFacade.telescopedict.values():
            self.telescopeList.append(telescope)

    def captureflat(self, lightshotdesc):
        flatshotdesc = None
        for flat in self.flats:
            if flat.compareflat(lightshotdesc):
                flatshotdesc = flat
            
        if flatshotdesc is None:
            flatshotdesc = copy.copy(lightshotdesc)
            flatshotdesc.kind = 'flat'
            flatshotdesc.images = []
            self.flats.append(flatshotdesc)

        flatshotdesc.captureflat()
        self.persFacade.writefits(flatshotdesc)

def createCameraConfiguration(name, interface, project):
    camerainterface = interface
    camera = createCamera(interface)
    cameraConfiguration = CameraConfiguration(name, camera)
    cameraConfiguration.initImageTypes()
    cameraConfiguration.interface = interface
    project.cameraconfiguration = cameraConfiguration
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
    def __init__(self, duration, imagetype, kind='light'):
        self.images = []
        self.imagetype = imagetype
        self.duration = duration
        self.cameraconfiguration = None
        self.imagingfunctions = []
        self.kind = kind

    def capture(self):
        if self.imagetype == 'RAW Bayer':
            for imgnr, img in enumerate(self.images):
                if img.filename is '':
                       img.signal = self.cameraconfiguration.camera.capture(self.duration, self.imagetype)

    def captureflat(self):
        img = Image()
        img.signal = self.cameraconfiguration.camera.capture(self.duration, self.imagetype)
        img.order = len(self.images)+1
        self.images.append(img)

    def setNrOfShots(self, nrOfShots):
        self.images = [Image(order=i+1) for i in range(nrOfShots)]
        
    def setimagetype(self, imagetype):
        self.imagetype = imagetype
        self.imagingfunctions.extend(self.cameraconfiguration.imagingfunctions[imagetype])

    def compareflat(self, shotdesc):
        if self.duration != shotdesc.duration:
            return False
        if self.cameraconfiguration is not shotdesc.cameraconfiguration:
            return False
        if self.imagetype != shotdesc.imagetype:
            return False
        if self.imagingfunctions != shotdesc.imagingfunctions:
            return False
        return True
    
    def taken(self):
        taken = True
        for img in self.images:
            if img.filename == '':
                taken = False

        return taken

def createShotdescription(nrOfShots, duration, project=None, imagetype='RAW Bayer', imagingfunction=None):
    shotdesc = Shotdescription(duration, imagetype)

    if project is not None:
        shotdesc.cameraconfiguration = project.cameraconfiguration
        if imagetype != '':
            shotdesc.imagingfunctions.extend(shotdesc.cameraconfiguration.imagingfunctions[imagetype])

        project.shotdescriptions.append(shotdesc)
    shotdesc.setNrOfShots(nrOfShots)
    return shotdesc

class Image:
    def __init__(self, img='', order=-1):
        self.signal = []
        self.filename = img
        self.order = order

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
        self.database = getDatabase()
        self.database.initschema()
        self.configdict = {}
        self.projectdict = {}
        self.loadedshotdescriptions = []
        self.adapterdict = {}
        self.telescopedict = {}
        self.optsystemdict = {}
        self.fitsmanager = getFITSManager()

    def persistproject(self, project):
        self.database.insertproject(project.name)
        try:
            os.mkdir(project.name)
        except OSError:
            pass

    def persistcameraconfiguration(self, cameraconfig, project):
        loadedconfigs = list(self.configdict.values())
        if cameraconfig in loadedconfigs:
            return
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
        if shotdesc in self.loadedshotdescriptions:
            return
        projid = self.database.getProjectIdFor(project.name)
        shotdescid = self.database.insertshotdescription(shotdesc.duration, shotdesc.imagetype, projid[0])
        for img in shotdesc.images:
            self.database.insertimage(shotdescid, img.filename)

    def writefits(self, shotdesc, project=None):
        desckind = shotdesc.kind
        if desckind == 'light':
            basedir = project.name
            duritstr = project.name + str(shotdesc.duration) + shotdesc.imagetype
        elif desckind == 'flat':
            basedir = 'calibrationframes/flats'
            duritstr = 'flat' + str(shotdesc.duration) + shotdesc.imagetype
        for image in shotdesc.images:
            if image.signal is not None:
                fn = duritstr + str(image.order) + '.fits'
                fn = fn.replace(' ','')
                image.filename = os.path.join(basedir, fn)
                self.fitsmanager.writefits(image.signal, image.filename)

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


    def loadproject(self, projectid, name, camconfigrowid, opticalSystemId):
        project = Project(name)
        if camconfigrowid in self.configdict:
            project.cameraconfiguration = self.configdict[camconfigrowid]

        self.projectdict[projectid] = project
        project.shotdescriptions = [self.loadshotdesc(*t) for t in self.database.getShotDescFor(projectid)]
        for shotdesc in project.shotdescriptions:
            shotdesc.cameraconfiguration = project.cameraconfiguration

        if opticalSystemId in self.optsystemdict:
            project.opticalSystem = self.optsystemdict[opticalSystemId]
        return project

    def loadshotdesc(self, shotdescid, duration, imgtype, project):
        shotdesc = Shotdescription(duration, imgtype)
        shotdesc.images = [Image(t[0]) for t in self.database.getImagesOf(shotdescid)]
        self.loadedshotdescriptions.append(shotdesc)
        return shotdesc

    def loadprojects(self):
        projects = []
        projecttuples = self.database.getprojects()
        projects = [self.loadproject(*projecttuple) for projecttuple in projecttuples]
        return projects

    def persistOpticalSystem(self, opticalSystem, project):
        adapterId = -1
        telescopeId = -1
        for rowId, adapter in self.adapterdict.items():
            if adapter is opticalSystem.adapter:
                adapterId = rowId
        for rowId, telescope in self.telescopedict.items():
            if telescope is opticalSystem.telescope:
                telescopeId = rowId
        self.database.persistopticalsystem(adapterId, telescopeId, project)

    def persistAdapter(self, adapter):
        rowId = self.database.persistAdapter(adapter.name)
        self.adapterdict[rowId] = adapter

    def persistTelescope(self, telescope):
        rowId = self.database.persistTelescope(telescope.name)
        self.telescopedict[rowId] = telescope

    def loadAdapters(self):
        adaptertuples = self.database.getAdapters()
        for adaptertuple in adaptertuples:
            self.adapterdict[adaptertuple[0]] = Adapter(adaptertuple[1])

    def loadTelescopes(self):
        telescopetuples = self.database.getTelescopes()
        for telescopetuple in telescopetuples:
            self.telescopedict[telescopetuple[0]] = Telescope(telescopetuple[1])

    def loadopticalsystems(self):
        optsystemtuples = self.database.getOptSystems()
        for optsystemtuple in optsystemtuples:
            adapter = None
            telescope = None
            if not optsystemtuple[1] == -1:
                adapter = self.adapterdict[optsystemtuple[1]]
            if not optsystemtuple[2] == -1:
                telescope = self.telescopedict[optsystemtuple[2]]
            optSystem = Opticalsystem('testing', adapter, telescope)
            self.optsystemdict[optsystemtuple[0]] = optSystem

def getDatabase():
    """used for unittesting.

    This function will be replace with a mock. Get rid of heavy database initialisation stuff.
    """
    return persistence.Database()

def getFITSManager():
    """used for unittesting
    """
    return persistence.FITSManager()
