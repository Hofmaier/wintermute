import glob, os
from astrophoto import persistence
from astrophoto import workflow
from astrophoto import camerainterface

filelist = glob.glob("*.db")
for f in filelist:
    os.remove(f)

pf = workflow.PersistenceFacade()

project = workflow.Project('jupiter')
pf.persistproject(project)


camerainterface.getInterfaceNames()
cam = camerainterface.Camera()
cam.formats = ['RGB Bayer']
config = workflow.CameraConfiguration('the imaging source 2012', cam)
config.interface = 'The Imaging Source'
config.initImageTypes()
project.cameraconfiguration = config

pf.persistcameraconfiguration(config, project)

shotdesc = workflow.createShotdescription(1,3, project, 'RAW Bayer')
pf.persistshotdescription(shotdesc, project)

pf.configdict = {}
pf.projectdict = {}

pf.loadcameraconfigurations()
pf.loadprojects()

projlist = pf.projectdict.values()
for proj in projlist:
    print('Project: ' + proj.name)
    print('Cameraconfiguration: ' + proj.cameraconfiguration.name)
    imgfuncdict = proj.cameraconfiguration.imagingfunctions
    print('Nr of Image types: ' + str(len(imgfuncdict)))
    for shotdesc in proj.shotdescriptions:
        print('Shotdesciption: Duration ' + str(shotdesc.duration) + ' ImageType: ' + shotdesc.imagetype )
        
