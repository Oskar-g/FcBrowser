from mysql.connector import MySQLConnection

from daemon.app.dao.ThreadDao import ThreadDao
from daemon.app.db.db_decorators import auto_comit
from daemon.app.entities import Thread


class ThreadSrv:
    def __init__(self):
        self.dao = ThreadDao()

    @auto_comit
    def create(self, thread: Thread):
        print("Creating row: ", thread)
        self.dao.create(thread)

    def read(self, key: str = None):
        self.threadDao = ThreadDao()
        thread = self.dao.read(key)
        print(thread)
        return thread

    @auto_comit
    def update(self, thread: Thread):
        print("Updating row: ", thread)
        self.dao.update(thread)

    @auto_comit
    def delete(self, key: str):
        print("Deleting row ID: ", key)
        self.dao.delete(key)
