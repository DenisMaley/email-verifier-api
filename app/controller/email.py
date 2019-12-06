from service.regex_checker import RegexChecker


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
        result_code = 200
        return result, result_code
