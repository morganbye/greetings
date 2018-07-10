from unittest import mock
import pytest
from hypothesis import given, strategies as st
import greetings.views


def test__create_token():

    result = greetings.views._create_token()

    assert len(result) == 40
    assert isinstance(result, str)


def mocked_requests_get(*args, **kwargs):

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.token = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://someurl.com/test.json':
        return MockResponse({"key1": "value1"}, 200)
    elif args[0] == 'http://someotherurl.com/anothertest.json':
        return MockResponse({"key2": "value2"}, 200)

    return MockResponse(None, 404)

@mock.patch('requests.get', side_effect=mocked_requests_get)
def test_get_hello(requests):

    result = greetings.views.get_hello(requests)
    assert result == "Hello World!"

