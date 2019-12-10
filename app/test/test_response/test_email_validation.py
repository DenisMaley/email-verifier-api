import unittest
from http import HTTPStatus

from response.email_validation import EmailValidationResponse


class TestEmailValidationResponse(unittest.TestCase):
    def setUp(self):
        self.email = 'local@domaim.com'
        self.valid = True
        self.validators = {
            'checker_1': {
                'valid': True,
                'details': {
                    'foo': 'bar'
                }
            },
            'checker_2': {
                'valid': False,
                'reason': 'Lorem ipsum'
            }
        }
        self.status = HTTPStatus.BAD_REQUEST
        self.response = EmailValidationResponse(self.email, self.valid, self.validators, self.status)

    def test_init_default(self):
        self.response = EmailValidationResponse()
        self.assertIsNone(self.response.email)
        self.assertFalse(self.response.valid)
        self.assertDictEqual(self.response.validators, {})
        self.assertEqual(self.response.status, HTTPStatus.OK)

    def test_init(self):
        self.assertEqual(self.response.email, self.email)
        self.assertEqual(self.response.valid, self.valid)
        self.assertDictEqual(self.response.validators, self.validators)
        self.assertEqual(self.response.status, self.status)

    def test_output(self):
        expected_output = ({
            'email': self.email,
            'valid': self.valid,
            'validators': self.validators
        }, self.status)
        self.assertTupleEqual(self.response.output(), expected_output)


if __name__ == '__main__':
    unittest.main()
