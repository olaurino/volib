from __future__ import print_function
from six import with_metaclass, iteritems

__author__ = 'olaurino'

__all__ = ['Enum', 'Enumeration', 'DataType', 'Attribute', 'Collection', 'Reference', 'ValueType', 'ObjectType']

import logging
from weakref import WeakKeyDictionary

logging.basicConfig()
logger = logging.getLogger(__name__)
debug = logger.debug
warning = logger.warning
error = logger.error


def get_fields(d, clazz):
    ret = {}
    for k, v in iteritems(d):
        if isinstance(v, clazz):
            ret[k] = v
    return ret


class ReferencableMeta(type):
    """
    Base metaclass for VODML Referencable types. It conveniently creates a vodml-id if one is not explicitly provided
    in the class declaration
    Examples:
>>> class MyReferencable(with_metaclass(ReferencableMeta, object)):
...     pass
...
>>> class MyClass(MyReferencable):
...     pass
...
>>> print(MyReferencable.vodml_id)
MyReferencable
>>> print(MyClass.vodml_id)
MyClass
>>> class MyOtherClass(MyReferencable):
...     vodml_id = 'myid'
...
>>> print(MyOtherClass.vodml_id)
myid
    """

    def __init__(cls, name, bases, d):
        if 'vodml_id' not in d.keys():
            cls.vodml_id = name
        type.__init__(cls, name, bases, d)


class ReferencableElement(with_metaclass(ReferencableMeta, object)):
    pass


class Role(ReferencableElement):
    pass


class Attribute(Role):
    """
    Class representing VODML Attributes. This class defines a Descriptor, so that special logic can be executing
    when the attributes are accessed. For instance, when assigning values to an Attribute the attribute can store the
    assigned value and possibly cast it according to its datatype. Also, validation can be performed on the assigned
    values.
    Examples:
>>> class MyEnum(Enumeration):
...     STAR = Enum('star')
...     GALAXY = Enum('galaxy')
...
>>> class MyClass(object):
...     attr = Attribute(MyEnum, 'utype')
...
>>> obj = MyClass()
>>> obj.attr = 'star'
>>> type(obj.attr) # doctest: +ELLIPSIS
<class '....Enum'>
>>> obj.attr.value
'star'
>>> print(obj.attr)
star
>>> del obj.attr
>>> type(obj.attr)
<type 'NoneType'>
>>> obj.attr = 'foo'
Traceback (most recent call last):
  ...
TypeError: Wrong value for Enum MyEnum. Valid values: MyEnum.STAR or "star", MyEnum.GALAXY or "galaxy"

    """

    def __init__(self, datatype, vodml_id, multiplicity=(1, 1), doc=None):
        self.datatype = datatype
        self.vodml_id = vodml_id
        self.multiplicity = multiplicity
        if doc is not None:
            self.__doc__ = doc
        else:
            self.__doc__ = datatype.description if hasattr(datatype,
                                                           "description") is None else "No description available"
        self.data = WeakKeyDictionary()

    def __get__(self, instance, _):
        if instance is None:
            return self
        debug("Getting value of %s" % (instance,))
        return self.data.get(instance, None)

    def __set__(self, instance, value):
        debug("Setting value of %s to %s" % (instance, value))
        if isinstance(value, self.datatype):
            self.data[instance] = value
        else:
            try:
                self.data[instance] = self.datatype.get_value(value)
            except AttributeError:
                try:
                    self.data[instance] = self.datatype(value)
                except:
                    error("Cannot cast value %s to datatype %s." % (value, self.datatype))

    def __delete__(self, instance):
        if instance in self.data:
            del self.data[instance]


class Collection(list):
    """
    A list of Attributes with given multiplicity.
    Examples:
>>> class Classification(Enumeration):
...     STAR = Enum('star')
...     GALAXY = Enum('galaxy')
...
>>> class QsoType(Enumeration):
...     QUASAR = Enum('quasar')
...     BLAZAR = Enum('blazar')
...
>>> l = Collection(Classification)
>>> l.append(Classification.STAR)
>>> l.append('galaxy')
>>> l.append(QsoType.QUASAR)
Traceback (most recent call last):
    ...
TypeError: Wrong value for Enum Classification. Valid values: Classification.STAR or "star", Classification.GALAXY or "galaxy"
>>> l = Collection(QsoType, multiplicity=(2,2))
>>> len(l)
2
>>> print(l)
[None, None]
>>> l[0] = QsoType.BLAZAR
>>> print(l[0])
blazar
>>> l = Collection(Classification, multiplicity=(2,2), default=(Classification.STAR, 'galaxy'))
>>> print(l[0])
star
>>> print(l[1])
galaxy
>>> len(l)
2
>>> l[0]=QsoType.QUASAR
Traceback (most recent call last):
    ...
TypeError: Wrong value for Enum Classification. Valid values: Classification.STAR or "star", Classification.GALAXY or "galaxy"
>>> l.append(Classification.STAR)
Traceback (most recent call last):
    ...
IndexError: Index out of range: this Collection has a max multiplicity of 2
>>> l = Collection(Classification, multiplicity=(0,-1), default=(Classification.STAR, Classification.GALAXY))
>>> l.append(Classification.STAR)
>>> len(l)
3
>>> l.append(QsoType.QUASAR)
Traceback (most recent call last):
    ...
TypeError: Wrong value for Enum Classification. Valid values: Classification.STAR or "star", Classification.GALAXY or "galaxy"
>>> l = Collection(Classification, multiplicity=(0,2), default=('star', 'galaxy'))
>>> l[2] = Classification.STAR
Traceback (most recent call last):
    ...
IndexError: Index out of range: this Collection has a max multiplicity of 2
>>> l = Collection(Classification, multiplicity=(0,2), default=('star', 'star', 'galaxy'))
Traceback (most recent call last):
    ...
IndexError: Too many elements in initialization iterable, this list has a max of 2 elements
>>> l = Collection(Classification, multiplicity=(-1,0), default=('star', 'star', 'galaxy'))
Traceback (most recent call last):
    ...
ValueError: Multiplicity values out of acceptable range. Min must be at least 0, Max must be at least 1 or -1 for infinite
    """

    def __init__(self, datatype, vodml_id="", multiplicity=(0, -1), default=(), doc=None):
        """
        :param datatype: the datatype of each element in the list. If values of a different datatype
        are added to the list, the code will try to cast the value to the list's declared datatype.
        :param multiplicity: a tuple (min, max), with min >= 0 and max >= 1. If max is set to -1 the list is assumed of
        unbound length.
        :param default: an initialization object to populate the list. Items in the iterable must all be castable to
        the declared datatype. If the iterable contains less than the min multiplicity, a None padding will be applied,
        i.e., a sufficient number of Nones will be appended to the list until it reaches at least the minimum number
        of elements according to the multiplicity
        :param doc: documentation string.
        :raise IndexError: if the initialization iterable has more elements than declared, the function will raise an
        IndexError.
        :raise ValueError: if the multiplicity tuple has inconsistent elements, a ValueError will be raised
        """
        if multiplicity[0] < 0 or multiplicity[1] < -1 or multiplicity[1] == 0:
            raise ValueError(
                "Multiplicity values out of acceptable range."
                " Min must be at least 0, Max must be at least 1 or -1 for infinite")
        new_iterable = []
        for elem in default:
            if not isinstance(elem, datatype):
                new_elem_value = datatype.get_value(elem)
                new_elem = Attribute(datatype, '')
                new_iterable.append(new_elem)
                new_iterable[len(new_iterable) - 1] = new_elem_value
            else:
                new_iterable.append(elem)
        self.datatype = datatype
        self.min = multiplicity[0]
        self.max = multiplicity[1]
        self.vodml_id = vodml_id
        self.__doc__ = doc
        if self.max != -1 and len(new_iterable) > self.max:
            raise IndexError(
                "Too many elements in initialization iterable, this list has a max of %s elements" % (self.max))
        if len(new_iterable) < self.min:
            while len(new_iterable) < self.min:
                new_iterable.append(None)
        super(Collection, self).__init__(new_iterable)

    def append(self, value):
        if self.max != -1 and len(self) == self.max:
            raise IndexError("Index out of range: this Collection has a max multiplicity of %s" % (self.max,))
        list.append(self, self.datatype.get_value(value))

    def __setitem__(self, index, value):
        if self.max != -1 and index >= self.max:
            raise IndexError("Index out of range: this Collection has a max multiplicity of %s" % (self.max,))
        list.__setitem__(self, index, self.datatype.get_value(value))


class Reference(Attribute):
    pass


class Type(ReferencableElement):
    pass


class ValueType(Type):
    pass


class DataType(ValueType):
    pass


class ObjectType(DataType):
    pass


class Singleton(type):
    """
    Metaclass for singleton object, i.e., objects that can be instantiated only once. Used mainly, if not only,
    by Enumerator.
    Examples:
>>> class MySingleton(with_metaclass(Singleton, object)):
...     pass
...
>>> my_instance = MySingleton()
>>> my_instance2 = MySingleton()
>>> my_instance is my_instance2
True
    """

    def __init__(cls, *args, **kwargs):
        super(Singleton, cls).__init__(*args, **kwargs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            debug("Instantiating class %s for the first time" % (cls,))
            cls._instance = super(Singleton, cls).__call__(*args)
        debug("Returning singleton instance of class %s" % cls)
        return cls._instance


class Enum(object):
    """
    Simple class for storing Enumeration values. Values can be any kind of Python objects.
    Examples:
>>> e = Enum('foo')
>>> e.value
'foo'
>>> e = Enum([1,2,3])
>>> e.value
[1, 2, 3]
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class FinalChild(type):
    """
    Metaclass for classes that can be extended only once, as for Enumeration.
    The metaclass checks for the __final_child__ flag in the class whose children must not be extended.
    Examples:
>>> class MyClass(with_metaclass(FinalChild, object)):
...     pass
...
>>> class MyChild(MyClass):
...     __final_child__ = True
...
>>> class FinalClass(MyChild):
...     pass
...
>>> class NoClass(FinalClass):
...     pass
...
Traceback (most recent call last):
    ...
TypeError: type 'FinalClass' is Final and thus it cannot be extended
    """

    def __new__(mcs, name, bases, classdict):
        for b in bases:
            for b2 in b.__bases__:
                if hasattr(b2, '__final_child__') and b2.__final_child__:
                    raise TypeError("type '{0}' is Final and thus it cannot be extended".format(b.__name__))

        return type.__new__(mcs, name, bases, dict(classdict))


class EnumerationMeta(Singleton, ReferencableMeta, FinalChild):
    """
    Metaclass for @Enumeration and its derived classes. It makes Enumeration a Singleton and its derived classes finals.
    It also generates a vodml_id from the class name if a vodml_id is not explicitly set.
    """

    def __init__(cls, name, bases, d):
        Singleton.__init__(cls, name, bases, d)
        cls._enums = get_fields(d, Enum)

        def get_value(value):
            if isinstance(value, Enum):
                if value in cls._enums.values():
                    return value
                else:
                    raise TypeError("Wrong value for Enum %s. Valid values: %s" % (name, cls.get_enums()))

            for field, enum in iteritems(cls._enums):
                if enum.value == value:
                    return enum
            else:
                raise TypeError("Wrong value for Enum %s. Valid values: %s" % (name, cls.get_enums()))

        cls.get_value = staticmethod(get_value)

        def get_enums():
            _str = ', '.join(
                ['.'.join((name, field)) + ' or "' + enum.value + '"' for field, enum in iteritems(cls._enums)])
            return _str

        cls.get_enums = staticmethod(get_enums)


class Enumeration(with_metaclass(EnumerationMeta, ValueType)):
    """
    Base class for Enumeration types. Most of the logic is in the @EnumerationMeta metaclass.
    Classes implementing Enumeration types MUST extend this class and are considered Final, i.e., they cannot
    be extended further.

    Examples:
>>> class MyEnum(Enumeration):
...     STAR = Enum('star')
...     GALAXY = Enum('galaxy')
...
>>> MyEnum.get_value('star') # doctest: +ELLIPSIS
<....Enum object at ...>
>>> MyEnum.get_enums()
'MyEnum.STAR or "star", MyEnum.GALAXY or "galaxy"'
>>> MyEnum.get_value('foo')
Traceback (most recent call last):
  ...
TypeError: Wrong value for Enum MyEnum. Valid values: MyEnum.STAR or "star", MyEnum.GALAXY or "galaxy"

    """
    __final_child__ = True
