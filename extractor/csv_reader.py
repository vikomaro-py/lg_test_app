import csv
import os
from extractor.base import IBaseReader


class CSVReader(IBaseReader):
    """
    csv-file source reader
    """
    def __init__(self, source):
        """
        :param source: path to csv
        """
        if not os.path.isfile(source):
            raise FileNotFoundError(f"{source} is not a file")
        super().__init__(source)

    def read(self):
        print(f'Reading {self.source}')
        return open(self.source, 'r')

    def parse(self):
        data = self.read()
        print(f'Parsing {self.source}')
        return csv.DictReader(data)
