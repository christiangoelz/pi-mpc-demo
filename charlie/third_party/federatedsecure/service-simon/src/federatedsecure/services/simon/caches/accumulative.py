from federatedsecure.services.simon.caches.functional import CacheFunctional


class CacheAccumulative(CacheFunctional):
    def __init__(self, minimum=1, maximum=-1):
        super().__init__(
            function=lambda x, y: (x if isinstance(x, list) else [x]) + [y],
            minimum=minimum,
            maximum=maximum
            )