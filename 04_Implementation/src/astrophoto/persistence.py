import sqlite3

class PersistenceFacade:

    def __init__(self):
        self.database = createDatabase()

    def insertproject(self, name):
        self.database.insertproject(name)

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("workflow.db")

    def init(self):
        cursor = self.connection.cursor()
        with open('workflowschema.sql','r') as f:
            schema = f.read();
        cursor.executescript(schema)

    def insertproject(self, name):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO projects (name) VALUES (?)', (name,))
        self.connection.commit()
        c.close()

    def insertcameraconfiguration(self, name, project)

def createDatabase():
    database = Database()
    return database
