__author__ = 'Omar Laurino'

from unittest import TestCase
from volib import Resolver as BaseResolver
from volib.model import DataType, Attribute, Reference
from volib.astro import ivoa_1_0
from volib.parser import parse

import volib
import mock
from mock import mock_open

from sys import version_info

if version_info.major == 2:
    import __builtin__ as builtins
else:
    import builtins

xml_catalog ="""
<?xml version="1.0"?>
<VOTABLE version="1.3_vodml"
         xmlns="http://www.ivoa.net/xml/VOTable/v1.4b">
    <!-- VODML PREAMBLE. MUST BE DIRECT CHILD OF VOTABLE -->
    <!-- NOTE: VO-DML UTYPES (vo-dml:*) ONLY PERTAIN TO SERIALIZATION, NOT TO MODEL DEFINITION -->
    <GROUP>
        <VODML>
            <TYPE>vodml:Model</TYPE>
        </VODML>
        <PARAM value="ref" datatype="char" arraysize="*" name="name">
            <VODML>
                <ROLE>vodml:Model.name</ROLE>
            </VODML>
        </PARAM>
        <PARAM value="1.0" datatype="char" arraysize="*" name="version">
            <VODML>
                <ROLE>vodml:Model.version</ROLE>
            </VODML>
        </PARAM>
        <PARAM value="file:ReferenceDM-1.0.vodml.xml" datatype="char" arraysize="*" name="url">
            <VODML>
                <ROLE>vodml:Model.url</ROLE>
            </VODML>
        </PARAM>
    </GROUP>

    <PARAM ID="J2000" value="J2000" datatype="char" arraysize="*" name="j2000"/>

    <RESOURCE>
        <!-- DataType to GROUP in RESOURCE -->
        <GROUP ID="_icrs">
            <VODML>
                <ROLE>vodml:Instance.root</ROLE>
                <TYPE>ref:source.stc.SkyCoordinateFrame</TYPE>
            </VODML>
            <!-- Attribute to PARAM -->
            <PARAM value="ICRS" datatype="char" arraysize="*"
                   name="name">
                <VODML>
                    <ROLE>ref:source.stc.SkyCoordinateFrame.name</ROLE>
                </VODML>
            </PARAM>
            <!-- Attribute to PARAMref -->
            <PARAMref ref="J2000">
                <VODML>
                    <ROLE>ref:source.stc.SkyCoordinateFrame.equinox</ROLE>
                </VODML>
            </PARAMref>
        </GROUP>

        <!-- DataType to GROUP in RESOURCE -->
        <GROUP>
            <VODML>
                <ROLE>vodml:Instance.root</ROLE>
                <TYPE>ref:source.stc.SkyCoordinate</TYPE>
            </VODML>

            <PARAM name="ra" utype="" value="123.00000" datatype="float">
                <VODML>
                    <ROLE>ref:source.stc.SkyCoordinate.longitude</ROLE>
                </VODML>
            </PARAM>

            <PARAM name="dec" value="-2.10000" datatype="float">
                <VODML>
                    <ROLE>ref:source.stc.SkyCoordinate.latitude</ROLE>
                </VODML>
            </PARAM>

            <!-- Attribute to GROUPref -->
            <GROUP ref="_icrs">
                <VODML>
                    <ROLE>ref:source.stc.SkyCoordinate.frame</ROLE>
                </VODML>
            </GROUP>
        </GROUP>

        <!-- ObjectType to GROUP in RESOURCE -->
        <!-- Collection (Composition) Container -->
        <GROUP utype="vo-dml:Instance.root">
            <VODML>
                <ROLE>vodml:Instance.root</ROLE>
                <TYPE>ref:Catalog</TYPE>
            </VODML>

            <PARAM value="My Catalog" datatype="char" arraysize="*" name="name">
                <VODML>
                    <ROLE>ref:Catalog.name</ROLE>
                </VODML>
            </PARAM>

            <PARAM value="My Description" datatype="char" arraysize="*" name="description">
                <VODML>
                    <ROLE>ref:Catalog.description</ROLE>
                </VODML>
            </PARAM>

            <GROUP ID="CATALOG">
                <VODML>
                    <ROLE>ref:Catalog.sources</ROLE>
                    <TYPE>vodml:Collection</TYPE>
                </VODML>
            </GROUP>
        </GROUP>

        <GROUP ID="_error">
            <PARAM utype="vo-dml:Instance.type" value="ref:source.stc.CircleError" datatype="char" arraysize="*"
                   name="type"/>
            <!-- Inheritance, although for extensions in the same model parent might be omitted -->
            <PARAM utype="vo-dml:Instance.type" value="ref:source.stc.SkyError" datatype="char" arraysize="*"
                   name="type"/>
            <FIELDref ref="_error_radius" utype="ref:source.stc.CircleError.radius"/>
        </GROUP>

        <TABLE>
            <GROUP ID="SOURCE">
                <VODML>
                    <ROLE>vodml:Collection.item</ROLE>
                    <TYPE>ref:source.Source</TYPE>
                </VODML>

                <GROUP ref="CATALOG">
                    <VODML>
                        <ROLE>vodml:Collection.parent</ROLE>
                    </VODML>
                </GROUP>

                <FIELDref ref="_designation">
                    <VODML>
                        <ROLE>ref:source.Source.name</ROLE>
                    </VODML>
                </FIELDref>

                <!-- Attribute to GROUP in GROUP -->
                <GROUP>
                    <VODML>
                        <ROLE>ref:source.Source.position</ROLE>
                        <TYPE>ref:source.stc.SkyCoordinate</TYPE>
                    </VODML>

                    <FIELDref ref="_ra">
                        <VODML>
                            <ROLE>ref:source.stc.SkyCoordinate.longitude</ROLE>
                        </VODML>
                    </FIELDref>

                    <FIELDref ref="_dec">
                        <VODML>
                            <ROLE>ref:source.stc.SkyCoordinate.latitude</ROLE>
                        </VODML>
                    </FIELDref>

                    <GROUP ref="_icrs" utype="">
                        <VODML>
                            <ROLE>ref:source.stc.SkyCoordinate.frame</ROLE>
                        </VODML>
                    </GROUP>

                    <!-- Reference to ObjectType -->
                    <GROUP ref="_error">
                        <VODML>
                            <ROLE>ref:source.stc.SkyCoordinate.error</ROLE>
                        </VODML>
                    </GROUP>
                </GROUP>
            </GROUP>
            <FIELD ID="_designation" datatype="char" name="name" arraysize="*"/>
            <FIELD ID="_ra" datatype="float" name="ra"/>
            <FIELD ID="_dec" datatype="float" name="dec"/>
            <FIELD ID="_error_radius" datatype="float" arraysize="*" name="radius"/>
            <DATA>
                <TABLEDATA>
                    <TR>
                        <TD>SOURCE_1</TD>
                        <TD>1.0</TD>
                        <TD>1.1</TD>
                        <TD>0.1</TD>
                    </TR>
                    <TR>
                        <TD>SOURCE_2</TD>
                        <TD>2.0</TD>
                        <TD>2.1</TD>
                        <TD>0.2</TD>
                    </TR>
                    <TR>
                        <TD>SOURCE_3</TD>
                        <TD>3.0</TD>
                        <TD>3.1</TD>
                        <TD>0.3</TD>
                    </TR>
                </TABLEDATA>
            </DATA>
        </TABLE>
    </RESOURCE>
</VOTABLE>
"""


class SkyError(DataType):
    vodml_id = 'source.stc.SkyError'


class CircleError(SkyError):
    vodml_id = 'source.stc.CircleError'

    radius = Attribute(ivoa_1_0.real,
                       'source.stc.CircleError.radius',
                       doc="""TODO : Missing description : please, update your UML model asap.""")


class SkyCoordinateFrame(DataType):
    vodml_id = 'source.stc.SkyCoordinateFrame'

    name = Attribute(ivoa_1_0.string,
                     'source.stc.SkyCoordinateFrame.name',
                     doc="""TODO : Missing description : please, update your UML model asap.""")

    documentURI = Attribute(ivoa_1_0.anyURI,
                            'source.stc.SkyCoordinateFrame.documentURI',
                            doc="""TODO : Missing description : please, update your UML model asap.""")

    equinox = Attribute(ivoa_1_0.string,
                        'source.stc.SkyCoordinateFrame.equinox',
                        doc="""TODO : Missing description : please, update your UML model asap.""")

    system = Attribute(ivoa_1_0.string,
                       'source.stc.SkyCoordinateFrame.system',
                       doc="""TODO : Missing description : please, update your UML model asap.""")


class SkyCoordinate(DataType):
    vodml_id = 'source.stc.SkyCoordinate'

    longitude = Attribute(ivoa_1_0.RealQuantity,
                          'source.stc.SkyCoordinate.longitude',
                          doc="""The longitude part of this position in units of degrees.""")

    latitude = Attribute(ivoa_1_0.RealQuantity,
                         'source.stc.SkyCoordinate.latitude',
                         doc="""The latitude part of this position in units of degrees.""")

    frame = Attribute(SkyCoordinateFrame,
                      'source.stc.SkyCoordinate.frame',
                      doc="""TODO : Missing description : please, update your UML model asap.""")

    error = Reference(SkyError,
                      'source.stc.SkyCoordinate.error',
                      doc="""None""")


class Resolver(BaseResolver):
    def __init__(self):
        self.name = 'test_resolver'
        self.version = '1.0'
        self.root_pkg = 'volib.tests.test_parser'
        self.import_ = 'from volib.tests import test_parser'
        self._resolver = {
            'source.stc.SkyError': 'tests.test_parser.SkyError',
            'source.stc.SkyCoordinateFrame': 'tests.test_parser.SkyCoordinateFrame',
            'source.stc.SkyCoordinate': 'tests.test_parser.SkyCoordinate',
            'source.stc.CircleError': 'tests.test_parser.CircleError',
        }


class TestParser(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestParser, cls).setUpClass()
        volib.add_resolver(Resolver())

    @mock.patch('volib.parser.os.path')
    @mock.patch('{}.open'.format(builtins.__name__), mock_open(read_data=xml_catalog))
    def test_parser(self, mock_path):
        # TC 1: good call
        mock_path.isfile.return_value = True
        instances = parse(file_name='catalog_name',
                          file_type='votable',
                          instance_class=SkyCoordinate,
                          mode='single',
                          limit=-1)

        self.assertEqual(3, len(instances), "Wrong number of instances")
        self.assertIsInstance(instances[0], volib.tests.test_parser.SkyCoordinate, "Wrong class for instance, got {}".format(type(instances[0])))

        # TC 2: bad call - not a file
        mock_path.isfile.return_value = False
        self.assertRaises(IOError, parse,
                          file_name='catalog_name',
                          file_type='votable',
                          instance_class=SkyCoordinate,
                          mode='single',
                          limit=-1)

        # TC 3: bad call - not a file_type
        mock_path.isfile.return_value = True
        self.assertRaises(AttributeError, parse,
                  file_name='catalog_name',
                  file_type='xml',
                  instance_class=SkyCoordinate,
                  mode='single',
                  limit=-1)

        # TC 4: bad call - wrong mode
        self.assertRaises(AttributeError, parse,
                          file_name='catalog_name',
                          file_type='votable',
                          instance_class=SkyCoordinate,
                          mode='foo',
                          limit=-2)

        # TC 5: bad call - wrong limit