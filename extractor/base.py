class IBaseReader:
    """
    Interface for input data readers.
    Requires source.
    """
    def __init__(self, source):
        self.source = source

    def read(self):
        return NotImplemented

    def parse(self):
        return NotImplemented

    def run(self):
        return self.parse()
