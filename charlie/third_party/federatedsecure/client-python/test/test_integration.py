import unittest

import federatedsecure.client


class TestIntegration(unittest.TestCase):

    def test_integration(self):
        api = federatedsecure.client.Api("http://localhost:55500")
        response = api.list()
        self.assertGreater(len(response), 0)
