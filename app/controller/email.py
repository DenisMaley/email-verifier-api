from service.regex_checker import RegexChecker
from service.dns_checker import DnsChecker
from service.smtp_checker import SmtpChecker
from model.email import Email


class EmailController:

    def __init__(self):
        pass

    @staticmethod
    def validate(address):
        regex_result = RegexChecker(address).validate()

        result = {
            'email': address,
            'valid': False,
            'validators': {
                'regex': regex_result
            }
        }

        if regex_result.keys() >= {'local', 'domain'}:
            email = Email(regex_result['local'], regex_result['domain'])

            result['validators']['domain'] = DnsChecker(email).verify()
            result['validators']['smtp'] = SmtpChecker(email).verify()

        validator_results = {k: v['valid'] for (k, v) in result['validators'].items()}
        result['valid'] = all(validator_results.values())

        # Todo make codes as constants
        result_code = 200
        return result, result_code
