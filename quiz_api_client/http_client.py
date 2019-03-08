import json
import logging

import requests


class HttpClient(object):

    def __init__(self, **kwargs):
        self.url = kwargs['url']
        self.logging = kwargs.get('logging', False)
        # Init session
        self.session = requests.Session()
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        self.session.headers.update(self.headers)

    def close(self):
        self.session.close()

    # Method GET
    def get(self, endpoint):
        self.log(self.logging)
        try:
            response = self.session.get(self.url + endpoint)
            print('Status: {} and response: {}'.format(response.status_code, json.dumps(response.json(), indent=4,
                                                                                        sort_keys=True)))
            return response
        except Exception as e:
            # TODO: Manage the exception
            print('ERROR: ', e)

    # Log request
    @staticmethod
    def log(should_log):
        if should_log:
            import http.client as http_client
            http_client.HTTPConnection.debuglevel = 1

            logging.basicConfig()
            logging.getLogger().setLevel(logging.DEBUG)
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True
