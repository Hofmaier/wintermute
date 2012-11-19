import numpy
import pyfits
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
        cursor.execute('INSERT INTO projects (name) VALUES (?)', (name, ))

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

    def insertshotdescription(self, duration, imagetype, projid):
        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO shotdescriptions
        ( imagetype, duration, project)
        VALUES (?, ?, ?)
        """, ( imagetype, duration, projid))
        self.connection.commit()
        return cursor.lastrowid

    def insertshot(self, shotdescid):
        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO shots
        ( shotdescription )
        VALUES (?)""", (shotdescid,))
        self.connection.commit()

    def getprojects(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT ROWID, name, cameraconfiguration FROM projects')
        projecttuples = cursor.fetchall()
        cursor.close()
        return projecttuples

    def getProjectIdFor(self, name):
        cursor = self.connection.cursor()
        t = (name,)
        cursor.execute('SELECT ROWID FROM projects WHERE name=?', t)
        return cursor.fetchone()

    def getShotDescFor(self, projectid):
        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT ROWID, duration, imagetype, project
        FROM shotdescriptions
        WHERE project=?
        """, (projectid,))
        return cursor.fetchall()

    def getimagingfunctions(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT cc.ROWID, cc.name, cc.interface, if.spectralchanneluuid,
        if.spatialfunction, if.imagetype
        FROM cameraconfigurations cc
        INNER JOIN imagingfunctions if ON cc.ROWID = if.cameraconfiguration
        """)
        return cursor.fetchall()

    def addConfigToProject(self, projectname, configid):
        cursor = self.connection.cursor()
        t = (configid, projectname)
        cursor.execute("""
        UPDATE projects SET cameraconfiguration = ?
        WHERE name = ?
        """, t)
        self.connection.commit()
        cursor.close()

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



    def insertOpticalSystem(self, opticalSystem):
        if not opticalSystem.adapter is None:
            pass
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

class FITSManager():

    def writefits(self, image, filename):
        """save image in fitsformat.
        
        image is a list of 640 x 480  integers. it contains intensity values of an image.
        """
        n = numpy.array(image)
        matrix = n.reshape(480, 640)
        int8matrix = numpy.int32(matrix)
        hdu = pyfits.PrimaryHDU(int8matrix)
        hdu.writeto(filename)

def createDatabase():
    database = Database()
    return database
