from model.email import Email
from response.email_validation import EmailValidationResponse
from service.dns_checker import DnsChecker
from service.regex_checker import RegexChecker
from service.smtp_checker import SmtpChecker


class EmailController:

    def __init__(self):
        pass

    @staticmethod
    def validate(address):
        response = EmailValidationResponse(email=address)

        regex_result = RegexChecker(address).validate()
        response.validators.update({RegexChecker.NAME: regex_result})

        if regex_result.keys() >= {'local', 'domain'}:
            email = Email(regex_result['local'], regex_result['domain'])

            response.validators.update({
                DnsChecker.NAME: DnsChecker(email).verify(),
                SmtpChecker.NAME: SmtpChecker(email).verify()
            })

        validator_results = {k: v['valid'] for (k, v) in response.validators.items()}
        response.valid = all(validator_results.values())

        return response.output()
