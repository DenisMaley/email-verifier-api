import re


class RegexChecker:
    # General Email Regex (RFC 5322 Official Standard)
    # For details check http://emailregex.com/
    FORMAT = '(^(?P<local>[a-zA-Z0-9_.+-]+)@(?P<domain>[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$)'

    def __init__(self, address):
        self.address = address
        self.match = re.match(self.FORMAT, address)

    def validate(self):
        return self.match is not None

    def result(self):
        result = {
            'valid': self.validate()
        }
        return result

    def parse(self):
        if self.validate():
            return self.match.group('local'), self.match.group('domain')
