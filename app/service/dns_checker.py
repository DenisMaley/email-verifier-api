class DnsChecker:
    def __init__(self, domain):
        self.domain = domain

    def validate(self):
        return True

    def result(self):
        result = {
            'valid': self.validate()
        }
        return result