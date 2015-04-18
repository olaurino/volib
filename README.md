VOLIB
=====


VOLIB is a Python implementation of the Virtual Observatory Data Modeling Language (VODML).

With VOLIB Python users can generate code that represents astronomical data model instances.
Users can instantiate Python objects and store them as VO-compliant files, or make VOLIB
read VO-compliant files and store them as Python instances.

The main goal of VOLIB and VODML is interoperability (even across domains) among data models,
data services, applications, and data serializations.

The code in this repo is currently at the prototype stage.

Install
-------

At this stage, the only way to get volib's code is through GitHub. The `develop` branch contains the latest version of
the code.


    $ git clone https://github.com/olaurino/volib.git
    $ cd volib
    $ git checkout develop 
    
The following instructions assume `conda` is available on the system's path. It should be easy to adapt these
instructions to different setups.

    $ conda create -n volibdev python=2.7 setuptools pip
    $ source activate volibdev
    
A standard `setup.py` file is provided for building and installing volib. Development mode can be activated using:

    $ python setup.py develop
    
Any missing dependencies will be downloaded automatically.
    
Note that volib registers some setuptools entry points. Libraries generated by volib also register entry points.
So, even in Development mode, if one want to unregister the entry points one needs to 'uninstall' volib or the generated
libraries:

    $ pip uninstall volib

Test
----
    
In order to run the tests, one needs `py.test` installed. The pytest-cov plugin is required to collect coverage
information:

    $ conda install pytest
    $ pip install pytest-cov
    $ python setup.py test

Coverage output is created into the `htmlcov` directory as well as sent to the terminal.    

The tests use some VODML/XML description files located in the `aux` folder to generate some code. The code will be
located in the `aux/output/reference` directory:

    $ cd aux/output/reference
    $ ls
    
This directory contains an installable Python package with the Python classes representing the Data Models described
in the reference VODML descriptions in files `ReferenceDM-1.0.vodml.xml` and `IVOA-1.0.vodml.xml` (although the
code describing the IVOA description is built-in in VOLIB, since it contains the mapping of the VODML primitive types
to Python native ones).

If installed (or Development mode is on), the `reference` package registers some `setuptools` EntryPoints that are
used by the VOLIB framework to dynamically load Python objects corresponding to specific UTYPEs.

You can test this demo package with:

    $ python setup.py develop
    
For instance, you can get the path to the class corresponding to the SkyCoordinate UTYPE in the Reference Data Model
by querying volib as follows:

    $ python
    >>> import volib
    >>> from volib import utypes
    >>> utype = utypes.UTYPE('ref:source.stc.SkyCoordinate')
    >>> volib.resolve(utype, '1.0')
    'ref_1_0.source.stc.SkyCoordinate'
    
The above code queries volib for the full path of the class representing the `SkyCoordinate` Type defined in the
Reference Data Model *version 1.0* inside the `stc` package, which is in turn a subpackage of the `source` package.

Note that different versions of the same package can be installed at the same time.

In order to get a hold on the actual Python class (or any other Python object representing the element pointed to
by a given UTYPE), you can use the `get_object` function:

    >>> volib.get_object(utype, '1.0')
    <class 'reference.ref_1_0.source.stc.SkyCoordinate'>
    
An higher level API can be used to get a `Context` that caches the values of the versions so that a client can
resolve `utypes` strings only. For example:

    >>> from collections import namedtuple
    >>> Model = namedtuple('Model', ('name', 'version'))
    >>> ref = Model('ref', '1.0')
    >>> import volib
    >>> context = volib.get_context((ref,))
    >>> context.resolve('ref:source.stc.SkyCoordinate')
    'ref_1_0.source.stc.SkyCoordinate'
    >>> context.get_object('ref:source.stc.SkyCoordinate')
    <class 'reference.ref_1_0.source.stc.SkyCoordinate'>
    
In the above simplistic example we build the `ref` object using a `namedtuple`. In practice the instance will more
likely come from file parsing or other components downstream.
    
Python API
----------

VOLIB defines classes, metaclasses, descriptors, and entry points to provide a seamless, interoperable infrastructure
for Python users and developers.

Once fully implemented, VOLIB will allow users and developers to seamlessly read and write interoperable Virtual
Observatory compliant files into and from Python classes.

A Data Model can be fully described in terms of a *Python spec*, a Python class using the definitions in `volib.model`
to declare models.

For instance, this is the Python representation of the `SkyCoordinate` object defined in the Reference Data Model:

```python

from volib.model import *
from volib.astro import ivoa_1_0

class SkyCoordinate(DataType):
    vodml_id = 'source.stc.SkyCoordinate'

    longitude = Attribute(ivoa_1_0.quantity.RealQuantity,
                        'source.stc.SkyCoordinate.longitude',
                        doc="""The longitude part of this position in units of degrees.""")
    
    latitude = Attribute(ivoa_1_0.quantity.RealQuantity,
                        'source.stc.SkyCoordinate.latitude',
                        doc="""The latitude part of this position in units of degrees.""")
    
    frame = Attribute(SkyCoordinateFrame,
                        'source.stc.SkyCoordinate.frame',
                        doc="""TODO : Missing description : please, update your UML model asap.""")
    
    error = Reference(SkyError,
                        'source.stc.SkyCoordinate.error',
                        doc="""None""")
```

This class was automatically generated by VOLIB from the VODML/XML descriptions, but it could have been created
by hand.

Note that the class extends the basic `DataType` defined in `volib.model`, representing the VODML *DataType*
definition.

Python Specs define their attributes at the class level by instantiating the classes defined in `volib.model` that
extend the *Role* type defined in VODML. These classes are used to instantiate the "attributes" of the `SkyCoordinate`
class, in this case.

VOLIB's machinery takes care of ensuring the consistency of the instances that extend `DataType`, `ObjectType`, and
`Enumeration`, including the values of their attributes.

For instance:

    >>> from reference.ref_1_0.source.stc import SkyCoordinate
    >>> coord = SkyCoordinate()
    >>> print coord.longitude
    None
    
Once instantiated, the SkyCoordinate object have attributes with no values. However, if we try to assign a value to
the attribute:
    
    >>> coord.longitude = 5
    >>> coord.longitude.value
    5.0
    
VOLIB cast the integer value we assigned to the longitude attribute in a way consistent with the attribute's datatype.
In fact:

    >>> SkyCoordinate.longitude
    <volib.model.Attribute object at 0x101220610>
    >>> SkyCoordinate.longitude.datatype
    <class 'volib.astro.ivoa_1_0.RealQuantity'>
    >>> coord.longitude
    <volib.astro.ivoa_1_0.RealQuantity object at 0x1012284d0>
    >>> SkyCoordinate.longitude
    <volib.model.Attribute object at 0x101220610>
    
Notice the difference between accessing the attribute from the class level, e.g. `SkyCoordinate.longitude` versus
`coord.longitude`. In the first case the underlying Attribute instance is exposed, while at the instance level we see
an instance of the attribute's datatype.

### Enumerations

Enumerations have a slightly different behavior, and they are designed to be used in a way that resembles JAVA
enumerations, to ensure the integrity of the instances, so that when serialized they can validate against the
interoperability standards.

Here is a snippet of code from the `reference.ref_1_0.source` module:

```python
class SourceClassification(Enumeration):
        STAR = Enum('star')
        GALAXY = Enum('galaxy')
        AGN = Enum('AGN')
        PLANET = Enum('planet')
        UNKNOWN = Enum('unknown')
        
class Source(AstroObject):
    vodml_id = 'source.Source'

    name = Attribute(ivoa_1_0.string,
                        'source.Source.name',
                        doc="""The designation of the source.""")
    
    ...
    
    classification = Attribute(SourceClassification,
                        'source.Source.classification',
                        doc="""TODO : Missing description : please, update your UML model asap.""")
```

Notice that `SourceClassification` extends the `Enumeration` class defined in `volib.model`, and that `Source`
has an attribute of datatype `SourceClassification`.

Here is an example of how these classes can be used:

    >>> from reference.ref_1_0.source import Source, SourceClassification
    >>> s = Source()
    >>> s.classification = SourceClassification.STAR
    >>> s.classification
    <volib.model.Enum object at 0x101220c10>
    >>> print s.classification
    star
    
And here is an example of how VOLIB ensures the consistency and integrity of the instances in a very Pythonic way.
also trying to dynamically cast values to the attribute's datatypes:

    >>> s.classification = 'galaxy'
    >>> s.classification
    <volib.model.Enum object at 0x101220c50>
    >>> print s.classification
    galaxy
    
    >>> s.classification = 'foo'
    Traceback (most recent call last):
        ...
    TypeError: Wrong value for Enum SourceClassification. Valid values: SourceClassification.PLANET or "planet",
        SourceClassification.AGN or "AGN", SourceClassification.STAR or "star",
        SourceClassification.GALAXY or "galaxy", SourceClassification.UNKNOWN or "unknown"

### Inheritance

VODML supports class inheritance, and so does VOLIB, thus leveraging Python's polymorphism capabilities.

Here is an a snippet from the module `reference.ref_1_0.source.stc`:

```python
class SkyError(DataType):
    vodml_id = 'source.stc.SkyError'
    
class CircleError(SkyError):
    vodml_id = 'source.stc.CircleError'

    radius = Attribute(ivoa_1_0.real,
                        'source.stc.CircleError.radius',
                        doc="""TODO : Missing description : please, update your UML model asap.""")

class GenericEllipse(SkyError):
    vodml_id = 'source.stc.GenericEllipse'

    major = Attribute(ivoa_1_0.real,
                        'GenericEllipse.major',
                        doc="""major axis of error ellipse""")
    
    minor = Attribute(ivoa_1_0.real,
                        'source.stc.GenericEllipse.minor',
                        doc="""TODO : Missing description : please, update your UML model asap.""")
    
    pa = Attribute(ivoa_1_0.real,
                        'source.stc.GenericEllipse.pa',
                        multiplicity=(0, -1),
                        doc="""Position angle of error ellipse in coordinate system of position.""")

```

The class `Source` has a `position` attribute, of type `SkyCoordinate`, which in turn has an `error` attribute of
type `SkyError`:

    >>> Source.position
    <volib.model.Attribute object at 0x101228290>
    >>> Source.position.datatype
    <class 'reference.ref_1_0.source.stc.SkyCoordinate'>
    >>> Source.position.datatype.error
    <volib.model.Reference object at 0x1012207d0>

    >>> from reference.ref_1_0.source.stc import CircleError, GenericEllipse
    >>> error = CircleError()
    >>> coord.error = error
    >>> s.position = coord
    >>> s.position.error.radius = 1
    >>> print s.position.error.radius
    1.0
    
    >>> coord.error = GenericEllipse()
    >>> coord.error.major = 0.1
    >>> coord.error.minor = 0.1
    >>> coord.error.pa = 20 
    >>> s.position.error
    <reference.ref_1_0.source.stc.GenericEllipse object at 0x101228610>
    >>> s.position.error.pa  
    20.0
    
This all works because the concrete classes extend the *abstract* `SkyError`, and `SkyCoordinate` accepts any
implementation of such class for its `error` attribute. In fact:

    >>> coord.error = Source()
    ERROR:volib.model:Cannot cast value <reference.ref_1_0.source.Source object at 0x101228550> to datatype <class 'reference.ref_1_0.source.stc.SkyError'>.

This framework enable users and developers to extend these classes so to implement their own features while enjoying
all the support of the framework itself, and in an interoperable fashion.

For instance, one can define an extension to `GenericEllipse` that adds some business logic to it, and use it in any
context a `SkyError` or a `GenericError` may be used, as shown in the simplistic code below:

    >>> class MyEllipseError(GenericEllipse):
    ...     def area(self):
    ...         import math
    ...         return math.pi*self.major*self.minor
    >>> myerror = MyEllipseError()
    >>> myerror.minor = 1.5
    >>> myerror.major = 3.1
    >>> coord.error = myerror
    >>> s.position.error.area()
    14.608405839192539