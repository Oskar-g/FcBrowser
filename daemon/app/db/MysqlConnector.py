import mysql.connector
from mysql.connector import MySQLConnection

from daemon.constants.db import DBHOST, DBUSER, DBPASS


def restart_database():
    mysql = Mysql()
    mysql.connect("")
    mysql.truncateDB()


# ------------------------------------------------------------
# RESTART DATABASE
# ------------------------------------------------------------
if __name__ == '__main__':
    restart_database()

class Mysql():
    def __init__(self):
        self.connection: MySQLConnection

    def connect(self, database="fc_threads") -> MySQLConnection:
        self.connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            passwd=DBPASS,
            database=database
        )
        return self.connection

    def truncateDB(self) -> ():
        mycursor = self.connection.cursor()
        mycursor.execute("DROP DATABASE IF EXISTS fc_threads")
        mycursor.execute("CREATE DATABASE fc_threads")
        mycursor.execute("USE fc_threads")
        mycursor.execute(
            "CREATE TABLE threads(id INTEGER PRIMARY KEY, name VARCHAR(255), category VARCHAR(255), url VARCHAR(255))")

    def disconect(self) -> ():
        if self.connection.is_connected():
            self.connection.close()
