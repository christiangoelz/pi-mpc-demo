"""basic synchronization microservices for Federated Secure Computing"""

from federatedsecure.services.sync.barrier import Barrier
from federatedsecure.services.sync.broadcast import Broadcast


def federatedsecure_register(registry):

    registry.register(
        {
            "namespace": "federatedsecure",
            "plugin": "Sync",
            "version": "0.6.0",
            "microservice": "Barrier"
        },
        Barrier()
    )

    registry.register(
        {
            "namespace": "federatedsecure",
            "plugin": "Sync",
            "version": "0.6.0",
            "microservice": "Broadcast"
        },
        Broadcast()
    )
