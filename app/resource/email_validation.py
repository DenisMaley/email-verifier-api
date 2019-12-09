from http import HTTPStatus

from controller.email import EmailController
from response.email_validation import EmailValidationResponse
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
            return EmailValidationResponse(validators=data, status=HTTPStatus.BAD_REQUEST).output()
