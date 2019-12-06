from service.regex_checker import RegexChecker
from service.dns_checker import DnsChecker


class EmailController:

    def __init__(self):
        pass

    @staticmethod
    def validate(address):
        regex_check = RegexChecker(address).validate()
        regex_result = RegexChecker(address).result()

        result = {
            'email': address,
            'valid': regex_check,
            'validators': {
                'regex': regex_result
            }
        }

        if regex_check:
            local, domain = RegexChecker(address).parse()
            dns_result = DnsChecker(domain).result()
            result['validators']['domain'] = dns_result
        result_code = 200
        return result, result_code
