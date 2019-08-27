import unittest

from daemon.app.db.MysqlConnector import Mysql


class SessionTest(unittest.TestCase):

    @staticmethod
    def test_create_db():
        mysql = Mysql()
        mysql.connect(None)
        mysql.truncateDB()
