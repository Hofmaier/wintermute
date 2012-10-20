from nose.tools import *
from astrophoto import workflow
import unittest

class TestProject(unittest.TestCase):
    def test_project(self):
        project = workflow.Project('jupiter')
        self.assertEqual(project.name, 'jupiter')
