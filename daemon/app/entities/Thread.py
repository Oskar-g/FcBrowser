class Thread:
    def __init__(self, key: int = None, name: str = None, category: str = None, url: str = None):
        self.id: int = key
        self.name: str = name
        self.category: str = category
        self.url: str = url

    def __str__(self):
        return """Thread : 
            id: {}, 
            name: {}, 
            category: {}, 
            url: {} """.format(self.id, self.name, self.category, self.url)
