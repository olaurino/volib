"""
Created on Dec 18, 2013

@author: olaurino
"""
from datetime import timedelta, datetime
from decimal import Decimal
from fractions import Fraction

from furl import furl

from volib import Resolver
from volib.model import *


model = ('ivoa', '1.0')

__all__ = ['AtomicValue']


class anyURI(furl):
    vodml_id = 'anyURI'


class duration(timedelta):
    vodml_id = 'duration'


class decimal(Decimal):
    vodml_id = 'decimal'


class real(float):
    vodml_id = 'real'


class nonnegativeInteger(int):
    vodml_id = 'nonnegativeInteger'


class rational(Fraction):
    vodml_id = 'rational'


class datetime(datetime):
    vodml_id = 'datetime'


class string(str):
    vodml_id = 'string'


class integer(int):
    vodml_id = 'integer'


boolean = bool


class AtomicValue(DataType):
    vodml_id = 'quantity.AtomicValue'
    ucd = Attribute(string, 'quantity.AtomicValue.ucd')

    def __init__(self, value=None):
        if value is not None:
            self.value = self.__class__.value.datatype(value)


class BooleanValue(AtomicValue):
    vodml_id = 'quantity.BooleanValue'
    value = Attribute(boolean, 'quantity.BooleanValue.value')


class StringValue(AtomicValue):
    vodml_id = 'quantity.StringValue'
    value = Attribute(string, 'quantity.StringValue.value')


class Quantity(AtomicValue):
    vodml_id = 'quantity.Quantity'
    unit = Attribute(string, 'quantity.Quantity.unit')

    def __init__(self, value=None, unit=None):
        AtomicValue.__init__(self, value)
        self.unit = unit


class IntegerQuantity(Quantity):
    vodml_id = 'quantity.IntegerQuantity'
    value = Attribute(integer, 'quantity.IntegerQuantity.value')


class RealQuantity(Quantity):
    vodml_id = 'quantity.RealQuantity'
    value = Attribute(real, 'quantity.RealQuantity.value')


class Resolver(Resolver):

    def __init__(self):
        self.name = 'ivoa'
        self.version = '1.0'
        self.import_ = 'from volib.astro import ivoa_1_0'
        self._resolver = {
            'Identity': 'ivoa_1_0.Identity',
            'quantity.AtomicValue': 'ivoa_1_0.AtomicValue',
            'quantity.BooleanValue': 'ivoa_1_0.BooleanValue',
            'quantity.IntegerQuantity': 'ivoa_1_0.IntegerQuantity',
            'quantity.Quantity': 'ivoa_1_0.Quantity',
            'quantity.RealQuantity': 'ivoa_1_0.RealQuantity',
            'quantity.StringValue': 'ivoa_1_0.StringValue',
            'boolean' : 'ivoa_1_0.boolean',
            'integer' : 'ivoa_1_0.integer',
            'string' : 'ivoa_1_0.string',
            'datetime' : 'ivoa_1_0.datetime',
            'rational' : 'ivoa_1_0.rational',
            'nonnegativeInteger' : 'ivoa_1_0.nonnegativeInteger',
            'real' : 'ivoa_1_0.real',
            'decimal' : 'ivoa_1_0.decimal',
            'duration' : 'ivoa_1_0.duration',
            'anyURI' : 'ivoa_1_0.anyURI',
        }

resolver = Resolver()