import socket
import smtplib
from .dns_checker import DnsChecker


class SmtpChecker:
    # Check https://www.greenend.org.uk/rjk/tech/smtpreplies.html#RCPT
    # for the documentation
    SUCCESS_CODE = 250

    # Address used for SMTP MAIL FROM command
    FROM = 'example@domain.com'

    def __init__(self, email):
        self.email = email
        self.result = {
            'valid': False,
        }

    def verify(self):
        try:
            code, message = self.ping_address()

            self.result['valid'] = code == self.SUCCESS_CODE
            if not self.result['valid']:
                self.result['reason'] = str(message)
        except Exception as e:
            self.result['reason'] = str(e)

        return self.result

    def ping_address(self):
        # Get local server hostname
        host = socket.gethostname()

        # SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP()
        server.set_debuglevel(0)

        # SMTP Conversation
        server.connect(self.get_first_mx_record())
        server.helo(host)
        server.mail(self.FROM)
        code, message = server.rcpt(str(self.email))
        server.quit()

        return code, message

    def get_first_mx_record(self):
        records = DnsChecker(self.email).get_mx_records()
        return str(records[0].exchange)
