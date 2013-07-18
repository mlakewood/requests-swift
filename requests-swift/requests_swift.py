"""
Python requests Auth class for the basic authorisation scheme
for swift.
"""

from requests.auth import AuthBase
import requests


class SwiftAuth(AuthBase):
    """
    Authorises with swift and the attached the correct
    headers to the request
    """

    def __init__(self, auth_url, user, key):
        """
        Authenticate with the url using the user and key
        and save the auth token
        """
        self.auth_url = auth_url
        self.user = user
        self.key = key


    def __call__(self, r):
        """
        Add auth token to the headers and return the
        request
        """
        headers = {"X-Storage-User": self.user, "X-Storage-Pass": self.key}
        resp = requests.get(self.auth_url, headers=headers)
        if resp.status_code == 200:
            r.headers['X-Auth-Token'] = resp.headers['X-Auth-Token']
        else:
            r = resp

        return r