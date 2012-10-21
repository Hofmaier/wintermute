import unittest
from astrophoto import camerainterface
import imp

class TestCamera(unittest.TestCase):

    def setUp(self):
        self.name = 'interfacemock'
        moduletuple = imp.find_module('camerainterfacemock', ['tests'])
        modulemock = imp.load_module('camerainterfacemock', *moduletuple)
        camerainterface.moduledict[self.name] = modulemock
    
    def test_createCamera(self):
        camera = camerainterface.createCamera(self.name)
        self.assertIsNotNone(camera)
        
    def test_getModule(self):
        module =  camerainterface.getModule(self.name)
        self.assertIsNotNone(module)
        self.assertEqual(module, camerainterface.moduledict[self.name])
