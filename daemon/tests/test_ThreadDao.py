import unittest

from daemon.app.dao.ThreadDao import ThreadDao
from daemon.app.entities.Thread import Thread

dao: ThreadDao = ThreadDao()


class SessionTest(unittest.TestCase):

    def test_create_row(self):
        thread = Thread(key="1", name="PoVale", category="Normal", url="Yolo")
        dao.create(thread)

    def test_create_many_row(self):
        threads = [
            Thread(key="1", name="PoVale", category="Normal", url="Yolo"),
            Thread(key="2", name="otro", category="Normal", url="SiSiSi"),
        ]

        dao.create_all(threads)

    def test_read_all_row(self):
        self.test_create_many_row()
        threads = dao.read()
        print(threads)

    def test_read_one(self):
        self.test_create_many_row()
        thread = dao.read("1")
        print(thread)

    def test_delete(self):
        self.test_create_row()
        print(dao.read("1"))
        dao.delete("1")
        print(dao.read("1"))
