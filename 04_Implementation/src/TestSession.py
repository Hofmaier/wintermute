import unittest
import Session

class TestSession(unittest.TestCase):
    def test_ctor(self):
        session = Session.Session()
        self.assertIsNotNone(session.projectFactory)

if __name__ == '__main__':
    unittest.main()
