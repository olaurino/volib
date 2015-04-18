# ./vodml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:6d743b07dfdab5359eb1250ad861ef9d25bd7952
# Generated 2014-07-31 13:35:52.040291 by PyXB version 1.2.3
# Namespace http://volute.googlecode.com/dm/vo-dml/v0.9

import io

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import pyxb.utils.utility
import pyxb.utils.domutils


# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:1e06b742-18d9-11e4-9a21-406c8f48f121')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://volute.googlecode.com/dm/vo-dml/v0.9', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])


def CreateFromDocument(xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM(node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://volute.googlecode.com/dm/vo-dml/v0.9}ElementID
class ElementID(pyxb.binding.datatypes.string):
    """
          Type representing the way referenceable elements are identified uniquely in VO-DML.
          TBD We could use an xsd:NCName where ElementID is used, but that may have somewhat more sever syntax constraints than desired.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ElementID')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 65, 2)
    _Documentation = u'\n          Type representing the way referenceable elements are identified uniquely in VO-DML.\n          TBD We could use an xsd:NCName where ElementID is used, but that may have somewhat more sever syntax constraints than desired.\n      '


ElementID._CF_pattern = pyxb.binding.facets.CF_pattern()
ElementID._CF_pattern.addPattern(pattern=u'[\\w\\._-]+')
ElementID._InitializeFacetMap(ElementID._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ElementID', ElementID)

# Atomic simple type: {http://volute.googlecode.com/dm/vo-dml/v0.9}ModelPrefix
class ModelPrefix(pyxb.binding.datatypes.string):
    """
        Type used to restrict valid values for prefixes.
        TBD We could use an xsd:NCName for this.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ModelPrefix')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 84, 2)
    _Documentation = u'\n        Type used to restrict valid values for prefixes.\n        TBD We could use an xsd:NCName for this.\n      '


ModelPrefix._CF_pattern = pyxb.binding.facets.CF_pattern()
ModelPrefix._CF_pattern.addPattern(pattern=u'[\\w_-]+')
ModelPrefix._InitializeFacetMap(ModelPrefix._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ModelPrefix', ModelPrefix)

# Atomic simple type: {http://volute.googlecode.com/dm/vo-dml/v0.9}UTYPE
class UTYPE(pyxb.binding.datatypes.string):
    """
        Class representing the way ReferencableElements can be referenced in VO-DML.
        It must be possible to refer to elements in other, imported data models as well as in the current model.
        Hence the UTYPE must identify both model and element.
        The element is identified by the VO-DML ID in the model, the model is identified using a
          prefix that MUST correspond to the vodml-id element of the current or an imported model.
          Note, references to element sin the current model MUST also have a prefix, there is no default model!
        TBD We could use an xsd:QName where UTYPE is used, but that may have somewhat more sever syntax constraints than desired.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UTYPE')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 102, 2)
    _Documentation = u'\n        Class representing the way ReferencableElements can be referenced in VO-DML.\n        It must be possible to refer to elements in other, imported data models as well as in the current model.\n        Hence the UTYPE must identify both model and element.\n        The element is identified by the VO-DML ID in the model, the model is identified using a\n          prefix that MUST correspond to the vodml-id element of the current or an imported model.\n          Note, references to element sin the current model MUST also have a prefix, there is no default model!\n        TBD We could use an xsd:QName where UTYPE is used, but that may have somewhat more sever syntax constraints than desired.\n      '


UTYPE._CF_pattern = pyxb.binding.facets.CF_pattern()
UTYPE._CF_pattern.addPattern(pattern=u'[\\w_-]+:[\\w_\\-/\\./*]+')
UTYPE._InitializeFacetMap(UTYPE._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'UTYPE', UTYPE)

# Atomic simple type: [anonymous]
class STD_ANON(pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 1011, 8)
    _Documentation = None


STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.XSD = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'XSD', tag=u'XSD')
STD_ANON.Java = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'Java', tag=u'Java')
STD_ANON.OCL = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'OCL', tag=u'OCL')
STD_ANON.Custom = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'Custom', tag=u'Custom')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement with content type ELEMENT_ONLY
class ReferencableElement(pyxb.binding.basis.complexTypeDefinition):
    """
        This is the base type for all types whose elements can be explicitly referenced.
        To this end it has a 'utype' element of type UTYPE that allows explicit and unique identification of these elements.
        Generally these are also elements that can be
        represented explicitly in alternative serialisations of
        a data model, such as a VOTable or a relational model.
        These should use the value of the utype element to "point into a data model" and identify a
        model element. VO-DML itself also has needs of pointing to other elements, sometimes in another model.
        The UTYPEref type is used for such references, which will always be named .utyperef'.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReferencableElement')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 131, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element vodml-id uses Python identifier vodml_id
    __vodml_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'vodml-id'), 'vodml_id',
                                                         '__httpvolute_googlecode_comdmvo_dmlv0_9_ReferencableElement_vodml_id',
                                                         False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6), )

    vodml_id = property(__vodml_id.value, __vodml_id.set, None,
                        u'\n              Identifier for its containing element.\n              Extracted as a separate type so that we can easily adapt to a different identifier design.\n          ')


    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name',
                                                     '__httpvolute_googlecode_comdmvo_dmlv0_9_ReferencableElement_name',
                                                     False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6), )

    name = property(__name.value, __name.set, None,
                    u'\n            The name of the model element. May be restricted with uniqueness constraints in subclasses.\n          ')


    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'),
                                                            'description',
                                                            '__httpvolute_googlecode_comdmvo_dmlv0_9_ReferencableElement_description',
                                                            False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6), )

    description = property(__description.value, __description.set, None,
                           u'\n            Human readable description of the model element.\n          ')


    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id',
                                             '__httpvolute_googlecode_comdmvo_dmlv0_9_ReferencableElement_id',
                                             pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 169,
                                                            4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 169, 4)

    id = property(__id.value, __id.set, None,
                  u'\n          A referencable element may be given an @id attribute to reflect an identifier\n          defined in some source document form which a VO-DML model may have been derived.\n        ')

    _ElementMap.update({
        __vodml_id.name(): __vodml_id,
        __name.name(): __name,
        __description.name(): __description
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'ReferencableElement', ReferencableElement)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}ElementRef with content type ELEMENT_ONLY
class ElementRef(pyxb.binding.basis.complexTypeDefinition):
    """
        This type represents how to reference a ReferencableElement.
        It can serve as base class to those types that explicitly reference another type, such as relations and roles.
        It provides for a uniform way to represent the reference to
        the target element using the 'utyperef' element.
        An important design choice is that we wish to allow references to elements in remote models.
        For that reasons we can not use an ID/IDREF or key/keyref pattern.
        Instead we define various constraints on
        this type and its usage in various contexts using
        the Schematron file in vo-dml.sch.xml.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ElementRef')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 180, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element utype uses Python identifier utype
    __utype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'utype'), 'utype',
                                                      '__httpvolute_googlecode_comdmvo_dmlv0_9_ElementRef_utype', False,
                                                      pyxb.utils.utility.Location(
                                                          '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 195,
                                                          6), )

    utype = property(__utype.value, __utype.set, None,
                     u'\n            The element identifying the referenced target element.\n            See the documentation for the UTYPE type.\n          ')

    _ElementMap.update({
        __utype.name(): __utype
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ElementRef', ElementRef)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Model with content type ELEMENT_ONLY
class Model(pyxb.binding.basis.complexTypeDefinition):
    """
                Represents a complete data model and is the type of the (single) declared root element for
                VO-DML/XML representation documents.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Model')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 210, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name',
                                                     '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_name', False,
                                                     pyxb.utils.utility.Location(
                                                         '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 218,
                                                         12), )

    name = property(__name.value, __name.set, None,
                    u'\n                        Short name of the model.\n                        NOTE this name MUST be used as prefix in any utype reference to elements in this model.\n                    ')


    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'),
                                                            'description',
                                                            '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_description',
                                                            False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 226, 12), )

    description = property(__description.value, __description.set, None,
                           u'\n                        The description of the model.\n                    ')


    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'title'), 'title',
                                                      '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_title', False,
                                                      pyxb.utils.utility.Location(
                                                          '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 233,
                                                          12), )

    title = property(__title.value, __title.set, None,
                     u'\n              The title of the model by which it is officially known.\n          ')


    # Element author uses Python identifier author
    __author = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'author'), 'author',
                                                       '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_author', True,
                                                       pyxb.utils.utility.Location(
                                                           '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 240,
                                                           12), )

    author = property(__author.value, __author.set, None,
                      u'\n                    List of authors of the model, only defined by name so far.\n            TBD could be expanded with email, affiliation and so on.\n          ')


    # Element version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'version'), 'version',
                                                        '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_version', False,
                                                        pyxb.utils.utility.Location(
                                                            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 248,
                                                            6), )

    version = property(__version.value, __version.set, None,
                       u'\n            Label giving the version of the model.\n          ')


    # Element previousVersion uses Python identifier previousVersion
    __previousVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'previousVersion'),
                                                                'previousVersion',
                                                                '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_previousVersion',
                                                                False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 255, 6), )

    previousVersion = property(__previousVersion.value, __previousVersion.set, None,
                               u'\n            URI identifying a VO-DML model that is the version from which the current version of model is derived.\n            TBD could be an IVO Identifier once models get properly registered?\n          ')


    # Element lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'lastModified'),
                                                             'lastModified',
                                                             '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_lastModified',
                                                             False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 263, 6), )

    lastModified = property(__lastModified.value, __lastModified.set, None,
                            u'\n            Timestamp when the last change to the current model was made.\n          ')


    # Element import uses Python identifier import_
    __import = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'import'), 'import_',
                                                       '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_import', True,
                                                       pyxb.utils.utility.Location(
                                                           '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 270,
                                                           6), )

    import_ = property(__import.value, __import.set, None,
                       u"\n            An 'import' element indicates a dependency on an external, predefined VO-DML data model.\n            Types from that model may be used for referencing, extension and assignment to\n            attributes.\n            Types from the external model MUST NOT be used for\n            composition relationships.\n            'identification' relations to elements from that model may be used to indicate some kind of\n            equivalence between\n            elements in the current model and the external elements.\n          \n            TBD We might require that every data model MUST include a version of the IVOA data model\n            to gain access to the standard\n            primitive types and some other types.\n            We may require that that standard model should be included *completely*,\n            i.e. including all its type definitions explicitly.\n            This would be similar to treating it as a UML Profile, rather than an import.\n            This would mean that the most common type assignments for attributes\n            can be checked within the model and not require\n            importing the remote model during validation.\n          ")


    # Element package uses Python identifier package
    __package = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'package'), 'package',
                                                        '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_package', True,
                                                        pyxb.utils.utility.Location(
                                                            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 295,
                                                            12), )

    package = property(__package.value, __package.set, None,
                       u'\n                        The collection of packages which can contain further detailed name spacing to\n                        the type definitions in the model.\n                    ')


    # Element objectType uses Python identifier objectType
    __objectType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'objectType'),
                                                           'objectType',
                                                           '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_objectType',
                                                           True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 303, 12), )

    objectType = property(__objectType.value, __objectType.set, None,
                          u'\n                        Collection of ObjectType definitions directly under the model, i.e. not contained in a Package.\n                    ')


    # Element dataType uses Python identifier dataType
    __dataType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'dataType'), 'dataType',
                                                         '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_dataType', True,
                                                         pyxb.utils.utility.Location(
                                                             '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd',
                                                             310, 12), )

    dataType = property(__dataType.value, __dataType.set, None,
                        u'\n                        Collection of DataType definitions directly under the model, i.e. not contained in a Package.\n                    ')


    # Element enumeration uses Python identifier enumeration
    __enumeration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'enumeration'),
                                                            'enumeration',
                                                            '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_enumeration',
                                                            True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 317, 12), )

    enumeration = property(__enumeration.value, __enumeration.set, None,
                           u'\n                        Collection of Enumeration definitions directly under the model, i.e. not contained in a Package.\n                    ')


    # Element primitiveType uses Python identifier primitiveType
    __primitiveType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'primitiveType'),
                                                              'primitiveType',
                                                              '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_primitiveType',
                                                              True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 324, 12), )

    primitiveType = property(__primitiveType.value, __primitiveType.set, None,
                             u'\n                        Collection of PrimitiveType definitions directly under the model, i.e. not contained in a\n                        Package.\n                    ')

    _ElementMap.update({
        __name.name(): __name,
        __description.name(): __description,
        __title.name(): __title,
        __author.name(): __author,
        __version.name(): __version,
        __previousVersion.name(): __previousVersion,
        __lastModified.name(): __lastModified,
        __import.name(): __import,
        __package.name(): __package,
        __objectType.name(): __objectType,
        __dataType.name(): __dataType,
        __enumeration.name(): __enumeration,
        __primitiveType.name(): __primitiveType
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Model', Model)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}ModelProxy with content type ELEMENT_ONLY
class ModelProxy(pyxb.binding.basis.complexTypeDefinition):
    """
        A "proxy" for an external model. Represents another model that is used by the current model.
        Defines the url where the VO-DML representation of that model can be retrieved, and
        a prefix that MUST be used when making references to
        elements in that model using a UTYPEref element.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ModelProxy')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 336, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name',
                                                     '__httpvolute_googlecode_comdmvo_dmlv0_9_ModelProxy_name', False,
                                                     pyxb.utils.utility.Location(
                                                         '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 346,
                                                         8), )

    name = property(__name.value, __name.set, None,
                    u"\n                    Name by which imported model is used in the current model and its documentation.\n                    This name MUST be the same as the 'name' of the model definition in that remote document.\n                    For all utypes pointing to elements in the imported model MUST use this name as prefix.\n                ")


    # Element version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'version'), 'version',
                                                        '__httpvolute_googlecode_comdmvo_dmlv0_9_ModelProxy_version',
                                                        False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 355, 8), )

    version = property(__version.value, __version.set, None,
                       u'\n                    Version of the current model.\n                ')


    # Element ivoId uses Python identifier ivoId
    __ivoId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ivoId'), 'ivoId',
                                                      '__httpvolute_googlecode_comdmvo_dmlv0_9_ModelProxy_ivoId', False,
                                                      pyxb.utils.utility.Location(
                                                          '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 362,
                                                          8), )

    ivoId = property(__ivoId.value, __ivoId.set, None,
                     u'\n            IVO Identifier of the imported model if that exists, i.e. if that has been registered in an IVOA Registry.\n          ')


    # Element url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'url'), 'url',
                                                    '__httpvolute_googlecode_comdmvo_dmlv0_9_ModelProxy_url', False,
                                                    pyxb.utils.utility.Location(
                                                        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 369,
                                                        6), )

    url = property(__url.value, __url.set, None,
                   u'\n            URL from which the VO-DML model document can be downloaded.\n            Note, could likely be done through a registry once ivoId is known.\n            TBD SHOULD this be a generic URI, or can we insits on URL?\n          ')


    # Element documentationURL uses Python identifier documentationURL
    __documentationURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'documentationURL'),
                                                                 'documentationURL',
                                                                 '__httpvolute_googlecode_comdmvo_dmlv0_9_ModelProxy_documentationURL',
                                                                 False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 378, 6), )

    documentationURL = property(__documentationURL.value, __documentationURL.set, None,
                                u'\n            URL where a documentation HTML file for the remote model can be downloaded.\n            This SHOULD be a document that contains anchors for each element thta has as name attribute the vodml-id of that element.\n            I.e. it is assumed that the\n            vodml-id-s of the imported types can be added onto this documentationURL\n            (should end with a #?) so that a direct link to the documentation for a referenced data model element can be found.\n          ')

    _ElementMap.update({
        __name.name(): __name,
        __version.name(): __version,
        __ivoId.name(): __ivoId,
        __url.name(): __url,
        __documentationURL.name(): __documentationURL
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ModelProxy', ModelProxy)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}SKOSConcept with content type ELEMENT_ONLY
class SKOSConcept(pyxb.binding.basis.complexTypeDefinition):
    """
        Type used to indicate on attributes that they take values representing a concept defined in
        an identified SKOS vocabulary, and/or restricted by being narrower than an
        identified "broadest" concept.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SKOSConcept')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 746, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element broadestSKOSConcept uses Python identifier broadestSKOSConcept
    __broadestSKOSConcept = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'broadestSKOSConcept'), 'broadestSKOSConcept',
        '__httpvolute_googlecode_comdmvo_dmlv0_9_SKOSConcept_broadestSKOSConcept', False,
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 755, 6), )

    broadestSKOSConcept = property(__broadestSKOSConcept.value, __broadestSKOSConcept.set, None,
                                   u'\n            A URI identifiying a SKOS concept that corresponds to the concept in the model.\n            Values of a corresponding attributes must be URI-s identifiying objects that are narrower\n            than the identified concept. This attribute may be null as\n            certain vocabularies may not have a\n          ')


    # Element vocabularyURI uses Python identifier vocabularyURI
    __vocabularyURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'vocabularyURI'),
                                                              'vocabularyURI',
                                                              '__httpvolute_googlecode_comdmvo_dmlv0_9_SKOSConcept_vocabularyURI',
                                                              True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 765, 6), )

    vocabularyURI = property(__vocabularyURI.value, __vocabularyURI.set, None,
                             u'\n            If no broadestSKOSConcept is defined, one or more explicit vocabularies can be provided from which the\n            value must be obtained.\n          ')

    _ElementMap.update({
        __broadestSKOSConcept.name(): __broadestSKOSConcept,
        __vocabularyURI.name(): __vocabularyURI
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'SKOSConcept', SKOSConcept)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Multiplicity with content type ELEMENT_ONLY
class Multiplicity(pyxb.binding.basis.complexTypeDefinition):
    """
        Also called "Cardinality". Indicates how many instances of a datatype can/must be associated to a given role.
        Unless
        Follows model in XSD, i.e. with explicit lower bound and upper bound on number of instances.
        maxOccurs must be gte minOccurs, unless it is negative, in which case it corresponds to unbounded.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Multiplicity')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 864, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element minOccurs uses Python identifier minOccurs
    __minOccurs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'minOccurs'), 'minOccurs',
                                                          '__httpvolute_googlecode_comdmvo_dmlv0_9_Multiplicity_minOccurs',
                                                          False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 874, 6), )

    minOccurs = property(__minOccurs.value, __minOccurs.set, None,
                         u'\n          Lower bound on number of instances/values.\n          ')


    # Element maxOccurs uses Python identifier maxOccurs
    __maxOccurs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'maxOccurs'), 'maxOccurs',
                                                          '__httpvolute_googlecode_comdmvo_dmlv0_9_Multiplicity_maxOccurs',
                                                          False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 881, 6), )

    maxOccurs = property(__maxOccurs.value, __maxOccurs.set, None, u'\n          When negative, unbounded.\n          ')

    _ElementMap.update({
        __minOccurs.name(): __minOccurs,
        __maxOccurs.name(): __maxOccurs
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Multiplicity', Multiplicity)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Constraint with content type ELEMENT_ONLY
class Constraint(pyxb.binding.basis.complexTypeDefinition):
    """
        It is useful to be able to attach constraints to data model elements beyond the multiplicity.
        Constraints apply to instances of types or roles.
        In general these can be complex and might require a language such as OCL (=Object
        Constraint Language).
          In VO-DML constraints can be added to a Type. A special set of constraints can apply to attributes,
          the AttributeCOnstraint.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Constraint')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 892, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'expression'),
                                                           'expression',
                                                           '__httpvolute_googlecode_comdmvo_dmlv0_9_Constraint_expression',
                                                           False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 904, 12), )

    expression = property(__expression.value, __expression.set, None,
                          u'\n            An expression constraining the value to which the constraint is applied.\n            May be human readable for now, could become a regular expression, or maybe OCL expression in future.\n            To be implemented by hand in target representations of\n            the model.\n          ')

    _ElementMap.update({
        __expression.name(): __expression
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Constraint', Constraint)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}ConstraintExpression with content type ELEMENT_ONLY
class ConstraintExpression(pyxb.binding.basis.complexTypeDefinition):
    """
        Sometimes constrants are more complex than some simple limit on ranges or values supported by the various explicit choices in the Constraints type.
        Designers can define more complex expressions using the current class.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ConstraintExpression')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 994, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element expression uses Python identifier expression
    __expression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'expression'),
                                                           'expression',
                                                           '__httpvolute_googlecode_comdmvo_dmlv0_9_ConstraintExpression_expression',
                                                           False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 1002, 6), )

    expression = property(__expression.value, __expression.set, None,
                          u'\n            The expression defining the constraint. This can be in any language, one of the ones supported by the language element below,\n            or some custom language.\n          ')


    # Element language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'language'), 'language',
                                                         '__httpvolute_googlecode_comdmvo_dmlv0_9_ConstraintExpression_language',
                                                         False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 1010, 6), )

    language = property(__language.value, __language.set, None, None)

    _ElementMap.update({
        __expression.name(): __expression,
        __language.name(): __language
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ConstraintExpression', ConstraintExpression)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Package with content type ELEMENT_ONLY
class Package(ReferencableElement):
    """
                A Package is a container for type definitions and possible (child-)packages.
                Names of types only need to be unique within their container (model or package),
                hence a package provides further name-spacing for type definitions.
                When
                deriving physical representations of a model, packages may be mapped to containers in the target
                meta-model.
                For example in mapping to XSD they may give rise to separate documents with type definitions and their
                own targetNamespace. When generating
                Java classes they may be used to define seprate packages for
                the classes derived form the types.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Package')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 393, 4)
    _ElementMap = ReferencableElement._ElementMap.copy()
    _AttributeMap = ReferencableElement._AttributeMap.copy()
    # Base type is ReferencableElement

    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element objectType uses Python identifier objectType
    __objectType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'objectType'),
                                                           'objectType',
                                                           '__httpvolute_googlecode_comdmvo_dmlv0_9_Package_objectType',
                                                           True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 420, 20), )

    objectType = property(__objectType.value, __objectType.set, None,
                          u'\n                                Collection of ObjectType-s defined in this package.\n                            ')


    # Element dataType uses Python identifier dataType
    __dataType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'dataType'), 'dataType',
                                                         '__httpvolute_googlecode_comdmvo_dmlv0_9_Package_dataType',
                                                         True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 427, 20), )

    dataType = property(__dataType.value, __dataType.set, None,
                        u'\n                                Collection of DataType-s defined in this package.\n                            ')


    # Element enumeration uses Python identifier enumeration
    __enumeration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'enumeration'),
                                                            'enumeration',
                                                            '__httpvolute_googlecode_comdmvo_dmlv0_9_Package_enumeration',
                                                            True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 434, 20), )

    enumeration = property(__enumeration.value, __enumeration.set, None,
                           u'\n                                Collection of Enumeration-s defined in this package.\n                            ')


    # Element primitiveType uses Python identifier primitiveType
    __primitiveType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'primitiveType'),
                                                              'primitiveType',
                                                              '__httpvolute_googlecode_comdmvo_dmlv0_9_Package_primitiveType',
                                                              True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 441, 20), )

    primitiveType = property(__primitiveType.value, __primitiveType.set, None,
                             u'\n                                Collection of PrimitiveType-s defined in this package.\n                            ')


    # Element package uses Python identifier package
    __package = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'package'), 'package',
                                                        '__httpvolute_googlecode_comdmvo_dmlv0_9_Package_package', True,
                                                        pyxb.utils.utility.Location(
                                                            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 448,
                                                            20), )

    package = property(__package.value, __package.set, None,
                       u'\n                                Collection of child Package-s defined in this package.\n                            ')


    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement
    _ElementMap.update({
        __objectType.name(): __objectType,
        __dataType.name(): __dataType,
        __enumeration.name(): __enumeration,
        __primitiveType.name(): __primitiveType,
        __package.name(): __package
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Package', Package)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Type with content type ELEMENT_ONLY
class Type(ReferencableElement):
    """
        Base class of all type definition elements.
        All Type-s extend ReferenceableElement, i.e. they are referencable.
        Adds name, description, inheritance and indication of abstractness to ReferencableElement.
      
        Name of the type. Must be unique in the collection of all types in a given container
        (i.e. model or package)
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 462, 4)
    _ElementMap = ReferencableElement._ElementMap.copy()
    _AttributeMap = ReferencableElement._AttributeMap.copy()
    # Base type is ReferencableElement

    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element extends uses Python identifier extends
    __extends = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'extends'), 'extends',
                                                        '__httpvolute_googlecode_comdmvo_dmlv0_9_Type_extends', False,
                                                        pyxb.utils.utility.Location(
                                                            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 477,
                                                            10), )

    extends = property(__extends.value, __extends.set, None,
                       u"\n                Reference to a type (called the base-type) that is extended by the current type (called the subtype).\n                This implements the typical is-a inheritance relationship, similar to the extends relations in XSD and Java,\n                the\n                generaliation in UML, or the subclassOf relation in RDF. Note, VO-DML does not support multiple inheritance.\n                Instances of a subtype are automatic instances of a base type.\n                Polymorphism is assumed: When a role (see below) defines a base type\n                as its datatype, instances of any subtype\n                can be uased as value of the role.\n                Roles defined on a base type are inherited by the subtypes.\n                Relations inherited from a basetype can be 'subsetted', which is similar to overriding their definition.\n                See the definiton of this property on the Relation type.\n              ")


    # Element constraint uses Python identifier constraint
    __constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'constraint'),
                                                           'constraint',
                                                           '__httpvolute_googlecode_comdmvo_dmlv0_9_Type_constraint',
                                                           True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 494, 12), )

    constraint = property(__constraint.value, __constraint.set, None,
                          u'\n                        Constraints defining valid instances of the type.\n                        May be an AttributeConstraint or an expression in some language.\n                    ')


    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Attribute abstract uses Python identifier abstract
    __abstract = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'abstract'), 'abstract',
                                                   '__httpvolute_googlecode_comdmvo_dmlv0_9_Type_abstract',
                                                   pyxb.binding.datatypes.boolean, unicode_default=u'false')
    __abstract._DeclarationLocation = pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 504, 8)
    __abstract._UseLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 504,
                                                          8)

    abstract = property(__abstract.value, __abstract.set, None, None)

    _ElementMap.update({
        __extends.name(): __extends,
        __constraint.name(): __constraint
    })
    _AttributeMap.update({
        __abstract.name(): __abstract
    })


Namespace.addCategoryObject('typeBinding', u'Type', Type)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}EnumLiteral with content type ELEMENT_ONLY
class EnumLiteral(ReferencableElement):
    """Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}EnumLiteral with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EnumLiteral')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 630, 2)
    _ElementMap = ReferencableElement._ElementMap.copy()
    _AttributeMap = ReferencableElement._AttributeMap.copy()
    # Base type is ReferencableElement

    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'EnumLiteral', EnumLiteral)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Role with content type ELEMENT_ONLY
class Role(ReferencableElement):
    """
        A Role represents the "role a Type plays in the definition of another Type".
        Generally, instances of structured types contain instances of other types, organised according to some
        predesigned pattern consisting basically of
        name-value pairs.
        The names refer to the particular role to which the values are assigned.
        These values must have the type corresponding to the role, implemented below using the datatype element.
        The values may be multiple-valued.
        Three different types
        of roles are supported in VO-DML: Attribute, COllection and Reference.
        Their characteristics are defined below.
      
        Role extends ReferencableElement.
        The 'name' element that is inherited from that type must be unique in the collection of roles
        defined on the parent type.
        This uniqueness must extend over the roles available on the type by
        inheritance.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Role')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 639, 2)
    _ElementMap = ReferencableElement._ElementMap.copy()
    _AttributeMap = ReferencableElement._AttributeMap.copy()
    # Base type is ReferencableElement

    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element datatype uses Python identifier datatype
    __datatype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'datatype'), 'datatype',
                                                         '__httpvolute_googlecode_comdmvo_dmlv0_9_Role_datatype', False,
                                                         pyxb.utils.utility.Location(
                                                             '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd',
                                                             665, 10), )

    datatype = property(__datatype.value, __datatype.set, None,
                        u'\n                Reference to the type that plays the role represented by this Role.\n              ')


    # Element multiplicity uses Python identifier multiplicity
    __multiplicity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'multiplicity'),
                                                             'multiplicity',
                                                             '__httpvolute_googlecode_comdmvo_dmlv0_9_Role_multiplicity',
                                                             False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 672, 10), )

    multiplicity = property(__multiplicity.value, __multiplicity.set, None,
                            u'\n                The multiplicity of the role (also called cardinality) indicates whether it must have a\n                value or may be without value, or possibly how many values are allowed.\n              ')


    # Element subsets uses Python identifier subsets
    __subsets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'subsets'), 'subsets',
                                                        '__httpvolute_googlecode_comdmvo_dmlv0_9_Role_subsets', False,
                                                        pyxb.utils.utility.Location(
                                                            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 680,
                                                            10), )

    subsets = property(__subsets.value, __subsets.set, None,
                       u'\n                Represents the UML subsetted property. Indicates that a particular relation refines the definition\n                of another relation. ONly a relation inherited form a base class can\n                be subsetted. Typical usage is\n                that the base class has a\n                relation to a class A, and the subclass refines this to indicating that\n                the relation should be to a subclass of A.\n\n                The value should identify the subsetted property.\n                TBD IF we are going to use utype-s to refer to elements also inside this\n                document, we should use an\n                appropriate keyref\n              \n                TBD this is a somewhat abstract, but very useful modeling concept.\n                It implements a very common modeling design pattern.\n                It exists in UML2.\n              ')


    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement
    _ElementMap.update({
        __datatype.name(): __datatype,
        __multiplicity.name(): __multiplicity,
        __subsets.name(): __subsets
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Role', Role)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}AttributeConstraints with content type ELEMENT_ONLY
class AttributeConstraints(Constraint):
    """
                An AttributeConstraint is defined of a type and references an attribute available on the type, either
                directly
                or through inheritance. It defines a set of simple constraints such as minValue/maxValue etc that
                can easily be
                parametrized and do not require the full definition of a complex constraint.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AttributeConstraints')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 917, 4)
    _ElementMap = Constraint._ElementMap.copy()
    _AttributeMap = Constraint._AttributeMap.copy()
    # Base type is Constraint

    # Element expression (expression) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Constraint

    # Element attribute uses Python identifier attribute
    __attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'attribute'), 'attribute',
                                                          '__httpvolute_googlecode_comdmvo_dmlv0_9_AttributeConstraints_attribute',
                                                          False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 930, 20), )

    attribute = property(__attribute.value, __attribute.set, None,
                         u'\n                                Identifies the attribute that is constrained. This attribute MUST be available on the\n                                type\n                            ')


    # Element minValue uses Python identifier minValue
    __minValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'minValue'), 'minValue',
                                                         '__httpvolute_googlecode_comdmvo_dmlv0_9_AttributeConstraints_minValue',
                                                         True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 939, 24), )

    minValue = property(__minValue.value, __minValue.set, None,
                        u'\n                                    For attributes with the minimum value the attribute is allowed to string attribute,\n                                    the minimum length the string must have.\n                                    TBD useful?\n                                ')


    # Element minLength uses Python identifier minLength
    __minLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'minLength'), 'minLength',
                                                          '__httpvolute_googlecode_comdmvo_dmlv0_9_AttributeConstraints_minLength',
                                                          True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 948, 24), )

    minLength = property(__minLength.value, __minLength.set, None,
                         u'\n                                    For a string attribute, the minimum length the string must have.\n                                    TBD useful?\n                                ')


    # Element maxLength uses Python identifier maxLength
    __maxLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'maxLength'), 'maxLength',
                                                          '__httpvolute_googlecode_comdmvo_dmlv0_9_AttributeConstraints_maxLength',
                                                          True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 956, 24), )

    maxLength = property(__maxLength.value, __maxLength.set, None,
                         u'\n                                    For a string attribute, the maximum length the string must have.\n                                    When <= 0, indicates the string has no length limit.\n                                ')


    # Element length uses Python identifier length
    __length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'length'), 'length',
                                                       '__httpvolute_googlecode_comdmvo_dmlv0_9_AttributeConstraints_length',
                                                       True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 964, 24), )

    length = property(__length.value, __length.set, None,
                      u'\n                                    For a string attribute, the exact length the string must have.\n                                ')


    # Element uniqueGlobally uses Python identifier uniqueGlobally
    __uniqueGlobally = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'uniqueGlobally'),
                                                               'uniqueGlobally',
                                                               '__httpvolute_googlecode_comdmvo_dmlv0_9_AttributeConstraints_uniqueGlobally',
                                                               True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 971, 24), )

    uniqueGlobally = property(__uniqueGlobally.value, __uniqueGlobally.set, None,
                              u'\n                                    Indicates that the value of the attribute must be "globally" unique.\n                                    TBD what is the context? A database, the IVOA?...\n                                ')


    # Element uniqueInCollection uses Python identifier uniqueInCollection
    __uniqueInCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'uniqueInCollection'), 'uniqueInCollection',
        '__httpvolute_googlecode_comdmvo_dmlv0_9_AttributeConstraints_uniqueInCollection', True,
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 979, 24), )

    uniqueInCollection = property(__uniqueInCollection.value, __uniqueInCollection.set, None,
                                  u'\n                                    Indicates that the value of the attribute must be unique in the collection of\n                                    objects that the parent type belongs to.\n                                    SHould be not-null.\n                                ')

    _ElementMap.update({
        __attribute.name(): __attribute,
        __minValue.name(): __minValue,
        __minLength.name(): __minLength,
        __maxLength.name(): __maxLength,
        __length.name(): __length,
        __uniqueGlobally.name(): __uniqueGlobally,
        __uniqueInCollection.name(): __uniqueInCollection
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'AttributeConstraints', AttributeConstraints)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}ObjectType with content type ELEMENT_ONLY
class ObjectType(Type):
    """
        TBD improve next description; make it less obscure; refer to ...
        "A type with an identity". This in contrast to value types where the value identifies the instance.
        Could be
        called Class to correspond closer to UML counterpart, though
        ObjectType is somewhat more explicitl.
        Using Class causes some problems in usage as it is often a reserved keyword.
        TBD should we
        include an explicit id attribute. Simplieifes it being referenced with UTYPE-s, but somewhat complex
        how to define
        minOccirs rule. Should for each concrete class have exactly one in extension
        hierarchy.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ObjectType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 509, 2)
    _ElementMap = Type._ElementMap.copy()
    _AttributeMap = Type._AttributeMap.copy()
    # Base type is Type

    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element extends (extends) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type

    # Element constraint (constraint) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type

    # Element attribute uses Python identifier attribute
    __attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'attribute'), 'attribute',
                                                          '__httpvolute_googlecode_comdmvo_dmlv0_9_ObjectType_attribute',
                                                          True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 528, 10), )

    attribute = property(__attribute.value, __attribute.set, None, u'\n                TODO\n              ')


    # Element collection uses Python identifier collection
    __collection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'collection'),
                                                           'collection',
                                                           '__httpvolute_googlecode_comdmvo_dmlv0_9_ObjectType_collection',
                                                           True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 535, 12), )

    collection = property(__collection.value, __collection.set, None, u'\n                TODO\n              ')


    # Element reference uses Python identifier reference
    __reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reference'), 'reference',
                                                          '__httpvolute_googlecode_comdmvo_dmlv0_9_ObjectType_reference',
                                                          True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 542, 10), )

    reference = property(__reference.value, __reference.set, None, u'\n                TODO\n              ')


    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Attribute abstract inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    _ElementMap.update({
        __attribute.name(): __attribute,
        __collection.name(): __collection,
        __reference.name(): __reference
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ObjectType', ObjectType)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}ValueType with content type ELEMENT_ONLY
class ValueType(Type):
    """
        Base class of all valaue types, i.e. those types identified by their value, rather than a separate explicit identifier.
        These are the types that can be assigned to Attribute-s.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ValueType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 555, 2)
    _ElementMap = Type._ElementMap.copy()
    _AttributeMap = Type._AttributeMap.copy()
    # Base type is Type

    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element extends (extends) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type

    # Element constraint (constraint) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type

    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Attribute abstract inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ValueType', ValueType)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Attribute with content type ELEMENT_ONLY
class Attribute(Role):
    """
        An Attribute is a Role where the target datatype is a ValueType.
        It represent "simple" properties of its container type, which can be an ObjectType or a DataType.
      
        Must refer to a ValueType.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Attribute')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 707, 2)
    _ElementMap = Role._ElementMap.copy()
    _AttributeMap = Role._AttributeMap.copy()
    # Base type is Role

    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element datatype (datatype) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role

    # Element multiplicity (multiplicity) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role

    # Element subsets (subsets) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role

    # Element skosconcept uses Python identifier skosconcept
    __skosconcept = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'skosconcept'),
                                                            'skosconcept',
                                                            '__httpvolute_googlecode_comdmvo_dmlv0_9_Attribute_skosconcept',
                                                            False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 720, 10), )

    skosconcept = property(__skosconcept.value, __skosconcept.set, None,
                           u'\n                It is possible to assign a SKOSConcept to an attribute definition.\n                This means that the values of the attribute have to comply with the definition of the SKOSConcept.\n                This can be done in two manners. Either the SKOSConcept\n                gives a link to a SKOS vocabulary, in which case the value must be a\n                concept defined in that vocabulary.\n                Or it defines a broadest SKOS concept, in which case the value must be a SKOS concept that is explicitly\n                declared to be (narrower than)\n                that concept, or a concept that is narrower than that concept.\n                The latter definition allows custom SKOS vocabularies to be used.\n                TBD it must be decided HOW the SKOS concept are to be represented as values.\n                By URI? By preferredLabel/en [??] as\n                defined in the vocabulary?\n                Maybe this needs to be part of the SKOSConcept definition.\n              ')


    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement
    _ElementMap.update({
        __skosconcept.name(): __skosconcept
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Attribute', Attribute)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Relation with content type ELEMENT_ONLY
class Relation(Role):
    """
        A relation is a Role where the target datatype is an ObjectType.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Relation')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 776, 2)
    _ElementMap = Role._ElementMap.copy()
    _AttributeMap = Role._AttributeMap.copy()
    # Base type is Role

    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element datatype (datatype) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role

    # Element multiplicity (multiplicity) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role

    # Element subsets (subsets) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role

    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Relation', Relation)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}PrimitiveType with content type ELEMENT_ONLY
class PrimitiveType(ValueType):
    """
        Atomic/simple type. Defined by a single value. Generally a built in type from the IVOA profile model,
        or a subclass of one of those types.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PrimitiveType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 569, 2)
    _ElementMap = ValueType._ElementMap.copy()
    _AttributeMap = ValueType._AttributeMap.copy()
    # Base type is ValueType

    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element extends (extends) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type

    # Element constraint (constraint) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type

    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Attribute abstract inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'PrimitiveType', PrimitiveType)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}DataType with content type ELEMENT_ONLY
class DataType(ValueType):
    """Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}DataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DataType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 582, 2)
    _ElementMap = ValueType._ElementMap.copy()
    _AttributeMap = ValueType._AttributeMap.copy()
    # Base type is ValueType

    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element extends (extends) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type

    # Element constraint (constraint) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type

    # Element attribute uses Python identifier attribute
    __attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'attribute'), 'attribute',
                                                          '__httpvolute_googlecode_comdmvo_dmlv0_9_DataType_attribute',
                                                          True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 586, 10), )

    attribute = property(__attribute.value, __attribute.set, None, u'\n                TODO\n              ')


    # Element reference uses Python identifier reference
    __reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reference'), 'reference',
                                                          '__httpvolute_googlecode_comdmvo_dmlv0_9_DataType_reference',
                                                          True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 593, 10), )

    reference = property(__reference.value, __reference.set, None, u'\n                TODO\n              ')


    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Attribute abstract inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    _ElementMap.update({
        __attribute.name(): __attribute,
        __reference.name(): __reference
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'DataType', DataType)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Reference with content type ELEMENT_ONLY
class Reference(Relation):
    """
        A Reference is a Relation that indicates a kind of "usage" relationship
        between the target ObjectType and the owner of the reference, the "referrer".
        The referrer can be an ObjectType (typically) but also a DataType.
        The relation is
        looser than the composition/collection relationship, acting like a
        semantically meaningful pointer rather than indicating a component of the referrer.
        Consequently, in general many referrers can point at the same target instance,
        and ObjectType-s can
        be the target in different reference definitions.
        The lifecycle of the target is not bound to that of the referrer.
        Often the target instance is used to provide a context for the definition of
        the referrer. For example a coordinate frame may be
        referenced to provide context to coordinate values.
        TBD more needed ...?
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Reference')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 790, 2)
    _ElementMap = Relation._ElementMap.copy()
    _AttributeMap = Relation._AttributeMap.copy()
    # Base type is Relation

    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element datatype (datatype) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role

    # Element multiplicity (multiplicity) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role

    # Element subsets (subsets) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role

    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Reference', Reference)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Composition with content type ELEMENT_ONLY
class Composition(Relation):
    """
          This type implements a composition relation between the parent and child ObjectTypes.
          Its instances are ONLY used to set the "collection" field on an ObjectType.
          It is a rule that an object type can only be the target of a single collection definition.
          A subclass can be assigned a target to a collection if a
        baseclass is already assigned such a target, but only if the collection is explicitly 'subsetted'.
        A collection is assumed to be a set, i.e.
        a given object (as identified by its identifier!) cannot occur
        multiple times in the collection.
        The collection
        may be ordered, whichi implies that the order in whichi objects have been added
        to
        the collection is to be preserved. As clients can always do an explicit sort on any of the child objects' attributes,
        it seems not necessary to add functionality for
        declaring a collection is
        sorted on one or more attributes.
        Through the uniqueInCollection constraint that can be assigned to attributes, a collection can impose the
        constraint that different objects in the collection
        must have distinct values of the
        attribute to which that constraint is assigned.
        It would be better probably to add the capability to assign such constraints to this collection type.
        This would
        also give more flexibility in for example creating explicit (named) keys, or defining
        multi-attribute uniqueness constraints.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Composition')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 820, 4)
    _ElementMap = Relation._ElementMap.copy()
    _AttributeMap = Relation._AttributeMap.copy()
    # Base type is Relation

    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element datatype (datatype) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role

    # Element multiplicity (multiplicity) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role

    # Element subsets (subsets) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role

    # Element isOrdered uses Python identifier isOrdered
    __isOrdered = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'isOrdered'), 'isOrdered',
                                                          '__httpvolute_googlecode_comdmvo_dmlv0_9_Composition_isOrdered',
                                                          False, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 851, 10), )

    isOrdered = property(__isOrdered.value, __isOrdered.set, None,
                         u'\n                If true, this collection preserves the ordering of object insertions.\n              ')


    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement
    _ElementMap.update({
        __isOrdered.name(): __isOrdered
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Composition', Composition)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Enumeration with content type ELEMENT_ONLY
class Enumeration(PrimitiveType):
    """
        A primitive type with a limited, discrete set of values.
        May explicitly extend a PrimitiveType. Its values must be compatible with that type then.
        TBD Should define what it
        might mean for an enumeraiton to extend another enumeration.
        Should it restrict the possible values further? Or should it add to the values? Or ...?
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Enumeration')
    _XSDLocation = pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 605, 2)
    _ElementMap = PrimitiveType._ElementMap.copy()
    _AttributeMap = PrimitiveType._AttributeMap.copy()
    # Base type is PrimitiveType

    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Element extends (extends) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type

    # Element constraint (constraint) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type

    # Element literal uses Python identifier literal
    __literal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'literal'), 'literal',
                                                        '__httpvolute_googlecode_comdmvo_dmlv0_9_Enumeration_literal',
                                                        True, pyxb.utils.utility.Location(
            '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 618, 10), )

    literal = property(__literal.value, __literal.set, None, u'\n                TODO\n              ')


    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferencableElement

    # Attribute abstract inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    _ElementMap.update({
        __literal.name(): __literal
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Enumeration', Enumeration)

model = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'model'), Model,
                                   documentation=u"\n        Every VO-DML/XML document must start with a 'model' element, no other root elements are supported by this spec.\n      ",
                                   location=pyxb.utils.utility.Location(
                                       '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 1054, 2))
Namespace.addCategoryObject('elementBinding', model.name().localName(), model)

ReferencableElement._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'vodml-id'), ElementID, scope=ReferencableElement,
                               documentation=u'\n              Identifier for its containing element.\n              Extracted as a separate type so that we can easily adapt to a different identifier design.\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6)))

ReferencableElement._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string,
                               scope=ReferencableElement,
                               documentation=u'\n            The name of the model element. May be restricted with uniqueness constraints in subclasses.\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6)))

ReferencableElement._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string,
                               scope=ReferencableElement,
                               documentation=u'\n            Human readable description of the model element.\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6)))


def _BuildAutomaton():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        ReferencableElement._UseForTag(pyxb.namespace.ExpandedName(None, u'vodml-id')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferencableElement._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        ReferencableElement._UseForTag(pyxb.namespace.ExpandedName(None, u'description')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


ReferencableElement._Automaton = _BuildAutomaton()

ElementRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'utype'), UTYPE, scope=ElementRef,
                                                  documentation=u'\n            The element identifying the referenced target element.\n            See the documentation for the UTYPE type.\n          ',
                                                  location=pyxb.utils.utility.Location(
                                                      '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 195, 6)))


def _BuildAutomaton_():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ElementRef._UseForTag(pyxb.namespace.ExpandedName(None, u'utype')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 195, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


ElementRef._Automaton = _BuildAutomaton_()

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), ModelPrefix, scope=Model,
                                             documentation=u'\n                        Short name of the model.\n                        NOTE this name MUST be used as prefix in any utype reference to elements in this model.\n                    ',
                                             location=pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 218, 12)))

Model._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string,
                               scope=Model,
                               documentation=u'\n                        The description of the model.\n                    ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 226, 12)))

Model._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'title'), pyxb.binding.datatypes.string, scope=Model,
                               documentation=u'\n              The title of the model by which it is officially known.\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 233, 12)))

Model._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'author'), pyxb.binding.datatypes.string, scope=Model,
                               documentation=u'\n                    List of authors of the model, only defined by name so far.\n            TBD could be expanded with email, affiliation and so on.\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 240, 12)))

Model._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'version'), pyxb.binding.datatypes.string,
                               scope=Model,
                               documentation=u'\n            Label giving the version of the model.\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 248, 6)))

Model._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'previousVersion'), pyxb.binding.datatypes.anyURI,
                               scope=Model,
                               documentation=u'\n            URI identifying a VO-DML model that is the version from which the current version of model is derived.\n            TBD could be an IVO Identifier once models get properly registered?\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 255, 6)))

Model._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'lastModified'), pyxb.binding.datatypes.dateTime,
                               scope=Model,
                               documentation=u'\n            Timestamp when the last change to the current model was made.\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 263, 6)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'import'), ModelProxy, scope=Model,
                                             documentation=u"\n            An 'import' element indicates a dependency on an external, predefined VO-DML data model.\n            Types from that model may be used for referencing, extension and assignment to\n            attributes.\n            Types from the external model MUST NOT be used for\n            composition relationships.\n            'identification' relations to elements from that model may be used to indicate some kind of\n            equivalence between\n            elements in the current model and the external elements.\n          \n            TBD We might require that every data model MUST include a version of the IVOA data model\n            to gain access to the standard\n            primitive types and some other types.\n            We may require that that standard model should be included *completely*,\n            i.e. including all its type definitions explicitly.\n            This would be similar to treating it as a UML Profile, rather than an import.\n            This would mean that the most common type assignments for attributes\n            can be checked within the model and not require\n            importing the remote model during validation.\n          ",
                                             location=pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 270, 6)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'package'), Package, scope=Model,
                                             documentation=u'\n                        The collection of packages which can contain further detailed name spacing to\n                        the type definitions in the model.\n                    ',
                                             location=pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 295, 12)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'objectType'), ObjectType, scope=Model,
                                             documentation=u'\n                        Collection of ObjectType definitions directly under the model, i.e. not contained in a Package.\n                    ',
                                             location=pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 303, 12)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'dataType'), DataType, scope=Model,
                                             documentation=u'\n                        Collection of DataType definitions directly under the model, i.e. not contained in a Package.\n                    ',
                                             location=pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 310, 12)))

Model._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'enumeration'), Enumeration, scope=Model,
                               documentation=u'\n                        Collection of Enumeration definitions directly under the model, i.e. not contained in a Package.\n                    ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 317, 12)))

Model._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'primitiveType'), PrimitiveType, scope=Model,
                               documentation=u'\n                        Collection of PrimitiveType definitions directly under the model, i.e. not contained in a\n                        Package.\n                    ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 324, 12)))


def _BuildAutomaton_2():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 226, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 240, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 255, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 270, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 295, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 303, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 310, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 317, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 324, 12))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 218, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, u'description')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 226, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, u'title')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 233, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, u'author')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 240, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, u'version')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 248, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, u'previousVersion')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 255, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, u'lastModified')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 263, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, u'import')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 270, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, u'package')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 295, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, u'objectType')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 303, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, u'dataType')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 310, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, u'enumeration')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 317, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, u'primitiveType')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 324, 12))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    transitions.append(fac.Transition(st_2, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
    ]))
    transitions.append(fac.Transition(st_8, [
    ]))
    transitions.append(fac.Transition(st_9, [
    ]))
    transitions.append(fac.Transition(st_10, [
    ]))
    transitions.append(fac.Transition(st_11, [
    ]))
    transitions.append(fac.Transition(st_12, [
    ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, True)]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Model._Automaton = _BuildAutomaton_2()

ModelProxy._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), ModelPrefix, scope=ModelProxy,
                               documentation=u"\n                    Name by which imported model is used in the current model and its documentation.\n                    This name MUST be the same as the 'name' of the model definition in that remote document.\n                    For all utypes pointing to elements in the imported model MUST use this name as prefix.\n                ",
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 346, 8)))

ModelProxy._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'version'), pyxb.binding.datatypes.string,
                               scope=ModelProxy,
                               documentation=u'\n                    Version of the current model.\n                ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 355, 8)))

ModelProxy._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ivoId'), pyxb.binding.datatypes.anyURI,
                               scope=ModelProxy,
                               documentation=u'\n            IVO Identifier of the imported model if that exists, i.e. if that has been registered in an IVOA Registry.\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 362, 8)))

ModelProxy._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'url'), pyxb.binding.datatypes.anyURI,
                               scope=ModelProxy,
                               documentation=u'\n            URL from which the VO-DML model document can be downloaded.\n            Note, could likely be done through a registry once ivoId is known.\n            TBD SHOULD this be a generic URI, or can we insits on URL?\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 369, 6)))

ModelProxy._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'documentationURL'), pyxb.binding.datatypes.anyURI,
                               scope=ModelProxy,
                               documentation=u'\n            URL where a documentation HTML file for the remote model can be downloaded.\n            This SHOULD be a document that contains anchors for each element thta has as name attribute the vodml-id of that element.\n            I.e. it is assumed that the\n            vodml-id-s of the imported types can be added onto this documentationURL\n            (should end with a #?) so that a direct link to the documentation for a referenced data model element can be found.\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 378, 6)))


def _BuildAutomaton_3():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 362, 8))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModelProxy._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 346, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModelProxy._UseForTag(pyxb.namespace.ExpandedName(None, u'version')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 355, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModelProxy._UseForTag(pyxb.namespace.ExpandedName(None, u'ivoId')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 362, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModelProxy._UseForTag(pyxb.namespace.ExpandedName(None, u'url')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 369, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        ModelProxy._UseForTag(pyxb.namespace.ExpandedName(None, u'documentationURL')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 378, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
    ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


ModelProxy._Automaton = _BuildAutomaton_3()

SKOSConcept._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'broadestSKOSConcept'), pyxb.binding.datatypes.anyURI,
                               scope=SKOSConcept,
                               documentation=u'\n            A URI identifiying a SKOS concept that corresponds to the concept in the model.\n            Values of a corresponding attributes must be URI-s identifiying objects that are narrower\n            than the identified concept. This attribute may be null as\n            certain vocabularies may not have a\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 755, 6)))

SKOSConcept._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'vocabularyURI'), pyxb.binding.datatypes.anyURI,
                               scope=SKOSConcept,
                               documentation=u'\n            If no broadestSKOSConcept is defined, one or more explicit vocabularies can be provided from which the\n            value must be obtained.\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 765, 6)))


def _BuildAutomaton_4():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 755, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 765, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        SKOSConcept._UseForTag(pyxb.namespace.ExpandedName(None, u'broadestSKOSConcept')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 755, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        SKOSConcept._UseForTag(pyxb.namespace.ExpandedName(None, u'vocabularyURI')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 765, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


SKOSConcept._Automaton = _BuildAutomaton_4()

Multiplicity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'minOccurs'),
                                                    pyxb.binding.datatypes.nonNegativeInteger, scope=Multiplicity,
                                                    documentation=u'\n          Lower bound on number of instances/values.\n          ',
                                                    location=pyxb.utils.utility.Location(
                                                        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 874, 6),
                                                    unicode_default=u'1'))

Multiplicity._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'maxOccurs'), pyxb.binding.datatypes.int,
                               scope=Multiplicity, documentation=u'\n          When negative, unbounded.\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 881, 6),
                               unicode_default=u'1'))


def _BuildAutomaton_5():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Multiplicity._UseForTag(pyxb.namespace.ExpandedName(None, u'minOccurs')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 874, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Multiplicity._UseForTag(pyxb.namespace.ExpandedName(None, u'maxOccurs')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 881, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Multiplicity._Automaton = _BuildAutomaton_5()

Constraint._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'expression'), ConstraintExpression, scope=Constraint,
                               documentation=u'\n            An expression constraining the value to which the constraint is applied.\n            May be human readable for now, could become a regular expression, or maybe OCL expression in future.\n            To be implemented by hand in target representations of\n            the model.\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 904, 12)))


def _BuildAutomaton_6():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 904, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Constraint._UseForTag(pyxb.namespace.ExpandedName(None, u'expression')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 904, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Constraint._Automaton = _BuildAutomaton_6()

ConstraintExpression._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'expression'), pyxb.binding.datatypes.string,
                               scope=ConstraintExpression,
                               documentation=u'\n            The expression defining the constraint. This can be in any language, one of the ones supported by the language element below,\n            or some custom language.\n          ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 1002, 6)))

ConstraintExpression._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'language'), STD_ANON, scope=ConstraintExpression,
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 1010, 6),
                               unicode_default=u'Custom'))


def _BuildAutomaton_7():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 1010, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        ConstraintExpression._UseForTag(pyxb.namespace.ExpandedName(None, u'expression')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 1002, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        ConstraintExpression._UseForTag(pyxb.namespace.ExpandedName(None, u'language')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 1010, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


ConstraintExpression._Automaton = _BuildAutomaton_7()

Package._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'objectType'), ObjectType, scope=Package,
                               documentation=u'\n                                Collection of ObjectType-s defined in this package.\n                            ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 420, 20)))

Package._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'dataType'), DataType, scope=Package,
                                               documentation=u'\n                                Collection of DataType-s defined in this package.\n                            ',
                                               location=pyxb.utils.utility.Location(
                                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 427, 20)))

Package._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'enumeration'), Enumeration, scope=Package,
                               documentation=u'\n                                Collection of Enumeration-s defined in this package.\n                            ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 434, 20)))

Package._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'primitiveType'), PrimitiveType, scope=Package,
                               documentation=u'\n                                Collection of PrimitiveType-s defined in this package.\n                            ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 441, 20)))

Package._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'package'), Package, scope=Package,
                                               documentation=u'\n                                Collection of child Package-s defined in this package.\n                            ',
                                               location=pyxb.utils.utility.Location(
                                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 448, 20)))


def _BuildAutomaton_8():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 420, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 427, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 434, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 441, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 448, 20))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, u'vodml-id')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, u'description')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, u'objectType')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 420, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, u'dataType')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 427, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, u'enumeration')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 434, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, u'primitiveType')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 441, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, u'package')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 448, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True)]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Package._Automaton = _BuildAutomaton_8()

Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'extends'), ElementRef, scope=Type,
                                            documentation=u"\n                Reference to a type (called the base-type) that is extended by the current type (called the subtype).\n                This implements the typical is-a inheritance relationship, similar to the extends relations in XSD and Java,\n                the\n                generaliation in UML, or the subclassOf relation in RDF. Note, VO-DML does not support multiple inheritance.\n                Instances of a subtype are automatic instances of a base type.\n                Polymorphism is assumed: When a role (see below) defines a base type\n                as its datatype, instances of any subtype\n                can be uased as value of the role.\n                Roles defined on a base type are inherited by the subtypes.\n                Relations inherited from a basetype can be 'subsetted', which is similar to overriding their definition.\n                See the definiton of this property on the Relation type.\n              ",
                                            location=pyxb.utils.utility.Location(
                                                '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 477, 10)))

Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'constraint'), Constraint, scope=Type,
                                            documentation=u'\n                        Constraints defining valid instances of the type.\n                        May be an AttributeConstraint or an expression in some language.\n                    ',
                                            location=pyxb.utils.utility.Location(
                                                '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 494, 12)))


def _BuildAutomaton_9():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 477, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 494, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Type._UseForTag(pyxb.namespace.ExpandedName(None, u'vodml-id')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Type._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Type._UseForTag(pyxb.namespace.ExpandedName(None, u'description')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Type._UseForTag(pyxb.namespace.ExpandedName(None, u'extends')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 477, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Type._UseForTag(pyxb.namespace.ExpandedName(None, u'constraint')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 494, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Type._Automaton = _BuildAutomaton_9()


def _BuildAutomaton_10():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EnumLiteral._UseForTag(pyxb.namespace.ExpandedName(None, u'vodml-id')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EnumLiteral._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EnumLiteral._UseForTag(pyxb.namespace.ExpandedName(None, u'description')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


EnumLiteral._Automaton = _BuildAutomaton_10()

Role._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'datatype'), ElementRef, scope=Role,
                                            documentation=u'\n                Reference to the type that plays the role represented by this Role.\n              ',
                                            location=pyxb.utils.utility.Location(
                                                '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 665, 10)))

Role._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'multiplicity'), Multiplicity, scope=Role,
                               documentation=u'\n                The multiplicity of the role (also called cardinality) indicates whether it must have a\n                value or may be without value, or possibly how many values are allowed.\n              ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 672, 10)))

Role._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'subsets'), ElementRef, scope=Role,
                                            documentation=u'\n                Represents the UML subsetted property. Indicates that a particular relation refines the definition\n                of another relation. ONly a relation inherited form a base class can\n                be subsetted. Typical usage is\n                that the base class has a\n                relation to a class A, and the subclass refines this to indicating that\n                the relation should be to a subclass of A.\n\n                The value should identify the subsetted property.\n                TBD IF we are going to use utype-s to refer to elements also inside this\n                document, we should use an\n                appropriate keyref\n              \n                TBD this is a somewhat abstract, but very useful modeling concept.\n                It implements a very common modeling design pattern.\n                It exists in UML2.\n              ',
                                            location=pyxb.utils.utility.Location(
                                                '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 680, 10)))


def _BuildAutomaton_11():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 680, 10))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Role._UseForTag(pyxb.namespace.ExpandedName(None, u'vodml-id')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Role._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Role._UseForTag(pyxb.namespace.ExpandedName(None, u'description')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Role._UseForTag(pyxb.namespace.ExpandedName(None, u'datatype')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 665, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Role._UseForTag(pyxb.namespace.ExpandedName(None, u'multiplicity')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 672, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Role._UseForTag(pyxb.namespace.ExpandedName(None, u'subsets')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 680, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
    ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True)]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Role._Automaton = _BuildAutomaton_11()

AttributeConstraints._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'attribute'), ElementRef, scope=AttributeConstraints,
                               documentation=u'\n                                Identifies the attribute that is constrained. This attribute MUST be available on the\n                                type\n                            ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 930, 20)))

AttributeConstraints._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'minValue'), pyxb.binding.datatypes.string,
                               scope=AttributeConstraints,
                               documentation=u'\n                                    For attributes with the minimum value the attribute is allowed to string attribute,\n                                    the minimum length the string must have.\n                                    TBD useful?\n                                ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 939, 24)))

AttributeConstraints._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'minLength'), pyxb.binding.datatypes.int,
                               scope=AttributeConstraints,
                               documentation=u'\n                                    For a string attribute, the minimum length the string must have.\n                                    TBD useful?\n                                ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 948, 24)))

AttributeConstraints._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'maxLength'), pyxb.binding.datatypes.int,
                               scope=AttributeConstraints,
                               documentation=u'\n                                    For a string attribute, the maximum length the string must have.\n                                    When <= 0, indicates the string has no length limit.\n                                ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 956, 24)))

AttributeConstraints._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'length'), pyxb.binding.datatypes.int,
                               scope=AttributeConstraints,
                               documentation=u'\n                                    For a string attribute, the exact length the string must have.\n                                ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 964, 24)))

AttributeConstraints._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'uniqueGlobally'), pyxb.binding.datatypes.boolean,
                               scope=AttributeConstraints,
                               documentation=u'\n                                    Indicates that the value of the attribute must be "globally" unique.\n                                    TBD what is the context? A database, the IVOA?...\n                                ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 971, 24),
                               unicode_default=u'false'))

AttributeConstraints._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'uniqueInCollection'), pyxb.binding.datatypes.boolean,
                               scope=AttributeConstraints,
                               documentation=u'\n                                    Indicates that the value of the attribute must be unique in the collection of\n                                    objects that the parent type belongs to.\n                                    SHould be not-null.\n                                ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 979, 24),
                               unicode_default=u'false'))


def _BuildAutomaton_12():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 904, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        AttributeConstraints._UseForTag(pyxb.namespace.ExpandedName(None, u'expression')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 904, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        AttributeConstraints._UseForTag(pyxb.namespace.ExpandedName(None, u'attribute')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 930, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        AttributeConstraints._UseForTag(pyxb.namespace.ExpandedName(None, u'minValue')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 939, 24))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        AttributeConstraints._UseForTag(pyxb.namespace.ExpandedName(None, u'minLength')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 948, 24))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        AttributeConstraints._UseForTag(pyxb.namespace.ExpandedName(None, u'maxLength')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 956, 24))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        AttributeConstraints._UseForTag(pyxb.namespace.ExpandedName(None, u'length')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 964, 24))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        AttributeConstraints._UseForTag(pyxb.namespace.ExpandedName(None, u'uniqueGlobally')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 971, 24))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        AttributeConstraints._UseForTag(pyxb.namespace.ExpandedName(None, u'uniqueInCollection')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 979, 24))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


AttributeConstraints._Automaton = _BuildAutomaton_12()

ObjectType._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'attribute'), Attribute, scope=ObjectType,
                               documentation=u'\n                TODO\n              ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 528, 10)))

ObjectType._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'collection'), Composition, scope=ObjectType,
                               documentation=u'\n                TODO\n              ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 535, 12)))

ObjectType._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reference'), Reference, scope=ObjectType,
                               documentation=u'\n                TODO\n              ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 542, 10)))


def _BuildAutomaton_13():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 477, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 494, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 528, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 535, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 542, 10))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'vodml-id')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'description')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'extends')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 477, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'constraint')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 494, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'attribute')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 528, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'collection')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 535, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, u'reference')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 542, 10))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True)]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


ObjectType._Automaton = _BuildAutomaton_13()


def _BuildAutomaton_14():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 477, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 494, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueType._UseForTag(pyxb.namespace.ExpandedName(None, u'vodml-id')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueType._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ValueType._UseForTag(pyxb.namespace.ExpandedName(None, u'description')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ValueType._UseForTag(pyxb.namespace.ExpandedName(None, u'extends')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 477, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ValueType._UseForTag(pyxb.namespace.ExpandedName(None, u'constraint')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 494, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


ValueType._Automaton = _BuildAutomaton_14()

Attribute._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'skosconcept'), SKOSConcept, scope=Attribute,
                               documentation=u'\n                It is possible to assign a SKOSConcept to an attribute definition.\n                This means that the values of the attribute have to comply with the definition of the SKOSConcept.\n                This can be done in two manners. Either the SKOSConcept\n                gives a link to a SKOS vocabulary, in which case the value must be a\n                concept defined in that vocabulary.\n                Or it defines a broadest SKOS concept, in which case the value must be a SKOS concept that is explicitly\n                declared to be (narrower than)\n                that concept, or a concept that is narrower than that concept.\n                The latter definition allows custom SKOS vocabularies to be used.\n                TBD it must be decided HOW the SKOS concept are to be represented as values.\n                By URI? By preferredLabel/en [??] as\n                defined in the vocabulary?\n                Maybe this needs to be part of the SKOSConcept definition.\n              ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 720, 10)))


def _BuildAutomaton_15():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 680, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 720, 10))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Attribute._UseForTag(pyxb.namespace.ExpandedName(None, u'vodml-id')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Attribute._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Attribute._UseForTag(pyxb.namespace.ExpandedName(None, u'description')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Attribute._UseForTag(pyxb.namespace.ExpandedName(None, u'datatype')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 665, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Attribute._UseForTag(pyxb.namespace.ExpandedName(None, u'multiplicity')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 672, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Attribute._UseForTag(pyxb.namespace.ExpandedName(None, u'subsets')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 680, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Attribute._UseForTag(pyxb.namespace.ExpandedName(None, u'skosconcept')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 720, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
    ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True)]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Attribute._Automaton = _BuildAutomaton_15()


def _BuildAutomaton_16():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 680, 10))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relation._UseForTag(pyxb.namespace.ExpandedName(None, u'vodml-id')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relation._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relation._UseForTag(pyxb.namespace.ExpandedName(None, u'description')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relation._UseForTag(pyxb.namespace.ExpandedName(None, u'datatype')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 665, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Relation._UseForTag(pyxb.namespace.ExpandedName(None, u'multiplicity')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 672, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Relation._UseForTag(pyxb.namespace.ExpandedName(None, u'subsets')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 680, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
    ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True)]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Relation._Automaton = _BuildAutomaton_16()


def _BuildAutomaton_17():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 477, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 494, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PrimitiveType._UseForTag(pyxb.namespace.ExpandedName(None, u'vodml-id')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PrimitiveType._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        PrimitiveType._UseForTag(pyxb.namespace.ExpandedName(None, u'description')),
        pyxb.utils.utility.Location('/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PrimitiveType._UseForTag(pyxb.namespace.ExpandedName(None, u'extends')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 477, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PrimitiveType._UseForTag(pyxb.namespace.ExpandedName(None, u'constraint')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 494, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


PrimitiveType._Automaton = _BuildAutomaton_17()

DataType._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'attribute'), Attribute, scope=DataType,
                               documentation=u'\n                TODO\n              ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 586, 10)))

DataType._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reference'), Reference, scope=DataType,
                               documentation=u'\n                TODO\n              ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 593, 10)))


def _BuildAutomaton_18():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 477, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 494, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 586, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 593, 10))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(None, u'vodml-id')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(None, u'description')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(None, u'extends')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 477, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(None, u'constraint')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 494, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(None, u'attribute')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 586, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(None, u'reference')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 593, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True)]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


DataType._Automaton = _BuildAutomaton_18()


def _BuildAutomaton_19():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 680, 10))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, u'vodml-id')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, u'description')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, u'datatype')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 665, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, u'multiplicity')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 672, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, u'subsets')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 680, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
    ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True)]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Reference._Automaton = _BuildAutomaton_19()

Composition._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'isOrdered'), pyxb.binding.datatypes.boolean,
                               scope=Composition,
                               documentation=u'\n                If true, this collection preserves the ordering of object insertions.\n              ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 851, 10),
                               unicode_default=u'false'))


def _BuildAutomaton_20():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 680, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 851, 10))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, u'vodml-id')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, u'description')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, u'datatype')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 665, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, u'multiplicity')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 672, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, u'subsets')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 680, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, u'isOrdered')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 851, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
    ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True)]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Composition._Automaton = _BuildAutomaton_20()

Enumeration._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'literal'), EnumLiteral, scope=Enumeration,
                               documentation=u'\n                TODO\n              ',
                               location=pyxb.utils.utility.Location(
                                   '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 618, 10)))


def _BuildAutomaton_21():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 477, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(
        '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 494, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Enumeration._UseForTag(pyxb.namespace.ExpandedName(None, u'vodml-id')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 145, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Enumeration._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 153, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Enumeration._UseForTag(pyxb.namespace.ExpandedName(None, u'description')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 160, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Enumeration._UseForTag(pyxb.namespace.ExpandedName(None, u'extends')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 477, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Enumeration._UseForTag(pyxb.namespace.ExpandedName(None, u'constraint')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 494, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Enumeration._UseForTag(pyxb.namespace.ExpandedName(None, u'literal')),
                                             pyxb.utils.utility.Location(
                                                 '/Users/olaurino/PycharmProjects/volib/aux/vo-dml.xsd', 618, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Enumeration._Automaton = _BuildAutomaton_21()

