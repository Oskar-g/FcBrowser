import unittest
from daemon.app import Request_session as rs


class SessionTest(unittest.TestCase):

    def test_get_coockie(self):
        cookie = rs.get_cookie()
        self.assertNotEqual(cookie, None)
