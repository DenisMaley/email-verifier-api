import socket
import dns.resolver


class DnsChecker:
    def __init__(self, domain):
        self.domain = domain
        self.result = {
            'valid': False,
        }

    def validate(self):
        try:
            self.get_ip()
            self.get_mx()
            self.result['valid'] = len(self.result['ip']) > 0 and len(self.result['mx']) > 0
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer) as e:
            self.result['reason'] = str(e)
        return self.result

    def get_ip(self):
        self.result['ip'] = [str(rdata) for rdata in dns.resolver.query(self.domain, 'A')]

    def get_mx(self):
        self.result['mx'] = [str(rdata.exchange) for rdata in dns.resolver.query(self.domain, 'MX')]