"""
Request module
"""

from tools import pathjoin

class Request(object):
    path = 'requests'

    def __init__(self, bin=None, body={}, content_length=0, content_type='', form_data={}, headers={},
        id='', method='', path='/', query_string={}, remote_addr='', time=None, **kwargs):
        self.bin = bin
        self.body = body
        self.content_length = content_length
        self.content_type = content_type
        self.form_data = form_data
        self.headers = headers
        self.id = id
        self.method = method
        self.path = path
        self.query_string = query_string
        self.remote_addr = remote_addr
        self.time = time

    @classmethod
    def from_response(cls, response, bin=None):
        assert 200 <= response.status_code < 400, response.reason
        data = response.json()
        if type(data) == list:
            ret = list()
            for item in data:
                ret.append(cls(bin=bin, **item))
            return ret
        return cls(bin=bin, **data)

    @property
    def api_url(self):
        '''return the api url of this request'''
        return pathjoin(Request.path, self.id, url=self.bin.api_url)

# Sample request json as returned from the service:
# { "body": "{'milan': true}",
#        "content_length": 15,
#        "content_type": "Application/Json",
#        "form_data": {},
#        "headers": {
#            "Accept": "Application/Json",
#            "Connect-Time": "5",
#            "Connection": "close",
#            "Content-Length": "15",
#            "Content-Type": "Application/Json",
#            "Host": "requestb.in",
#            "Total-Route-Time": "0",
#            "User-Agent": "curl/7.37.1",
#            "Via": "1.1 vegur",
#            "X-Request-Id": "9a583fee-c06c-4c02-9cb7-a5082857e643"
#        },
#        "id": "x4ol9j",
#        "method": "POST",
#        "path": "/1al2j5g1",
#        "query_string": {},
#        "remote_addr": "213.175.37.10",
#        "time": 1424180647.269193
#    }
#
