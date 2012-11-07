import unittest
from astrophoto import persistence
import mock

class TestPersistenceFacade(unittest.TestCase):
    def test_ctor(self):
        persistenceFacade = persistence.PersistenceFacade()
        dbmock = mock.Mock()
        persistence.createDatabase = mock.Mock(return_value=dbmock)
        self.assertIsNotNone(persistenceFacade.database)

    def test_insertproject(self):

        dbmock = mock.MagicMock()
        projectname = 'jupiter'
        dbmock.insertproject.return_value = 'True'
        persistence.createDatabase = mock.MagicMock(return_value=dbmock)
        persistenceFacade = persistence.PersistenceFacade()
        persistenceFacade.insertproject(projectname)
        dbmock.insertproject.assert_called_with(projectname)

