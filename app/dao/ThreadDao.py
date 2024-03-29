from mysql.connector import MySQLConnection

from app.db.MysqlConnector import Mysql
from app.entities import Thread
from constants.db import THREAD_TABLE


class ThreadDao:
    def __init__(self):
        self.conn: MySQLConnection = Mysql().connect()

    def create(self, thread: Thread):
        sql = "INSERT INTO {} VALUES (%s, %s, %s, %s)".format(THREAD_TABLE)
        val = (thread.id, thread.name, thread.category, thread.url)
        self.conn.cursor().execute(sql, val)

    def create_all(self, threads: []):
        for thread in threads:
            sql = "INSERT INTO {} VALUES (%s, %s, %s, %s)".format(THREAD_TABLE)
            val = (thread.id, thread.name, thread.category, thread.url)
            self.conn.cursor().execute(sql, val)

    def read(self, key: int = None):
        if key is None:
            return self._read_many()

        return self._read_one(key)

    def _read_one(self, key: int) -> Thread:
        sql = "SELECT * FROM {} WHERE id = %s".format(THREAD_TABLE)
        val = (key,)
        cursor = self.conn.cursor()
        cursor.execute(sql, val)
        return cursor.fetchone()

    def _read_many(self) -> []:
        sql = "SELECT * FROM {}".format(THREAD_TABLE)
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def update(self, thread: Thread):
        sql = "UPDATE {} SET name = %s, category = %s, url = %s WHERE id = %s".format(THREAD_TABLE)
        val = (thread.name, thread.category, thread.url, thread.id)
        self.conn.cursor().execute(sql, val)

    def delete(self, key: int):
        sql = "DELETE FROM {} WHERE id = %s".format(THREAD_TABLE)
        val = (key,)
        self.conn.cursor().execute(sql, val)

    def get_last_row(self) -> Thread:
        sql = "SELECT * FROM {} ORDER BY id DESC LIMIT 1".format(THREAD_TABLE)
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchone()
