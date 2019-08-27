class Thread:
    def __init__(self, key: str = None, name: str = None, category: str = None, url: str = None):
        self.id: str = key
        self.name: str = name
        self.category: str = category
        self.url: str = url

    def __str__(self):
        print(self)
