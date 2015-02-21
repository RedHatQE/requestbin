"""
The requestbin wrapper module
"""

import requests
from tools import pathjoin
from request import Request
from service import Service
from service import ServiceRequest as SRequest
import time

class Bin(object):
    """ the request bin object """
    path = 'api/v1/bins'

    def __init__(self, color=list(), name=None, private=False, request_count=0, service=None):
        self.color = color
        self.name = name
        self.private = private
        self.request_count = request_count
        self.service = service
        self.time = time.time()

    @classmethod
    def from_response(cls, response, service=None):
        assert 200 <= response.status_code < 400, response.reason
        data = response.json()
        return cls(service=service, **data)

    @classmethod
    def create(cls, service=Service(), private=False):
        """ create a bin instance on the server """
        response = service.send(SRequest('POST', cls.path, data={'private': private}))
        return cls.from_response(response, service=service)

    @classmethod
    def get(cls, name, service=Service()):
        '''fetch given bin from the service'''
        path = pathjoin(cls.path, name)
        response = service.send(SRequest('GET', path))
        return cls.from_response(response, service=service)

    def reload(self):
        '''reload self from self.service'''
        other = type(self).get(self.name, service=self.service)
        self.request_count = other.request_count

    @property
    def url(self):
        '''return the url of this bin'''
        return pathjoin(self.name, url=self.service.url)

    @property
    def api_url(self):
        '''return the api url of self'''
        return pathjoin(Bin.path, self.name, url=self.service.url)

    @property
    def requests(self):
        '''return accumulated requests to this bin'''
        path = pathjoin(self.path, self.name, Request.path)
        response = self.service.send(SRequest('GET', path))
        # a bin behaves as a push-down store --- better to return the requests
        # in order of appearance
        return list(reversed(Request.from_response(response, bin=self)))
