"""
contains class Api
"""

from federatedsecure.client.httpsinterface import HttpsInterface
from federatedsecure.client.representation import Representation


class Api:

    """
    Api is a wrapper for the representation API endpoints
    """

    def __init__(self, url=None, interface=None):
        """connects to the Federated Secure Computin API at url or
        through some specific interface"""
        if url is not None:
            self.interface = HttpsInterface(url)
        elif interface is not None:
            self.interface = interface

    def list(self):
        """lists available top-level microservices"""
        response, _ = self.interface.get('representations')
        return response['list']

    def create(self, *args, **kwargs):
        """finds matching top-level microservice,
        and returns uuid representing the microservice"""
        response, _ = self.interface.post('representations',
                                          body={'args': args,
                                                'kwargs': kwargs})
        endpoint = Representation(self, response['uuid'])
        return endpoint

    def upload(self, *args, **kwargs):
        """uploads data and stores them on the server side,
        and returns uuid representing the data"""
        response, _ = self.interface.put('representations',
                                         body={'args': args,
                                               'kwargs': kwargs})
        endpoint = Representation(self, response['uuid'])
        return endpoint

    def call(self, representation_uuid, *args, **kwargs):
        """calls server-side function represented by uuid,
        stores the return value on the server side,
        and returns uuid representing the return value"""
        response, _ = self.interface.patch('representation',
                                           representation_uuid,
                                           body={'args': args,
                                                 'kwargs': kwargs})
        if response['type'] == 'uuid':
            endpoint = Representation(self, response['uuid'])
            return endpoint
        return None

    def download(self, representation):
        """serializes the object represented by uuid, and returns the
        serialized data"""
        response, _ = self.interface.get('representation',
                                         representation['representation_uuid'])
        return response['object']

    def release(self, representation_uuid):
        """deletes the server side object represented by uuid"""
        self.interface.delete('representation', representation_uuid)
        return None

    def attribute(self, representation_uuid, member_name):
        """gets attribute (e.g., child variable, member function) of
        object represented by uuid, stores the pointer on the server
        side, and returns uuid representing the attribute"""
        response, _ = self.interface.get('representation',
                                         representation_uuid,
                                         member_name)
        endpoint = Representation(self, response['uuid'])
        return endpoint
