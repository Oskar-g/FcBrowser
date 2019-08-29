from app.dao.ThreadDao import ThreadDao
from app.db.db_decorators import auto_commit
from app.entities.Thread import Thread


class ThreadSrv:
    def __init__(self):
        self.dao = ThreadDao()

    @auto_commit
    def create(self, thread: Thread):
        print("Creating row: ", thread)
        self.dao.create(thread)

    def read(self, key: int = None):
        thread = self.dao.read(key)
        print(thread)
        return thread

    @auto_commit
    def update(self, thread: Thread):
        print("Updating row: ", thread)
        self.dao.update(thread)

    @auto_commit
    def delete(self, key: int):
        print("Deleting row ID: ", key)
        self.dao.delete(key)

    def get_last_thread(self) -> Thread:
        # print("Getting last thread")
        return self.dao.get_last_row()
