"""
Simple unittests for SwiftAuth.

SwiftAuth is an Authentication class for the requests library
that makes it easier to authenticate with the swift TempAuth
"""
import unittest

import requests
from httmock import urlmatch, HTTMock

from requests_swift import SwiftAuth


@urlmatch(netloc=r'http://swift-auth:8080.*')
def auth_match(url, request):
    return 'hello!'


class TestSwiftAuth(unittest.TestCase):
    """
    Some simple tests for testing the SwiftAuth Authentication
    class for requests.
    """

    def setUp(self):
        """
        Setup some stuff
        """
        self.auth_url = 'http://swift-auth:8080/auth/v1.0'
        self.user = 'test:tester'
        self.key = 'testing'
        self.url = 'http://swift-auth:8080/v1/AUTH_test'

    def test_authentication_works(self):
        """
        Request authentication and it works
        """
        import ipdb
        ipdb.set_trace()
        with HTTMock(auth_match):
            swift_auth = SwiftAuth(self.auth_url, self.user, self.key)
            r = requests.get(self.url, auth=swift_auth)
            print r.content




# def make_request():
#     auth_url = 'http://ec2-54-253-61-165.ap-southeast-2.compute.amazonaws.com:8080/auth/v1.0'
#     user = 'test:tester'
#     key = 'testing'

#     

#     swift_auth = SwiftAuth(auth_url, user, key)

#     response = requests.get(url, auth=swift_auth)
#     print response.status_code
#     print response.content


# if __name__ == '__main__':
#     make_request()

