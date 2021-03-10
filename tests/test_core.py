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

class ApiHttpbinGetCookies(BaseApi):
    url = "http://httpbin.org/cookies"
    params = {}
    method = "GET"
    headers = {"accept":"application/json"}

def test_httpbin_get():
    ApiHttpbinGet().run()\
        .validate("status_code",200)\
        .validate("headers.server","gunicorn/19.9.0") \
        .validate("json().url", "http://httpbin.org/get")

def test_httpbin_setcookies():
    api_run = ApiHttpbinGetCookies()\
                .set_cookie("freeform1", "123")\
                .set_cookie("freeform2", "456")\
                .run()
    freeform1 = api_run.extract("json().cookies.freeform1")
    freeform2 = api_run.extract("json().cookies.freeform2")
    assert freeform1 == "123"
    assert freeform2 == "456"

def test_httpbin_parameters_extract():
    # 取值
    freeform = ApiHttpbinGetCookies()\
                .set_cookie("freeform","123")\
                .run()\
                .extract("json().cookies.freeform")
    assert freeform == "123"