import os
import csv
from unittest import TestCase

from core.consts import FIXTURES_DIR

from extractor.csv_reader import CSVReader


class ExtractorsTestCase(TestCase):

    def setUp(self) -> None:
        super(ExtractorsTestCase, self).setUp()
        self.bank_1 = os.path.join(FIXTURES_DIR, 'bank1.csv')

    def test_csv_reader(self):
        reader = CSVReader(self.bank_1)
        self.assertTrue(hasattr(reader, 'read'))
        self.assertTrue(hasattr(reader, 'run'))
        data = reader.run()
        self.assertTrue(isinstance(data, csv.DictReader))

