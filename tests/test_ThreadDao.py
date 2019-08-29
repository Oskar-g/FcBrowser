import unittest

from app.dao.ThreadDao import ThreadDao
from app.entities.Thread import Thread

dao: ThreadDao = ThreadDao()


class SessionTest(unittest.TestCase):

    def test_create_row(self):
        dao.conn.rollback()
        thread = Thread(key=1, name="PoVale", category="Normal", url="Yolo")
        dao.create(thread)

    def test_create_many_row(self):
        dao.conn.rollback()
        threads = [
            Thread(key=1, name="PoVale", category="Normal", url="Yolo"),
            Thread(key=2, name="otro", category="Normal", url="SiSiSi"),
        ]
        dao.create_all(threads)

    def test_read_all_row(self):
        dao.conn.rollback()
        self.test_create_many_row()
        threads = dao.read()
        print(threads)
        dao.conn.rollback()

    def test_read_one(self):
        dao.conn.rollback()
        self.test_create_many_row()
        thread = dao.read(1)
        print(thread)
        dao.conn.rollback()

    def test_delete(self):
        dao.conn.rollback()
        self.test_create_many_row()
        print(dao.read(1))
        dao.delete(1)
        print(dao.read(1))

    def test_read_last_row(self):
        dao.conn.rollback()
        self.test_create_many_row()
        thread = dao.get_last_row()
        print(thread)
