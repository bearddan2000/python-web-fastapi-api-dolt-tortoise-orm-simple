import requests
import testify

from const import *

def fun_call(url: str, fun):
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 
    
    return fun(url, headers=headers)

def get_count(url: str, fun_ptr):
    
    resp = fun_call(url, fun_ptr)

    return len(resp.json()['results'])

def assert_not_equal_count(url: str, fun_ptr):
    """assert that there has been something added or removed"""
    before = get_count(GET_ALL_URL, requests.get)
    after = get_count(url, fun_ptr)
    testify.assert_not_equal(before, after)
    
    return 0

def assert_equal_count(url: str, fun_ptr):
    """assert that nothing has been added or removed"""
    before = get_count(GET_ALL_URL, requests.get)
    after = get_count(url, fun_ptr)
    testify.assert_equal(before, after)
    
    return 0

def assert_changed(index: int):
    key = 'results'
    resp = fun_call(GET_ALL_URL, requests.get).json()
    testify.assert_not_equal(STATIC[key][index], resp[key][index])
    return 0

def assert_url(url: str, fun_ptr):
    """assert that endpoint is valid"""
    
    resp = fun_call(url, fun_ptr)

    testify.assert_equal(resp.status_code, 200)

    return 0

class TestGet(testify.TestCase):
    """docstring for TestGet."""

    def test_get_all_url(self):
        return assert_url(GET_ALL_URL, requests.get)
    
    def test_get_all_equal_output(self):
        return assert_equal_count(GET_ALL_URL, requests.get)
    
if __name__ == '__main__':
    testify.run()
