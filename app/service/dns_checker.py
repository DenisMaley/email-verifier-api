import dns.resolver


class DnsChecker:
    NAME = 'domain'
    def __init__(self, email):
        self.email = email
        self.result = {
            'valid': False,
        }

    def verify(self):
        try:
            self.result['ip'] = [str(rdata) for rdata in self.get_ip_records()]
            self.result['mx'] = [str(rdata.exchange) for rdata in self.get_mx_records()]
            self.result['valid'] = len(self.result['ip']) > 0 and len(self.result['mx']) > 0
        except dns.resolver.NXDOMAIN:
            self.result['reason'] = "No such domain {}".format(self.email.domain)
        except dns.resolver.Timeout:
            self.result['reason'] = "Timed out while resolving {}. Check your internet connection".format(
                self.email.domain)
        except Exception as e:
            self.result['reason'] = str(e)

        return self.result

    def get_ip_records(self):
        return self.resolver_query('A')

    def get_mx_records(self):
        return self.resolver_query('MX')

    def resolver_query(self, param):
        return dns.resolver.query(self.email.domain, param)
