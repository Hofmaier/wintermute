from astrophoto import workflow
import unittest
import mock
from astrophoto import camerainterface

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
        self.assertEqual(writefitsmock.call_count, 2)

class TestCameraConfiguration(unittest.TestCase):
    def setUp(self):
        self.name = 'TIS dbk22au618.as 2012'

    def test_ctor(self):
        testcamera = camerainterface.Camera()
        testcamera.formats = ['RGB Bayer']
        cameraconfig = workflow.CameraConfiguration(self.name, testcamera )
        self.assertIsNotNone(cameraconfig)
        self.assertEqual(cameraconfig.name, self.name)

    def test_createCameraConfiguration(self):
        interface = 'tis'
        project = workflow.Project('jupiter')
        testcamera = camerainterface.Camera()
        testcamera.formats = ['RGB Bayer']
        createCameraMock = mock.MagicMock(return_value = testcamera)
        workflow.createCamera = createCameraMock

        cameraConfiguration = workflow.createCameraConfiguration(self.name, interface, project)
        self.assertIsNotNone(cameraConfiguration)
        self.assertIsNotNone(cameraConfiguration.camera)
        self.assertIs(testcamera, cameraConfiguration.camera)
        createCameraMock.assert_called_with(interface)
        self.assertIsNotNone(cameraConfiguration.imagingfunctions)
        self.assertEqual(list(cameraConfiguration.imagingfunctions.keys())[0], 'RAW Bayer')
        self.assertEqual(len(cameraConfiguration.imagingfunctions['RAW Bayer']), 3)

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

class TestSpectralChannel(unittest.TestCase):
    def test_ctor(self):
        spectralchannel = workflow.SpectralChannel()
        self.assertIsNotNone(spectralchannel)

class TestShotdescription(unittest.TestCase):
    def setUp(self):
        self.project = workflow.Project('jupiter')
        self.cameraconfiguration = workflow.CameraConfiguration('TIS dbk22au618.as 2012')
        self.project.cameraconfiguration = self.cameraconfiguration
        self.imagetype = 'RAW Bayer'
        self.duration = 3

    def test_ctor(self):
        shotdescription = workflow.Shotdescription(3, 'RAW Bayer')
        self.assertIsNotNone(shotdescription)

    def test_createShotdescription(self):
        nrOfShots = 5
        shotdesc = workflow.createShotdescription(nrOfShots, self.duration, self.project, self.imagetype)
        self.assertIsNotNone(shotdesc)
        self.assertEqual(shotdesc.duration, self.duration)
        self.assertEqual(shotdesc.imagetype, self.imagetype)
        self.assertEqual(len(shotdesc.images), nrOfShots)
        self.assertGreater(len(self.project.shotdescriptions), 0)
        self.assertIsNotNone(shotdesc.cameraconfiguration)
        self.assertEqual(shotdesc.images[0].order, 1)

    def test_capture(self):

        cameramock = mock.MagicMock()
        testimage = [1,2,3,4]
        cameramock.capture = mock.MagicMock(return_value=testimage)
        self.cameraconfiguration.camera = cameramock
        shotdesc = workflow.createShotdescription(1, self.duration, self.project, self.imagetype)
        shotdesc.cameraconfiguration = self.cameraconfiguration
        print('test_capture: before capture ')
        capturedImg = shotdesc.capture()
        self.assertIsNotNone(capturedImg)
        self.assertGreater(len(shotdesc.images),0)
        self.assertIsNotNone(shotdesc.images[0])
        cameramock.capture.assert_called_with(self.duration, self.imagetype)


class TestPersistenceFacade(unittest.TestCase):
    def setUp(self):
        self.dbmock = mock.Mock()
        workflow.getDatabase = mock.Mock(return_value=self.dbmock)

        self.filename = 'jupiter3RAWBayer1.fits'
        t = (self.filename,)
        l = [t]
        self.dbmock.getImagesOf = mock.MagicMock(return_value=l)
        self.persistencefacade = workflow.PersistenceFacade()

    def test_ctor(self):
        self.assertIsNotNone(self.persistencefacade.database)

    def test_persistproject(self):
        dbmock = mock.MagicMock()
        projectname = 'jupiter'
        project = workflow.Project(projectname)
        dbmock.insertproject.return_value = 'True'

        self.persistencefacade.persistproject(project)
        self.persistencefacade.database.insertproject.assert_called_with(project.name)

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
        self.persistencefacade.writefits(img, shotdesc, proj)
        self.assertEqual(img.filename, 'jupiter3RAWBayer1.fits')

class TestSpectralChannel(unittest.TestCase):
    def test_ctor(self):
        spectralchannel = workflow.SpectralChannel('bayer_red')
        self.assertIsNotNone(spectralchannel.uuid)
