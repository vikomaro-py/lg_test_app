class IBaseParser:
    def __init__(self, value, name=None):
        self.value = value
        self.name = name

    def parse(self):
        return NotImplemented
