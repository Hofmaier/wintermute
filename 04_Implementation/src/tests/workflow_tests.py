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
    def test_ctor(self):
        name = 'imaging source 2012'
        testcamera = camerainterface.Camera()
        testcamera.formats = ['RGB Bayer']
        cameraconfig = workflow.CameraConfiguration(name, testcamera )
        self.assertIsNotNone(cameraconfig)
        self.assertEqual(cameraconfig.name, name)

    def test_createCameraConfiguration(self):
        name = 'tis dbk22au618.as'
        interface = 'tis'
        project = workflow.Project('jupiter')
        testcamera = camerainterface.Camera()
        testcamera.formats = ['RGB Bayer']
        createCameraMock = mock.MagicMock(return_value = testcamera)
        workflow.createCamera = createCameraMock

        cameraConfiguration = workflow.createCameraConfiguration(name, interface, project)
        self.assertIsNotNone(cameraConfiguration)
        self.assertIsNotNone(cameraConfiguration.camera)
        self.assertIs(testcamera, cameraConfiguration.camera)
        createCameraMock.assert_called_with(interface)
        self.assertIsNotNone(cameraConfiguration.imagetypes)
        self.assertIsNotNone(cameraConfiguration.imagetypes[0])
        self.assertEqual(cameraConfiguration.imagetypes[0], 'RAW Bayer')

        self.assertEqual(len(cameraConfiguration.imagingfunctions[cameraConfiguration.imagetypes[0]]), 3)

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
    def test_ctor(self):
        shotdescription = workflow.Shotdescription(3, 'RAW Bayer')
        self.assertIsNotNone(shotdescription)

    def test_createShotdescription(self):
        nrOfShots = 5
        duration = 30
        project = workflow.Project('jupiter')
        imagetype = 'RAW Bayer'
        shotdescription = workflow.createShotdescription(nrOfShots, duration, project, imagetype)
        self.assertIsNotNone(shotdescription)
        
        # self.assertEqual(shotDescription.duration, duration)
        # self.assertEqual(shotDescription.temperature, temperature)

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
