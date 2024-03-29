import os
import unittest
from http import HTTPStatus

from quiz_api_client.http_client import HttpClient


class TestQuestions(unittest.TestCase):

    def setUp(self):
        url = os.getenv('API_URL', 'http://localhost:8080')
        print('API URL: ', url)
        self.rest_client = HttpClient(url=url, logging=True)
        self.questions_endpoint = '/api/quiz/v1/questions'

    def tearDown(self):
        self.rest_client.close()

    def test_get_questions_list(self):
        response = self.rest_client.get(self.questions_endpoint)
        self.assertEqual(response.status_code, HTTPStatus.OK)


if __name__ == '__main__':
    unittest.main(verbosity=2)
