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
        cameraconfigurationmock = workflow.CameraConfiguration(name, interface)
        mockfunc = mock.MagicMock(return_value = cameraconfigurationmock)
        workflow.createCameraConfiguration = mockfunc

        cameraconfiguration = session.createCameraConfiguration(name, interface)

        self.assertIsNotNone(cameraconfiguration)
        self.assertEqual(cameraconfiguration, cameraconfigurationmock)
        mockfunc.assert_called_with(name, interface, session.currentProject)
        self.assertIn(cameraconfiguration, session.workspace.cameraconfigurations)

class TestCameraConfiguration(unittest.TestCase):
    def test_ctor(self):
        name = 'imaging source 2012'
        camera = camerainterface.Camera()
        cameraconfig = workflow.CameraConfiguration(name, camera )
        self.assertIsNotNone(cameraconfig)
        self.assertEqual(cameraconfig.name, name)

    def test_createCameraConfiguration(self):
        name = 'tis dbk22au618.as'
        interface = 'tis'
        project = workflow.Project('jupiter')
        camera = camerainterface.Camera()
        createCameraMock = mock.MagicMock(return_value = camera)
        workflow.createCamera = createCameraMock

        cameraConfiguration = workflow.createCameraConfiguration(name, interface, project)
        self.assertIsNotNone(cameraConfiguration)
        self.assertIsNotNone(cameraConfiguration.camera)
        createCameraMock.assert_called_with(interface)
        

class Workspace(unittest.TestCase):
    def test_ctor(self):
        workspace = workflow.Workspace()
        self.assertIsNotNone(workspace)
        self.assertIsNotNone(workspace.cameraconfigurations)
