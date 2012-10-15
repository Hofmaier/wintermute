import unittest
import astro
import mock

class TestSession(unittest.TestCase):
    def test_ctor(self):
        session = astro.Session()
        self.assertIsNotNone(session.projectFactory)

    def test_createProject(self):
        projectFactory = astro.ProjectFactory()
        projectFactory.createProject = mock.MagicMock(return_value=astro.Project())
        session = astro.Session(projectFactory)
        session.createProject('testname')
        projectFactory.createProject.assert_called_with('testname')
            

if __name__ == '__main__':
    unittest.main()
