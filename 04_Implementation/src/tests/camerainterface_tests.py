import unittest
from astrophoto import camerainterface

class TestCamera(unittest.TestCase):
    def test_createCamera(self):
        name = 'tis'
        camera = camerainterface.createCamera(name)
        self.assertIsNotNone(camera)
