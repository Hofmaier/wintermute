from distutils.core import setup, Extension

module1 = Extension('unicap',
                    include_dirs = ['/usr/local/include/unicap'],
                    sources = ['unicapmodule.c'],
                    libraries = ['unicap'],
                    library_dirs = ['/usr/local/lib']
                    )

setup (name = 'cameracontrol',
       version = '0.1',
       description = 'contains interfaces for astrophotography cameras',
       ext_modules = [module1])
                    
