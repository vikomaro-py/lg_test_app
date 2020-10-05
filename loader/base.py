class IDataLoader:
    def __init__(self, data):
        self.data = data

    def load(self):
        return NotImplemented

    def run(self):
        return self.load()
