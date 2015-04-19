__author__ = 'olaurino'

__all__ = ['generate_code']

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

import logging
import os
import shutil
import re
import imp

import volib
from volib import vodml, vodml_ref


logging.basicConfig()
debug = logging.getLogger(__name__).debug

from jinja2 import Environment, FileSystemLoader
from networkx import DiGraph, topological_sort

_nonalpha = re.compile(r'[^0-9a-zA-Z]+')
_underscorer1 = re.compile(r'(.)([A-Z][a-z]+)')
_underscorer2 = re.compile(r'([a-z0-9])([A-Z])')


def pythonify(string):
    """
    Utility function to convert CamelCase strings to snake_case strings.
    Plus, change any non alphanumeric characters with _
    :rtype : basestring.
    :param string: string to be pythonized
    """
    alpha = _nonalpha.sub(r'_', string)
    subbed = _underscorer1.sub(r'\1_\2', alpha)
    return subbed


def alpha(string):
    return _nonalpha.sub(r'_', string)


def resolve(vodml_ref_string, meta, model):
    vodmlref = vodml_ref.VODML_REF(vodml_ref_string)
    version = meta.import_dict[vodmlref.prefix]
    ret = volib.resolve(vodmlref, version)
    if model and vodmlref.prefix == model.name:
        ret = ret.replace('%s_%s' % (pythonify(model.name), pythonify(model.version))+'.', '')
    tokens = ret.split(model.name+'.')
    if len(tokens) > 1:
        ret = tokens[1]
    return ret


def regex_replace(s, find, replace):
    return re.sub(find, replace, s)


def resolve_import(imp):
    return volib.resolvers[get_tuple(imp)].import_


__cwd = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(os.path.join(__cwd, 'templates')))
env.lstrip_blocks = True
env.trim_blocks = True

env.filters['pythonify'] = pythonify
env.filters['alpha'] = alpha
env.filters['resolve'] = resolve
env.filters['resolve_import'] = resolve_import
env.filters['regex_replace'] = regex_replace


def write_package(package, meta, basedir):
    pkg_dir = os.path.join(basedir, package.name)
    if not os.path.exists(pkg_dir):
        os.makedirs(pkg_dir)

    with open(os.path.join(pkg_dir, '__init__.py'), 'w') as f:
        template = env.get_template('package.jj')
        output = template.render(instance=package, meta=meta)
        f.write(output)

    if hasattr(package, 'package'):
        for pkg in package.package:
            write_package(pkg, meta, pkg_dir)


def write_model(model, meta, basedir):
    model_dir = os.path.join(basedir, "%s_%s" % (pythonify(model.name), pythonify(model.version)))
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    meta.import_ = model.import_
    meta.import_dict = {model.name: model.version}
    meta.resolved_imports = {}

    for imp_ in model.import_:
        meta.resolved_imports[imp_] = volib.resolvers[get_tuple(imp_)].import_
        meta.import_dict[imp_.name] = imp_.version

    aux = os.path.join(model_dir, '__aux__.py')
    with open(aux, 'w') as f:
        template = env.get_template('resolver.jj')
        output = template.render(instance=model, meta=meta)
        f.write(output)

    aux = imp.load_source('.'.join((alpha(meta.name), "%s_%s" % (alpha(model.name), alpha(model.version)), '__aux__')), aux)
    volib.add_resolver(aux.resolver)

    meta.self_import = aux.resolver.import_

    with open(os.path.join(model_dir, '__init__.py'), 'w') as f:
        template = env.get_template('model.jj')
        output = template.render(instance=model, meta=meta)
        f.write(output)

    if hasattr(model, 'package'):
        for pkg in model.package:
            write_package(pkg, meta, model_dir)


def get_tuple(model):
    return model.name, model.version


def add_model(models_graph, new_model):
    if new_model.name != 'ivoa':
        models_graph.add_node(get_tuple(new_model), {'model': new_model})
        for dep_proxy in new_model.import_:
            if dep_proxy.name != 'ivoa':
                models_graph.add_node(get_tuple(dep_proxy), {'model': dep_proxy})
                models_graph.add_edge(get_tuple(new_model), get_tuple(dep_proxy))
                dep_model = vodml.CreateFromDocument(urllib2.urlopen(dep_proxy.url).read())
                add_model(models_graph, dep_model)


def generate_code(model_urls, pkg_metadata, basedir, overwrite=True, write_deps=False):
    """
>>> import volib
>>> class MetaData(object):
...     name = 'reference'
...     version = '1.0'
>>> m = MetaData()
>>> basedir = os.path.dirname(volib.resources.__file__)
>>> os.chdir(basedir)
>>> generate_code(['file:ReferenceDM-1.0.vodml.xml',], m, 'output', write_deps=True)


    :param model_urls:
    :param pkg_metadata:
    :param basedir:
    :param overwrite:
    :return:
    """
    pkg_dir = os.path.join(basedir, pythonify(pkg_metadata.name))
    models_dir = os.path.join(pkg_dir, pythonify(pkg_metadata.name))
    if overwrite and os.path.exists(basedir):
        shutil.rmtree(basedir)
    if not os.path.exists(pkg_dir):
        os.makedirs(pkg_dir)

    models_graph = DiGraph()

    models_to_write = []

    for url in model_urls:
        model = vodml.CreateFromDocument(urllib2.urlopen(url).read())
        if model.name != 'ivoa':
            models_to_write.append(get_tuple(model))
            add_model(models_graph, model)

    models_list = topological_sort(models_graph)
    models_list.reverse()

    node_dict = dict(models_graph.nodes(data=True))

    for model in models_list:
        if write_deps or model in models_to_write and model.name != 'ivoa':
            write_model(node_dict[model]['model'], pkg_metadata, models_dir)

    with open(os.path.join(pkg_dir, 'setup.py'), 'w') as f:
        template = env.get_template('setup.jj')
        models = models_to_write if not write_deps else models_list
        output = template.render(meta=pkg_metadata, models=models)
        f.write(output)

    with open(os.path.join(models_dir, '__init__.py'), 'w'):
        pass

