import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("workflow.db")
        self.connection.row_factory = sqlite3.Row

    def initschema(self):
        cursor = self.connection.cursor()
        with open('astrophoto/workflowschema.sql','r') as f:
            schema = f.read();
        cursor.executescript(schema)

    def insertproject(self, name):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO projects (name) VALUES (?)', (name,))
        self.connection.commit()
        cursor.close()

    def insertcameraconfiguration(self, name, project, interface):
        cursor = self.connection.cursor()
        queryparameter = (project,)
        cursor.execute("""
        SELECT ROWID FROM projects
        WHERE name = ?
        """, queryparameter)
        projectrow = cursor.fetchone()

        cursor.execute('INSERT INTO cameraconfigurations (name, project, interface) VALUES (?, ?, ?)', ( name, projectrow[0], interface ))
        self.connection.commit()
        cursor.close()

    def insertshotdescription(self, duration, 

    def getprojects(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT name FROM projects')
        projecttuples = cursor.fetchall()
        cursor.close()
        return projecttuples

    def getCameraconfigOf(self, project):
        cursor = self.connection.cursor()
        queryparameter = (project,)
        cursor.execute("""
        SELECT cc.name, cc.interface FROM cameraconfigurations cc
        INNER JOIN projects ON cc.project = projects.ROWID
        WHERE projects.name = ?
        """, queryparameter)
        cameraconfig = cursor.fetchone()
        cursor.close()
        return cameraconfig

    def getCameraOf(self, cameraconfig):
        cursor = self.connection.cursor()
        queryparamater = (cameraconfig,)
        cursor.execute("""
        SELECT interface FROM cameras
        INNER JOIN cameraconfigurations
        ON cameras.cameraconfig = cameraconfigurations.ROWID
        WHERE cameraconfigurations.name = ?
        """, queryparameter)
        camera = cursor.fetchone()
        cursor.close()
        return camera

def createDatabase():
    database = Database()
    return database
