from core.mappings import MAPPINGS, DEFAULT_MAPPING, DEFAULT_TRAFARET
from transformer.base import IRowTransformer, IRowsTransformer


class RowTransformer(IRowTransformer):
    """
    Class that transforms data from reader to list of dictionaries in format mentioned
    in MAPPINGS
    """
    def convert(self):
        data = self.prepare()
        mapper_config = MAPPINGS.get(self.parser, DEFAULT_MAPPING)
        trafaret = mapper_config.get('default', DEFAULT_TRAFARET)
        result = dict()
        for k in data.keys():
            if k in trafaret.keys():
                t = trafaret[k]
                column_name = t.get('name', k)
                parser = t.get('parser', lambda x: x)
                column_data = parser(data[k]).parse()
                column_value = column_data['value']
                result.update({column_name: column_value})
            else:
                result[k] = data[k]
        return result


class BankThreeRowTransformer(RowTransformer):
    def prepare(self):
        data = self.data
        euro = data.pop('euro', 0)
        cents = data.pop('cents', 0)
        data['amount'] = f"{euro}.{cents}"
        return data


class RowsTransformer(IRowsTransformer):
    parser = None
    transformer_class = RowTransformer

    def convert(self):
        result = []
        for row in self.data:
            converted_row = self.transformer_class(row, parser=self.parser)
            result.append(converted_row.convert())
        return result


class BankOneRowsTransformer(RowsTransformer):
    parser = "bank1"


class BankTwoRowsTransformer(RowsTransformer):
    parser = "bank2"


class BankThreeRowsTransformer(RowsTransformer):
    parser = "bank3"
    transformer_class = BankThreeRowTransformer
