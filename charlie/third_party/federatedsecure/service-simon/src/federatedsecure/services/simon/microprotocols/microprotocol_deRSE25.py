from federatedsecure.services.simon.caches.cache \
    import Cache
from federatedsecure.services.simon.caches.accumulative \
    import CacheAccumulative
from federatedsecure.services.simon.caches.additive \
    import CacheAdditive
from federatedsecure.services.simon.microprotocols.microprotocol \
    import Microprotocol


class MicroprotocolShareSecrets(Microprotocol):

    def __init__(self, microservice, properties, myself):
        super().__init__(microservice, properties, myself)

        self.n = self.network.count

        self.register_cache('input',
                            Cache())
        self.register_cache('secrets',
                            CacheAccumulative(minimum=self.n))      

        self.register_stage(0,
                            ['input'],
                            self.stage_0)
        self.register_stage(1,
                            ['secrets'],
                            self.stage_1)

    def stage_0(self, args):
        self.network.broadcast(args['input'],'secrets')
        return 1, None

    def stage_1(self, args):
        return -1, {'secrets': args['secrets'],
                    }