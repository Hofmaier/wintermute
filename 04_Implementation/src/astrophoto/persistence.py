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

    def insertproject(self, name, opticalSystemId):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM projects WHERE name = ?', (name,))
        exists = cursor.fetchone()
        if exists is None:
            cursor.execute('INSERT INTO projects (name, opticalSystemID) VALUES (?, ?)', (name, opticalSystemId, ))
        else:
            cursor.execute('UPDATE projects set opticalSystemID = ? WHERE name = ?', (opticalSystemId, name, ))
        self.connection.commit()
        cursor.close()

    def insertcameraconfiguration(self, name, interface):
        cursor = self.connection.cursor()

        cursor.execute('INSERT INTO cameraconfigurations (name, interface) VALUES (?, ?)', ( name, interface ))
        self.connection.commit()
        return cursor.lastrowid

    def insertimagingfunction(self, spectraluuid, spatialfunc, imagetype, configid):
        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO imagingfunctions
        (spectralchanneluuid, spatialfunction, imagetype, cameraconfiguration)
        VALUES (?,?,?,?)
        """, (spectraluuid, spatialfunc, imagetype, configid))
        self.connection.commit()
        

    def insertshotdescription(self, duration):
        pass

    def insertOpticalSystem(self, adapterName, telescopeName):
        cursor = self.connection.cursor()
        queryparameter = (adapterName, telescopeName, )
        cursor.execute('SELECT ROWID FROM opticSystems WHERE adapterName = ? AND telescopeName = ?', queryparameter)
        exists = cursor.fetchone()
        if exists is None:
            cursor.execute('INSERT INTO opticSystems (adapterName, telescopeName) VALUES (?,?)', queryparameter)
            cursor.execute('SELECT last_insert_rowid()')
            exists = cursor.fetchone()
        self.connection.commit()
        cursor.close()
        return exists[0]    

    def insertAdapter(self, adapterName):
        cursor = self.connection.cursor()
        queryparameter = (adapterName, )
        cursor.execute('SELECT name FROM adapters WHERE name = ?', queryparameter)
        exists = cursor.fetchone()
        if exists is None:
            cursor.execute('INSERT INTO adapters (name) VALUES (?)', queryparameter)
        cursor.close()

    def insertTelescope(self, telescopeName):
        cursor = self.connection.cursor()
        queryparameter = (telescopeName, )
        cursor.execute('SELECT name FROM telescopes WHERE name = ?', queryparameter)
        exists = cursor.fetchone()
        if exists is None:
            cursor.execute('INSERT INTO telescopes (name) VALUES (?)', queryparameter)
        cursor.close()

    def getprojects(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT name FROM projects')
        projecttuples = cursor.fetchall()
        cursor.close()
        return projecttuples

    def getCameraconfigOf(self, project):
        cursor = self.connection.cursor()
        queryparameter = (project,)
        print(queryparameter)
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

    def getOpticalsystemOf(self, project):
        cursor = self.connection.cursor()
        queryparameter = (project.name,)
        cursor.execute("""
        SELECT adapterName, telescopeName FROM opticSystems
        INNER JOIN projects
        ON projects.opticalSystemID = opticSystems.ROWID
        WHERE projects.name = ?
        """, queryparameter)
        opticSystemTupel = cursor.fetchone()
        cursor.close()
        return opticSystemTupel

def createDatabase():
    database = Database()
    return database
