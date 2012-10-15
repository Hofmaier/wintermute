class Session:
    def __init__(self, factory=None):
        if factory == None:
            factory = ProjectFactory()
        self.projectFactory = factory

    def createProject(self, name):
        self.projectFactory.createProject(name)

class ProjectFactory:
    pass

class Project:
    pass
