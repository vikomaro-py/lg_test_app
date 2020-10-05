class IRowsTransformer:
    """
    Interface that transforms sequence
    """

    def __init__(self, data, parser=None):
        self.data = data
        if parser:
            self.parser = parser

    def convert(self):
        return NotImplemented

    def run(self):
        return self.convert()


class IRowTransformer:
    """
    Interface that transforms row
    """
    def __init__(self, data, parser=None):
        """
        :param data: Iterable from extractor.base.IBaseReader subclasses run() method
        :param parser: parser name from MAPPINGS
        """
        self.data = data
        self.parser = parser or 'default'

    def prepare(self):
        """
        Prepare data before convert
        :return: Iterable same as data
        """
        return self.data

    def convert(self):
        return NotImplemented
