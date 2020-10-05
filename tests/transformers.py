import os
from unittest import TestCase

from core.consts import FIXTURES_DIR
from core.mappings import OUTPUT_ORDER, MAPPINGS
from extractor.csv_reader import CSVReader
from transformer.bank import BankTwoRowsTransformer


class TransformersTestCase(TestCase):

    def setUp(self) -> None:
        super(TransformersTestCase, self).setUp()
        data_source = os.path.join(FIXTURES_DIR, 'bank2.csv')
        self.data = CSVReader(data_source).run()
        self.transformed_data = BankTwoRowsTransformer(self.data).run()
        self.mapping = MAPPINGS['bank2']['default']

    def test_rows_transformer_count(self):
        self.assertEqual(len(self.transformed_data), 2)

    def test_row_transformer_keys(self):
        for r in self.transformed_data:
            keys = sorted(list(r.keys()), key=lambda x: x)
            output_keys = sorted(list(OUTPUT_ORDER), key=lambda x: x)
            self.assertEqual(keys, output_keys)
