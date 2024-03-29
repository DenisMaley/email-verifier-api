import re


class RegexChecker:
    NAME = 'regex'
    # General Email Regex (RFC 5322 Official Standard)
    # For details check http://emailregex.com/
    FORMAT = '(^(?P<local>[a-zA-Z0-9_.+-]+)@(?P<domain>[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$)'
    MAIN_ERROR = 'Incorrect syntax according to RFC 5322'

    def __init__(self, address):
        self.address = address
        self.match = re.match(self.FORMAT, address)
        self.result = {
            'valid': False,
        }

    def validate(self):
        if self.match is None:
            self.result['reason'] = self.MAIN_ERROR
        else:
            self.result.update({
                'valid': True,
                'local': self.match.group('local'),
                'domain': self.match.group('domain'),
            })

        return self.result
