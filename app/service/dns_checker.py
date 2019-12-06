import socket
import dns.resolver

class DnsChecker:
    def __init__(self, domain):
        self.domain = domain

    def validate(self):
        return len(self.getIP()) > 0

    def getIP(self):
        return [str(rdata) for rdata in dns.resolver.query(self.domain, 'A')]

    def result(self):
        result = {
            'domain': self.domain,
            'valid': self.validate(),
            'ip': self.getIP()
        }
        return result