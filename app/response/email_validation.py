class EmailValidationResponse:

    def __init__(self, email=None, valid=False, validators=None, status=None):
        self.email = email
        self.valid = valid
        self.validators = {} if validators is None else validators
        self.status = status

    def output(self):
        return ({
            'email': self.email,
            'valid': self.valid,
            'validators': self.validators
        }, self.status)
