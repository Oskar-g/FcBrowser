import unittest

from daemon.app.db.MysqlConnector import Mysql


class SessionTest(unittest.TestCase):

    def test_create_db(self):
        mysql = Mysql()
        mysql.connect(None)
        mysql.truncateDB()
