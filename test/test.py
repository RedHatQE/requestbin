"""
test for the silly requestb.in wrapper module
"""
import requests, json
from requestbin.bin import Bin
from requestbin.request import Request

def test_01_basic_functionality():
    # create a fresh bin on default service
    bin = Bin.create()
    assert bin.request_count == 0 and bin.requests == [], 'invalid initial status'
    assert Bin.from_response(requests.get(bin.api_url)).name == bin.name, 'invalid bin name/api_url'

    # make a post request
    requests.post(bin.url, data=json.dumps({u'0': False, u'1': True}), headers={'content-type': 'application/json'})

    # assert count increased
    bin.reload()
    assert bin.request_count == 1, 'invalid requests count'

    # fetch the stored request
    request = bin.requests[0]

    assert request.method == 'POST', 'invalid request method'
    assert request.time > bin.time, 'invalid request timestamp'
    assert request.content_type == 'application/json', 'invalid content type'
    assert json.loads(request.body) == {u'0': False, u'1': True}, 'invalid body content'
    assert Request.from_response(requests.get(request.api_url), bin=bin).id == request.id, 'invalid request id/api_url'

    # requests order is maintained
    requests.post(bin.url, data=json.dumps({u'2': False, u'3': True}), headers={'content-type': 'application/json'})
    request_times = [request.time for request in bin.requests]
    assert request_times == sorted(request_times), 'order not preserved'
