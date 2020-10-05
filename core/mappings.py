from transformer.parsers.row_parsers import DateColumnParser, ColumnParser

OUTPUT_ORDER = ["date", "type", "amount", "from", "to"]

MAPPINGS = {
    "bank1": {
        "default": {
            "timestamp": {
                "name": "date",
                "parser": DateColumnParser
            },
            "default": {
                "parser": ColumnParser
            }
        }
    },
    "bank2": {
        "default": {
            "date": {
                "parser": DateColumnParser
            },
            "transaction": {
                "name": "type",
                "parser": ColumnParser
            },
            "amounts": {
                "name": "amount",
                "parser": ColumnParser
            },
            "default": {
                "parser": ColumnParser
            }
        }
    },
    "bank3": {
        "default": {
            "date_readable": {
                "name": "date",
                "parser": DateColumnParser
            },
            "amount": {
                "parser": ColumnParser
            },
            "default": {
                "parser": ColumnParser
            }
        }
    },
    "default": {
        "default": {}
    },
}

DEFAULT_MAPPING = MAPPINGS['default']
DEFAULT_TRAFARET = DEFAULT_MAPPING['default']
