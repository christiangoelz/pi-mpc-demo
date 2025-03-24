from api import TestApi
from assertions import TestAssertions
from interface import TestInterface


"""
Tests the built-in microservice KeyValueStorage
"""


class TestKeyValueStorage(TestAssertions):

    """
    Tests the built-in microservice KeyValueStorage
    """

    def test_key_value_storage(self):

        """
        Tests the built-in microservice KeyValueStorage
        """

        interface = TestInterface()
        api = TestApi(interface=interface)

        microservice = api.create(microservice='KeyValueStorage')
        kvstorage = microservice.create(storage='TestStorage')
        kvstorage.store(key='meaning', value=42)
        value = api.download(kvstorage.retrieve('meaning'))
        self.assertEqual(value, 42)
