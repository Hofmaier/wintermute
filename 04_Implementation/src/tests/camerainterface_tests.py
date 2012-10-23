import unittest
from astrophoto import camerainterface
import imp

class TestCamera(unittest.TestCase):

    def setUp(self):
        self.name = 'interfacemock'
        moduletuple = imp.find_module('camerainterfacemock', ['tests'])
        self.modulemock = imp.load_module('camerainterfacemock', *moduletuple)
        camerainterface.moduledict[self.name] = self.modulemock
    
    def test_createCamera(self):
        camera = camerainterface.createCamera(self.name)
        self.assertIsNotNone(camera)
        
    def test_getModule(self):
        module =  camerainterface.getModule(self.name)
        self.assertIsNotNone(module)
        self.assertEqual(module, camerainterface.moduledict[self.name])
        
    def test_getImageTypes(self):
        expectedType = [camerainterface.ImageType.Bayermatrix]
        camera = self.modulemock.createCameraControl()
        imageTypeList = camera.getImageTypes()
        self.assertIsNotNone(imageTypeList)
        self.assertEqual(imageTypeList, expectedType)

class TestImageType(unittest.TestCase):
    
    def test_simpleUsage(self):
        imagetype = camerainterface.ImageType.Bayermatrix
        self.assertIsNotNone(imagetype)
        self.assertEqual(camerainterface.ImageType.toStr[imagetype], 'Bayer-Matrix')

