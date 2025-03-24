![license](https://img.shields.io/github/license/federatedsecure/webserver-connexion)
![CodeQL](https://github.com/federatedsecure/webserver-connexion/workflows/CodeQL/badge.svg)
![Pylint](https://raw.githubusercontent.com/federatedsecure/webserver-connexion/main/.github/badges/pylint.svg)

# installing prerequisites

```
pip install connexion[flask,uvicorn,swagger-ui]
pip install federatedsecure-server
```

# running the server

```
git clone https://github.com/federatedsecure/webserver-connexion
cd webserver-connexion/src
python __main__.py
```

any optional named parameters are passed to the uvicorn server, e.g.

```
python __main__.py port=55000
```
