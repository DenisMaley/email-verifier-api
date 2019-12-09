from controller.email import EmailController
from .base_resource import BaseResource


class EmailValidation(BaseResource):
    SCHEMA_FILE = 'email_validation.json'

    def post(self):
        self.parser.add_argument('email')
        input_data = self.parser.parse_args()

        valid, data = self.validate(input_data)

        if valid:
            return EmailController.validate(data['email'])
        else:
            return {'valid': False, 'validators': data}, 400
