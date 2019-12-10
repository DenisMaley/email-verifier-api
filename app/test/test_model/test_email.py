import unittest

from model.email import Email


class TestEmail(unittest.TestCase):
    def setUp(self):
        self.local = 'local'
        self.domain = 'domain.com'
        self.address = '{}@{}'.format(self.local, self.domain)
        self.email = Email(self.local, self.domain)

    def test_init(self):
        self.assertEqual(self.email.address, self.address)
        self.assertEqual(self.email.local, self.local)
        self.assertEqual(self.email.domain, self.domain)

    def test_repr(self):
        self.assertEqual(repr(self.email), self.address)

    def test_str(self):
        self.assertEqual(str(self.email), self.address)


if __name__ == '__main__':
    unittest.main()
