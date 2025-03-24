import random
import datetime
import sys

import federatedsecure.client


SERVER_PARTY_1 = "http://127.0.0.1:55500"
SERVER_PARTY_2 = "http://127.0.0.1:55501"

SHARED_NODES = [SERVER_PARTY_1, SERVER_PARTY_2]
SHARED_UUID = "c54beb59-b780-4878-96a7-b0867dca6635"


if __name__ == "__main__":

    MY_INDEX = int(sys.argv[1])
    MY_NODE = SHARED_NODES[MY_INDEX]
    MY_NETWORK = {'nodes': SHARED_NODES,
                  'uuid': SHARED_UUID,
                  'myself': MY_INDEX}

    api = federatedsecure.client.Api(MY_NODE)
    microservice = api.create(protocol="Simon")

    for NUM_CATEGORIES in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        for NUM_RECORDS in [10, 20, 30, 40, 50, 60, 70, 80, 90,
                            100, 200, 500, 1000, 2000, 5000, 10000]:

            MY_SECRET = [(f'patient_{i}',
                          f'category_{random.randrange(NUM_CATEGORIES)}')
                         for i in range(NUM_RECORDS)]

            start_time = datetime.datetime.now()

            result = microservice.compute(
                microprotocol="StatisticsContingencyVertical",
                data=MY_SECRET,
                network=MY_NETWORK)

            stop_time = datetime.datetime.now()
            diff_time = stop_time - start_time

            print(NUM_CATEGORIES, NUM_RECORDS, str(diff_time.seconds + diff_time.microseconds * 0.000001).replace('.', ','))
            # print(api.download(result))
