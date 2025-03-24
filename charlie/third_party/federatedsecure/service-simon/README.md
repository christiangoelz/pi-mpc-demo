![license](https://img.shields.io/github/license/federatedsecure/service-simon)
![CodeQL](https://github.com/federatedsecure/service-simon/workflows/CodeQL/badge.svg)
![Pylint](https://raw.githubusercontent.com/federatedsecure/service-simon/main/.github/badges/pylint.svg)

# Installation (server-side)

`pip install federatedsecure-simon`

# Usage (client side)

`pip install federatedsecure-client`

``` python
import federatedsecure.client

api = federatedsecure.client.Api(MY_NODE)
microservice = api.create(protocol="Simon")
result = microservice.compute(microprotocol="SecureSum", data=MY_SECRET, network=MY_NETWORK)
print(api.download(result))
```
