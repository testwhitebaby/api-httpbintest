import requests

session = requests.sessions.Session()

class BaseApi(object):
    method = "GET"
    url = ""
    params = {}
    cookies = {}
    headers = {}
    data = {}
    json = {}

    def __init__(self):
        self.response() == None

    def set_params(self, **params):
        self.params = params
        return self

    def set_cookie(self, key, value):
        self.cookies.update({key, value})
        return self

    def set_data(self, data):
        self.data = data
        return self

    def set_json(self, json):
        self.json = json
        return self

    def run(self):
        self.response = session.request(
            self.method,
            self.url,
            params=self.params,
            cookies=self.cookies,
            headers=self.headers,
            data=self.data,
            json=self.json
        )
        return self

    def extract(self,field):
        value = self.response
        for _key in field.split("."):
            if isinstance(value, requests.Response):
                if _key == "json()":
                    value = self.response.json()
                else:
                    value = getattr(value, _key)
            elif isinstance(value, (requests.structures.CaseInsensitiveDict, dict)):
                value = value[_key]

        return value

    # jsonpath格式去返回值，支持headers,body
    def validate(self, key, expected_value):
        # value = self.response
        # for _key in key.split("."):
        #     if isinstance(value,requests.Response):
        #         if _key == "json()":
        #             value = self.response.json()
        #         else:
        #             value = getattr(value,_key)
        #     elif isinstance(value, (requests.structures.CaseInsensitiveDict,dict)):
        #         value = value[_key]
        # assert value == expected_value
        # return self
        actual_value = self.extract(key)
        assert actual_value == expected_value
        return self

    def get_response(self):
        return self.response()
