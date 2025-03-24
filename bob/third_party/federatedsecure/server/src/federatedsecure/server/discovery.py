"""routines to discover services and their microservices on server startup"""

import importlib
import pkgutil

import federatedsecure.services


def discover_builtins_and_plugins(registry):
    """discover microservices and classes in federatedsecure.server.services
    and federatedsecure.server.services"""

    for namespace_package in [federatedsecure.services]:
        for _, name, _ in pkgutil.iter_modules(
                namespace_package.__path__,
                namespace_package.__name__ + "."):
            module = importlib.import_module(name)
            try:
                getattr(module, "federatedsecure_register")(registry)
            except AttributeError:
                pass
