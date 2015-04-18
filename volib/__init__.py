__author__ = 'olaurino'

__all__ = ['Resolver', 'resolvers', 'resolve', 'add_resolver', 'vodml', 'get_object', 'Context', 'get_context']

import utypes

def utype_factory(utype):
    if isinstance(utype, basestring):
        utype = utypes.UTYPE(utype)
    return utype


class Resolver(object):
    def __init__(self):
        self._resolver = {}
        self.name = None
        self.version = None

    def resolve(self, utype):
        utype = utype_factory(utype)
        vodml_id = utype.vodml_id
        return self._resolver[vodml_id]


resolvers = {}

from pkg_resources import iter_entry_points

for ep in iter_entry_points(group='vodml.resolver'):
    res = ep.load()
    resolvers[(res.name, res.version)] = res


def resolve(utype, version):
    utype = utype_factory(utype)
    return resolvers[(utype.prefix, version)].resolve(utype)


def get_object(utype, version):
    utype = utype_factory(utype)
    resolver = resolvers[(utype.prefix, version)]
    full_path = resolver.resolve(utype)
    ret = __import__(resolver.root_pkg)
    components = full_path.split('.')
    for comp in components:
        ret = getattr(ret, comp)
    return ret


def add_resolver(resolver):
    resolvers[(resolver.name, resolver.version)] = resolver


class Context(object):
    def __init__(self, models):
        self.models = {model.name: model.version for model in models}

    def resolve(self, utype):
        utype = utype_factory(utype)
        name = utype.prefix
        version = self.models[name]
        return resolve(utype, version)

    def get_object(self, utype):
        utype = utype_factory(utype)
        name = utype.prefix
        version = self.models[name]
        return get_object(utype, version)


def get_context(models):
    return Context(models)