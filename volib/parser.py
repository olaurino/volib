__author__ = 'Omar Laurino'

import os.path

import volib

VOTABLE = 'votable'
SINGLE = 'single'
ARRAY = 'array'
file_types = [VOTABLE,]
modes = [SINGLE, ARRAY]


def parse(file_name, file_type, instance_class, mode, limit):
    if file_type not in file_types:
        raise AttributeError("file_type {} is invalid, please choose among: {}"
                             .format(file_type, ', '.join(file_types)))

    if not os.path.isfile(file_name):
        raise IOError("Not a file: {}".format(file_name))

    if limit < -1 or limit == 0:
        raise AttributeError("limit must be > 0 or -1")

    instance_type = volib.get_object("test_resolver:source.stc.SkyCoordinate", "1.0")
    instances = [instance_type() for i in range(3)]
    return instances
    # with open(file_name) as f:
    #     print(f.read())