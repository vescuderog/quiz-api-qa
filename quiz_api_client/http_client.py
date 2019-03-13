import json
import logging

import requests


class HttpClient(object):

    def __init__(self, **kwargs):
        self.url = kwargs['url']
        self.logging = kwargs.get('logging', False)
        # Init session
        self.session = requests.Session()
        # Default headers
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        self.session.headers.update(self.headers)

    def close(self):
        # Close session
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
            print('ERROR GET: ', e)

    # Method POST
    def post(self, endpoint, payload):
        self.log(self.logging)
        try:
            data = json.dumps(payload)
            response = self.session.post(self.url + endpoint, data=data)
            print('Status: {} and headers: {}'.format(response.status_code, response.headers))
            return response
        except Exception as e:
            # TODO: Manage the exception
            print('ERROR POST: ', e)

    # Method PATCH
    def patch(self, endpoint, payload):
        self.log(self.logging)
        try:
            data = json.dumps(payload)
            response = self.session.patch(self.url + endpoint, data=data)
            print('Status: {} and response: {}'.format(response.status_code, json.dumps(response.json(), indent=4,
                                                                                        sort_keys=True)))
            return response
        except Exception as e:
            # TODO: Manage the exception
            print('ERROR PATCH: ', e)

    # Method DELETE
    def delete(self, endpoint):
        self.log(self.logging)
        try:
            response = self.session.delete(self.url + endpoint)
            print('Status: {}'.format(response.status_code))
            return response
        except Exception as e:
            # TODO: Manage the exception
            print('ERROR DELETE: ', e)

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
