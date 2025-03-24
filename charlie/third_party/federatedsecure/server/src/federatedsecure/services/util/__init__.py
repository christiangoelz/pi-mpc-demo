"""basic utility microservices for Federated Secure Computing"""

from federatedsecure.services.util.kvstorage import KeyValueStorage


def federatedsecure_register(registry):

    registry.register(
        {
            "namespace": "federatedsecure",
            "plugin": "Util",
            "version": "0.6.0",
            "microservice": "KeyValueStorage"
        },
        KeyValueStorage()
    )
