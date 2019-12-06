from service.regex_checker import RegexChecker
from service.dns_checker import DnsChecker


class EmailController:

    def __init__(self):
        pass

    @staticmethod
    def validate(address):
        regex_result = RegexChecker(address).validate()

        result = {
            'email': address,
            'valid': regex_result['valid'],
            'validators': {
                'regex': regex_result
            }
        }

        if 'domain' in regex_result:
            dns_result = DnsChecker(regex_result['domain']).validate()
            result['validators']['domain'] = dns_result
            result['valid'] = result['valid'] and dns_result['valid']

        # Todo make codes as constants
        result_code = 200
        return result, result_code
