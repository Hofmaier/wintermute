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
        self.assertEqual(cameraConfiguration.imagingfunctions.keys()[0], 'RAW Bayer')
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

class TestShotdesciption(unittest.TestCase):
    def setUp(self):
        self.project = workflow.Project('jupiter')
        self.cameraconfiguration = workflow.CameraConfiguration('TIS dbk22au618.as 2012')
        self.project.cameraconfiguration = self.cameraconfiguration

    def test_ctor(self):
        shotdescription = workflow.Shotdescription(3, 'RAW Bayer')
        self.assertIsNotNone(shotdescription)

    def test_createShotdescription(self):
        nrOfShots = 5
        duration = 30

        imagetype = 'RAW Bayer'
        shotdesc = workflow.createShotdescription(nrOfShots, duration, self.project, imagetype)
        self.assertIsNotNone(shotdesc)
        self.assertEqual(shotdesc.duration, duration)
        self.assertEqual(shotdesc.imagetype, imagetype)
        self.assertEqual(len(shotdesc.shots), nrOfShots)
        self.assertGreater(len(self.project.shotdescriptions), 0)
        self.assertIsNotNone(shotdesc.cameraconfiguration)

    def test_capture(self):
        shotdesc = workflow.createShotdescription(1, 30, self.project, 'RAW Bayer')
        cameramock = mock.MagicMock()
        testimage = [1,2,3,4]
        cameramock.capture = mock.MagicMock(return_value=testimage)
        self.cameraconfiguration.camera = cameramock
        shotdesc.capture()
        self.assertGreater(len(shotdesc.shots),0)
        self.assertIsNotNone(shotdesc.shots[0].images[0])

class TestShot(unittest.TestCase):

    def test_ctor(self):
        shot = workflow.Shot()
        self.assertIsNotNone(shot)

class TestPersistenceFacade(unittest.TestCase):
    def setUp(self):
        self.persistencefacade = workflow.PersistenceFacade()

    def test_ctor(self):
        persistencefacade = workflow.PersistenceFacade()
        dbmock = mock.Mock()
        persistencefacade.getDatabase = mock.Mock(return_value=dbmock)
        self.assertIsNotNone(persistencefacade.database)

    def test_persistproject(self):
        dbmock = mock.MagicMock()
        projectname = 'jupiter'
        project = workflow.Project(projectname)
        dbmock.insertproject.return_value = 'True'
        persistencefacade = workflow.PersistenceFacade()
        persistencefacade.getDatabase = mock.MagicMock(return_value=dbmock)
        persistencefacade.database = dbmock
        persistencefacade.persistproject(project)
        dbmock.insertproject.assert_called_with(project.name)

    def test_loadprojects(self):
        projects = self.persistencefacade.loadprojects()
        self.assertIsNotNone(projects)
        self.assertEqual(1, len(projects))

class TestSpectralChannel(unittest.TestCase):
    def test_ctor(self):
        spectralchannel = workflow.SpectralChannel('bayer_red')
        self.assertIsNotNone(spectralchannel.uuid)
