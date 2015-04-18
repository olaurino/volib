# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:02:18 2013

@author: olaurino
"""

MODEL = "vo-dml:Model";
MODEL_URL = "vo-dml:Model.url";
MODEL_PREFIX = "vo-dml:Model.name";
OBJECTTYPE = "vo-dml:ObjectType";
OBJECT_ID = "vo-dml:Object.ID";
IDENTIFIER = "vo-dml:Identifier";
REFERENCE = "vo-dml:Reference";
INSTANCE_TYPE = "vo-dml:Instance.type";
TYPE_INSTANCE = "vo-dml:Type.instance";
OBJECTTYPE_INSTANCE = "vo-dml:ObjectType.instance";
DATATYPE_INSTANCE = "vo-dml:DataType.instance";
CONTAINER = "vo-dml:Object.container";


def is_model(vodml_ref):
    """
    Returns whether the argument is the utype for a vodml:Model
    """
    return MODEL == str(vodml_ref);


def vodml_ref_for(referencable_element, model):
    """
    utility method to extract the utype from a ReferencableElement
    If this is used, only this method needs to be changed if the
    identifier/utype design were to be changed.
    """
    return model.name + ":" + referencable_element.vodml_id \
        if referencable_element is not None else None


class VODML_REF(object):
    """
    class for VODML_REFs: a VODML_REF is a pointer to a vodml_id in a model definition
    and is represented by a prefix that points to a model and an id pointing
    to an element in that model by its vodml_id.
    Examples:
>>> u = VODML_REF('foo:bar')
>>> u.prefix
'foo'
>>> u.vodml_id
'bar'
>>> print u
foo:bar
>>> u = VODML_REF('bar')
>>> print u.prefix
None
>>> print u.vodml_id
bar
>>> print u
bar
>>> u = VODML_REF('foo:bar')
>>> u2 = VODML_REF('foo:bar')
>>> u == u2
True
    """

    def __init__(self, qualified_string):
        tokens = qualified_string.split(":")
        self.prefix = tokens[0] if len(tokens) > 1 else None
        self.vodml_id = tokens[1] if len(tokens) > 1 else tokens[0]

    def __str__(self):
        return self.prefix + ":" + self.vodml_id if self.prefix is not None else self.vodml_id

    def __repr__(self):
        return "VODML_REF -> " + self.__str__()

    def __eq__(self, other):
        """
        Two VODML_REFs are equal if they have the same prefix and vodml_id
        """
        return (self.prefix, self.vodml_id) == (other.prefix, other.vodml_id)

