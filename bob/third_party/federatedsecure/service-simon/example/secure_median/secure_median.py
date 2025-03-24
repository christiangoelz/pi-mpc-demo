"""
1. start three servers (set URLs accordingly below)
2. then run this script three times with arguments 0, 1, and 2 as well as the input data as list respectively:
e.g.: python3 secure_median.py 0 [0,2,9,3] 
"""

import sys
import federatedsecure.client
import json 

URL_ALICE = "http://127.0.0.1:55500"  # URL of Alice's server, needs to be running
URL_BOB = "http://127.0.0.1:55501"  # URL of Bob's server, needs to be running
URL_CHARLIE = "http://127.0.0.1:55502"  # URL of Charlie's server, needs to be running

SHARED_NODES = [URL_ALICE, URL_BOB, URL_CHARLIE]  # servers in the network are known to all
SHARED_UUID = "387a7282-c380-44c9-aede-08da7e931931"  # UUID specific to private virtual network, known to all

if __name__ == "__main__":

    MY_INDEX = int(sys.argv[1])  # 0 for Alice, 1 for Bob, 2 for Charlie
    MY_NODE = SHARED_NODES[MY_INDEX]
    MY_NETWORK = {'nodes': SHARED_NODES, 'uuid': SHARED_UUID, 'myself': MY_INDEX}
    MY_SECRET = json.loads(sys.argv[2])  # my secret input
    api = federatedsecure.client.Api(MY_NODE)
    microservice = api.create(protocol="Simon")
    result = microservice.compute(microprotocol="SecureMedian", data=MY_SECRET, network=MY_NETWORK)
    print(api.download(result))
    