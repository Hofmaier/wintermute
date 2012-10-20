from astrophoto import workflow
import unittest

class TestProject(unittest.TestCase):
    def test_project(self):
        project = workflow.Project('jupiter')
        self.assertEqual(project.name, 'jupiter')


class TestSession(unittest.TestCase):
    def test_ctor(self):
        session = workflow.Session()
        self.assertIsNotNone(session)

    def test_createCameraConfiguration(self):
        session = workflow.Session()
        name = 'Imaging Source'
        interface = 'tis'
        camera = session.createCameraConfiguration(name, interface)
        self.assertIsNotNone(camera)

class TestCameraConfiguration(unittest.TestCase):
    def test_ctor(self):
        name = 'imaging source 2012'
        camera = workflow.CameraConfiguration(name)
        self.assertIsNotNone(camera)
        self.assertEqual(camera.name, name)

    def test_createCameraConfiguration(self):
        name = 'tis dbk22au618.as'
        interface = 'tis'
        project = workflow.Project('jupiter')
        cameraConfiguration = workflow.createCameraConfiguration(name, interface, project)
        self.assertIsNotNone(cameraConfiguration)

