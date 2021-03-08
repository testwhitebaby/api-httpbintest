from hogwards_apitest.api import BaseApi

class ApiHttpbinGet(BaseApi):
    url = "http://httpbin.org/get"
    params = {}
    method = "GET"
    headers = {"accept":"application/json"}

class ApiHttpbinPost(BaseApi):
    url = "http://httpbin.org/post"
    params = {}
    method = "POST"
    headers = {"accept":"application/json"}
    data = "abc=123"
    json = {"abc":123}

def test_httpbin_get():
    ApiHttpbinGet().run()\
        .validate("status_code",200)