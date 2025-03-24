from federatedsecure.server.bus import Bus


"""
Provides a special interface that creates a local 
microservices bus and routes API requests to it
"""


class TestInterface:

    def __init__(self):
        self.bus = Bus()

    def post(self, *path, body=None):
        """
        route POST /representations to create a microservice
        """
        if len(path) == 1:
            if path[0] == 'representations':
                response = self.bus.create_representation(body)
                return {'type': 'uuid', 'uuid': response}, 200
        raise RuntimeError()

    def put(self, *path, body=None):
        """
        route PUT /representations to store some data
        """
        if len(path) == 1:
            if path[0] == 'representations':
                response = self.bus.upload_representation(body)
                return {'type': 'uuid', 'uuid': response}, 200
        raise RuntimeError()

    def patch(self, *path, body=None):
        """
        route PATCH /representation/{uuid} to call some member function
        """
        if len(path) == 2:
            if path[0] == 'representation':
                response = self.bus.call_representation(path[1], body)
                if response is None:
                    return {'type': 'none'}, 200
                return {'type': 'uuid', 'uuid': response}, 200
        raise RuntimeError()

    def get(self, *path):
        """
        route GET to various endpoints
        """
        if len(path) == 1:
            if path[0] == 'representations':
                response = self.bus.list_representations()
                return {'type': 'list', 'list': response}, 200
        if len(path) == 2:
            if path[0] == 'representation':
                response = self.bus.download_representation(path[1])
                return {'type': 'object', 'object': response}, 200
        if len(path) == 3:
            if path[0] == 'representation':
                uuid = self.bus.create_attribute(path[1], path[2], public=True)
                return {'type': 'uuid', 'uuid': uuid}, 200
        raise RuntimeError()

    def delete(self, *path):
        """
        route DELETE /representation/{uuid} to release some stored handle
        """
        if len(path) == 2:
            if path[0] == 'representation':
                self.bus.release_representation(path[1])
                return {'type': 'none'}, 200
        raise RuntimeError()
