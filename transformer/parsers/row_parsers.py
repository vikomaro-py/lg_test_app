from dateutil.parser import parse as parse_date
from transformer.parsers.base import IBaseParser


class DateColumnParser(IBaseParser):
    def parse(self):
        result = {}
        if self.name:
            result['name'] = self.name
        try:
            value = parse_date(self.value).date().strftime("%Y-%m-%d")
        except Exception:
            value = 'Bad input date'
        result['value'] = value.strip()
        return result


class ColumnParser(IBaseParser):
    def parse(self):
        result = {'value': self.value.strip()}
        if self.name:
            result['name'] = self.name
        return result

