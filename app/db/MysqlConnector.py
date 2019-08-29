import mysql.connector
from mysql.connector import MySQLConnection

from constants.db import DBHOST, DBUSER, DBPASS


def restart_database():
    db = Mysql()
    db.connect("")
    db.truncate_db()


# ------------------------------------------------------------
# RESTART DATABASE
# ------------------------------------------------------------
if __name__ == '__main__':
    restart_database()


class Mysql:
    def __init__(self):
        self.connection = None

    def connect(self, database="fc_threads") -> MySQLConnection:
        self.connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            passwd=DBPASS,
            database=database
        )
        return self.connection

    def truncate_db(self) -> ():
        cursor = self.connection.cursor()
        cursor.execute("DROP DATABASE IF EXISTS fc_threads")
        cursor.execute("CREATE DATABASE fc_threads")
        cursor.execute("USE fc_threads")
        cursor.execute(
            "CREATE TABLE threads(id INTEGER PRIMARY KEY, name VARCHAR(255), category VARCHAR(255), url VARCHAR(255))")

    def disconnect(self) -> ():
        if self.connection.is_connected():
            self.connection.close()
