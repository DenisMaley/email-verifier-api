class Email:

    def __init__(self, local, domain):
        self.address = '{}@{}'.format(local, domain)
        self.local = local
        self.domain = domain

    def __repr__(self):
        return self.address

    def __str__(self):
        return self.address
