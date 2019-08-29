import unittest

from app import Request_session as rs


class SessionTest(unittest.TestCase):

    def test_get_cookie(self):
        cookie = rs.get_cookie()
        self.assertNotEqual(cookie, None)
