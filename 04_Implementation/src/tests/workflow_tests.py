from astrophoto import workflow
import unittest
import mock
from astrophoto import camerainterface
import copy

class TestProject(unittest.TestCase):
    def test_project(self):
        project = workflow.Project('jupiter')
        self.assertEqual(project.name, 'jupiter')

class TestSession(unittest.TestCase):

    def setUp(self):
        mockdb = mock.MagicMock()
        mockdb.initschema = mock.MagicMock()
        workflow.getDatabase = mock.MagicMock(return_value=mockdb)
        self.session = workflow.Session()
        self.projectname = 'jupiter'

    def test_ctor(self):
        session = workflow.Session()
        self.assertIsNotNone(session)
        self.assertIsNotNone(session.workspace)

    def test_createProject(self):
        project = self.session.createProject(self.projectname)
        self.assertIsNotNone(project)
        self.assertEqual(project.name, self.projectname)
        self.assertEqual(self.session.currentProject, project)

    def test_createCameraConfiguration(self):
        session = workflow.Session()
        project = workflow.Project('jupiter')
        session.currentProject = project
        name = 'tis dbk22au618.as 2012'
        interface = 'tis'
        cameramock = camerainterface.Camera()
        cameraconfigurationmock = workflow.CameraConfiguration(name )
        mockfunc = mock.MagicMock(return_value = cameraconfigurationmock)
        workflow.createCameraConfiguration = mockfunc

        cameraconfiguration = session.createCameraConfiguration(name, interface)

        self.assertIsNotNone(cameraconfiguration)
        self.assertEqual(cameraconfiguration, cameraconfigurationmock)
        mockfunc.assert_called_with(name, interface, session.currentProject)
        self.assertIn(cameraconfiguration, session.workspace.cameraconfigurations)

    def test_getInterfaceNames(self):
        session = workflow.Session()

    def test_capture(self):
        shotdesc = workflow.Shotdescription(3, 'RAW Bayer')
        img1 = workflow.Image()
        img1.order = 1
        img2 = workflow.Image()
        img2.order = 2
        imageserie = [img1, img2]
        self.currentProject = workflow.Project('jupiter')
        shotdesc.capture = mock.MagicMock(return_value = imageserie)
        writefitsmock = mock.MagicMock()
        self.session.workspace.persFacade.writefits = writefitsmock
        self.session.capture(shotdesc)
        shotdesc.capture.assert_called_with()
        self.assertEqual(writefitsmock.call_count, 1)

    def test_captureflat(self):
        session = workflow.Session()
        workspace = mock.MagicMock()
        workspace.captureflat = mock.MagicMock()
        session.workspace = workspace
        shotdesc = workflow.Shotdescription(3,'RAW Bayer')
        session.captureflat(shotdesc)
        session.workspace.captureflat.assert_called_with(shotdesc)

class TestCameraConfiguration(unittest.TestCase):
    def setUp(self):
        self.name = 'TIS dbk22au618.as 2012'
        self.project = workflow.Project('jupiter')
        self.testcamera = camerainterface.Camera()
        self.testcamera.formats = ['RGB Bayer']
        self.testimg = [1,2,3,4]
        self.capture = mock.MagicMock(return_value = self.testimg)
        self.testcamera.capture = self.capture
        createCameraMock = mock.MagicMock(return_value = self.testcamera)

        workflow.createCamera = createCameraMock

    def test_ctor(self):
        testcamera = camerainterface.Camera()
        testcamera.formats = ['RGB Bayer']
        cameraconfig = workflow.CameraConfiguration(self.name, testcamera )
        self.assertIsNotNone(cameraconfig)
        self.assertEqual(cameraconfig.name, self.name)

    def test_createCameraConfiguration(self):
        interface = 'tis'

        cameraConfiguration = workflow.createCameraConfiguration(self.name, interface, self.project)
        self.assertIsNotNone(cameraConfiguration)
        self.assertIsNotNone(cameraConfiguration.camera)
        self.assertIs(self.testcamera, cameraConfiguration.camera)
        workflow.createCamera.assert_called_with(interface)
        self.assertIsNotNone(cameraConfiguration.imagingfunctions)
        self.assertEqual(list(cameraConfiguration.imagingfunctions.keys())[0], 'RAW Bayer')
        self.assertEqual(len(cameraConfiguration.imagingfunctions['RAW Bayer']), 3)

    def test_capturebias(self):
        camconfig = workflow.createCameraConfiguration(self.name,  'tis', self.project)
        self.assertIs(camconfig.camera, self.testcamera)
        shotdesc = camconfig.capturebias()
        self.capture.assert_called_with(0, 'RAW Bayer')
        self.assertIsNotNone(shotdesc)
        self.assertEqual(len(shotdesc.images), 1)
        for img in shotdesc.images:
            self.assertIsNotNone(img)
            self.assertIs(img.signal, self.testimg)
        self.assertIs(shotdesc.cameraconfiguration, camconfig)
        camconfig.camera.capture.assert_called_with(0, 'RAW Bayer')

class TestTelescope(unittest.TestCase):
    def test_ctor(self):
        name = 'Celestron Edge HD 1400'
        telescope = workflow.Telescope(name)
        self.assertIsNotNone(telescope)
        self.assertEqual(telescope.name, name)

class TestAdapter(unittest.TestCase):
    def test_ctor(self):
        name = 'SBIG Starlight Adapter'
        adapter = workflow.Adapter(name)
        self.assertIsNotNone(adapter)
        self.assertEqual(adapter.name, name)

class TestOpticalSystem(unittest.TestCase):
    def test_ctor(self):
        adapter = workflow.Adapter("SBIG Starlight Adapter")
        telescope = workflow.Telescope("Celestron Edge HD 1400")
        name = 'SBIGCelestronConfig'
        opticalSystem = workflow.Opticalsystem(name, adapter, telescope)
        self.assertIsNotNone(opticalSystem)
        self.assertEqual(opticalSystem.adapter, adapter)
        self.assertEqual(opticalSystem.telescope, telescope)
        self.assertEqual(opticalSystem.name, name)

class TestWorkspace(unittest.TestCase):
    def test_ctor(self):
        workspace = workflow.Workspace()
        self.assertIsNotNone(workspace)
        self.assertIsNotNone(workspace.cameraconfigurations)

    def test_captureflat(self):
        workspace = workflow.Workspace()
        workspace.flats = []
        shotdesc1 = workflow.Shotdescription(3, 'RAW Bayer')
        cameraconfig = workflow.CameraConfiguration('TIS dbk22au618.as 2012')
        cameraconfig.camera = mock.MagicMock()
        cameraconfig.camera.capture = mock.MagicMock(return_value=[1,2,3,4])
        shotdesc1.cameraconfiguration = cameraconfig
        shotdesc1.setNrOfShots(5)
        workspace.persFacade.writefits = mock.MagicMock()
        workspace.captureflat(shotdesc1)
        self.assertEqual(len(workspace.flats), 1)
        flatshotdesc = workspace.flats[0]        
        self.assertEqual(len(flatshotdesc.images), 1)

        firstimg = flatshotdesc.images[0]
        self.assertEqual(firstimg.order, 1)
        self.assertEqual(flatshotdesc.kind, 'flat')
        shotdesc2 = workflow.Shotdescription(3, 'RAW Bayer')
        shotdesc2.cameraconfiguration = cameraconfig
        workspace.captureflat(shotdesc2)
        self.assertEqual(len(workspace.flats), 1)
        workspace.persFacade.writefits.assert_called_with(flatshotdesc)
        shotdesc3 = workflow.Shotdescription(2, 'RAW Bayer')
        shotdesc3.cameraconfiguration = cameraconfig
        workspace.captureflat(shotdesc3)
        self.assertEqual(len(workspace.flats), 2)

class TestSpectralChannel(unittest.TestCase):
    def test_ctor(self):
        spectralchannel = workflow.SpectralChannel()
        self.assertIsNotNone(spectralchannel)

class TestShotdescription(unittest.TestCase):
    def setUp(self):
        self.project = workflow.Project('jupiter')
        self.cameraconfiguration = workflow.CameraConfiguration('TIS dbk22au618.as 2012')
        camera = mock.MagicMock()
        camera.formats = ['RGB Bayer']
        testimage = [1,2,3,4]
        camera.capture = mock.MagicMock(return_value=testimage)
        self.cameraconfiguration.camera = camera
        self.cameraconfiguration.initImageTypes()
        self.project.cameraconfiguration = self.cameraconfiguration
        self.imagetype = 'RAW Bayer'
        self.duration = 0.03
        self.shotdesc = workflow.createShotdescription(1, self.duration, self.project, self.imagetype)

    def test_ctor(self):
        shotdescription = workflow.Shotdescription(3, 'RAW Bayer')
        self.assertIsNotNone(shotdescription)
        self.assertEqual(shotdescription.kind, 'light')

    def test_createShotdescription(self):
        nrOfShots = 5
        shotdesc = workflow.createShotdescription(nrOfShots, self.duration, self.project, self.imagetype)
        self.assertEqual(len(self.cameraconfiguration.imagingfunctions['RAW Bayer']),3)
        self.assertIsNotNone(shotdesc)
        self.assertEqual(shotdesc.duration, self.duration)
        self.assertEqual(shotdesc.imagetype, self.imagetype)
        self.assertEqual(len(shotdesc.images), nrOfShots)
        self.assertGreater(len(self.project.shotdescriptions), 0)
        self.assertIsNotNone(shotdesc.cameraconfiguration)
        self.assertEqual(shotdesc.images[0].order, 1)
        self.assertEqual(len(shotdesc.imagingfunctions), 3)

    def test_capture(self):
        cameramock = mock.MagicMock()
        self.cameraconfiguration.camera = cameramock
        capturedImg = self.shotdesc.capture()
        self.assertGreater(len(self.shotdesc.images),0)
        self.assertIsNotNone(self.shotdesc.images[0])
        cameramock.capture.assert_called_with(self.duration, self.imagetype)

    def test_captureflat(self):
        flatshotdesc = workflow.createShotdescription(0,self.duration,self.project,self.imagetype)
        flatshotdesc.kind = 'flat'
        flatshotdesc.captureflat()
        self.assertEqual(len(flatshotdesc.images),1)
        for img in flatshotdesc.images:
            self.assertEqual(len(img.signal), 4)

    def test_compareflat(self):
        equallightshotdesc = workflow.createShotdescription(1, self.duration, self.project, self.imagetype)
        flatshotdesc = copy.copy(equallightshotdesc)
        flatshotdesc.cameraconfiguration = self.cameraconfiguration
        self.assertTrue(equallightshotdesc.imagingfunctions == flatshotdesc.imagingfunctions)
        self.assertFalse(equallightshotdesc.imagingfunctions != flatshotdesc.imagingfunctions)
        self.assertTrue(flatshotdesc.compareflat(equallightshotdesc))
        differentshotdesc = workflow.createShotdescription(1,3,self.project, self.imagetype)
        self.assertFalse(flatshotdesc.compareflat(differentshotdesc))

    def test_setimagetype(self):
        shotdesc = workflow.createShotdescription(0,0,self.project,'')
        self.assertEqual(len(shotdesc.imagingfunctions),0)
        shotdesc.setimagetype('RAW Bayer')
        self.assertEqual(shotdesc.imagetype, 'RAW Bayer')
        self.assertEqual(len(shotdesc.imagingfunctions),3)

    def test_taken(self):
        self.assertFalse(self.shotdesc.taken())
        self.shotdesc.capture()
        for img in self.shotdesc.images:
            img.filename = 'jupiter/jupiter3RAWBayer1.fits'
        self.assertTrue(self.shotdesc.taken())
        
class TestPersistenceFacade(unittest.TestCase):
    def setUp(self):
        self.dbmock = mock.Mock()
        workflow.getDatabase = mock.Mock(return_value=self.dbmock)
        self.filename = 'jupiter/jupiter3RAWBayer1.fits'
        t = (self.filename,)
        l = [t]
        self.dbmock.getImagesOf = mock.MagicMock(return_value=l)
        self.persistencefacade = workflow.PersistenceFacade()
        fitsmanager = mock.MagicMock()
        fitsmanager.writefits = mock.MagicMock()
        self.persistencefacade.fitsmanager = fitsmanager
        projectname = 'jupiter'
        self.project = workflow.Project(projectname)
        self.testcamera = camerainterface.Camera()
        self.testcamera.formats = ['RGB Bayer']
        self.cameraconfig = workflow.CameraConfiguration('TIS dbk22au618.as 2012', self.testcamera )
        self.cameraconfig.initImageTypes()
        self.project.cameraconfiguration = self.cameraconfig

    def test_ctor(self):
        self.assertIsNotNone(self.persistencefacade.database)

    def test_persistproject(self):
        dbmock = mock.MagicMock()
        dbmock.insertproject.return_value = 'True'
        self.persistencefacade.persistproject(self.project)
        self.persistencefacade.database.insertproject.assert_called_with(self.project.name)

    def test_persistshotdescription(self):
        self.dbmock.insertshotdescription = mock.MagicMock(return_value=1)
        projid = (1,)
        self.dbmock.getProjectIdFor = mock.MagicMock(return_value=projid)
        duration = 0.03
        shotdesc = workflow.createShotdescription(5, duration, self.project)
        
        self.persistencefacade.persistshotdescription( shotdesc, self.project)
        self.dbmock.insertshotdescription.assert_called_with(duration, 'RAW Bayer', projid[0])

    def test_loadprojects(self):
        t = (1, 'jupiter', 1, 1)
        l = [t]
        self.dbmock.getprojects = mock.MagicMock(return_value=l)
        sdtl = [(1,3,'RAW Bayer', 1)]
        self.dbmock.getShotDescFor = mock.MagicMock(return_value=sdtl)

        projects = self.persistencefacade.loadprojects()
        self.assertIsNotNone(projects)
        self.assertEqual(1, len(projects))

    def test_loadshotdesc(self):
        dur = 1
        imgt = 'RAW Bayer'

        shotdesc = self.persistencefacade.loadshotdesc(1, dur, imgt, None)
        self.assertEqual(len(shotdesc.images), 1)
        self.assertEqual(shotdesc.images[0].filename, self.filename)

    def test_writefits(self):
        proj = workflow.Project('jupiter')
        duration = 3
        imagetype = 'RAW Bayer'
        shotdesc = workflow.Shotdescription(duration, imagetype)
        shotdesc.setNrOfShots(1)
        img = shotdesc.images[0]
        self.persistencefacade.writefits( shotdesc, proj)
        self.assertEqual(img.filename, 'jupiter/jupiter3RAWBayer1.fits')
        
    def test_writefits_with_flat(self):
        flatshotdesc = workflow.Shotdescription(3, 'RAW Bayer')
        flatshotdesc.kind = 'flat'
        img = workflow.Image()
        img.order = 1
        flatshotdesc.images.append(img)
        self.persistencefacade.writefits(flatshotdesc)
        self.assertEqual(img.filename, 'calibrationframes/flats/flat3RAWBayer1.fits')
            

class TestSpectralChannel(unittest.TestCase):
    def test_ctor(self):
        spectralchannel = workflow.SpectralChannel('bayer_red')
        self.assertIsNotNone(spectralchannel.uuid)
