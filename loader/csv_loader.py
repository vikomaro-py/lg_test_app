import csv
import os
from loader.base import IDataLoader
from core.mappings import OUTPUT_ORDER


class CSVDataLoader(IDataLoader):

    def __init__(self, data, **kwargs):
        super(CSVDataLoader, self).__init__(data)

    def load(self):
        file_path = 'report.csv'
        file_exists = os.path.exists(file_path)
        with open(file_path, 'a', newline='') as report_file:
            writer = csv.DictWriter(report_file, OUTPUT_ORDER)
            if not file_exists:
                writer.writeheader()
            writer.writerows(self.data)
        print("report.csv saved!")
