from extractor.csv_reader import CSVReader
from transformer.bank import BankOneRowsTransformer, BankTwoRowsTransformer, BankThreeRowsTransformer
from loader.csv_loader import CSVDataLoader

PIPELINES = {
    "bank1": {
        "default": {
            "extractor": CSVReader,
            "transformer": BankOneRowsTransformer,
            "loader": CSVDataLoader,
        }
    },
    "bank2": {
        "default": {
            "extractor": CSVReader,
            "transformer": BankTwoRowsTransformer,
            "loader": CSVDataLoader,
        }
    },
    "bank3": {
        "default": {
            "extractor": CSVReader,
            "transformer": BankThreeRowsTransformer,
            "loader": CSVDataLoader,
        }
    },
    "default": {
        "default": {
            "extractor": lambda x: x,
            "transformer": lambda x: x,
            "loader": lambda x: x,
        }
    },
}

DEFAULT_SOURCE = PIPELINES['default']
DEFAULT_PIPELINE = DEFAULT_SOURCE['default']
