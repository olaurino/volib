# .\vodml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:6d743b07dfdab5359eb1250ad861ef9d25bd7952
# Generated 2015-04-18 17:16:35.320000 by PyXB version 1.2.4 using Python 2.7.9.final.0
# Namespace http://volute.googlecode.com/dm/vo-dml/v0.9

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:317f77a1-e610-11e4-9312-5cc5d49a9b64')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://volute.googlecode.com/dm/vo-dml/v0.9', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
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
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://volute.googlecode.com/dm/vo-dml/v0.9}VODMLID
class VODMLID (pyxb.binding.datatypes.string):

    """
          Type representing the way referable elements are identified uniquely in VO-DML.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VODMLID')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 21, 2)
    _Documentation = '\n          Type representing the way referable elements are identified uniquely in VO-DML.\n      '
VODMLID._CF_pattern = pyxb.binding.facets.CF_pattern()
VODMLID._CF_pattern.addPattern(pattern='[\\w\\._-]+')
VODMLID._InitializeFacetMap(VODMLID._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'VODMLID', VODMLID)

# Atomic simple type: {http://volute.googlecode.com/dm/vo-dml/v0.9}ModelName
class ModelName (pyxb.binding.datatypes.string):

    """
        Type used to restrict valid values for prefixes.
        TBD We could use an xsd:NCName for this.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ModelName')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 38, 2)
    _Documentation = '\n        Type used to restrict valid values for prefixes.\n        TBD We could use an xsd:NCName for this.\n      '
ModelName._CF_pattern = pyxb.binding.facets.CF_pattern()
ModelName._CF_pattern.addPattern(pattern='[\\w_-]+')
ModelName._InitializeFacetMap(ModelName._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ModelName', ModelName)

# Atomic simple type: {http://volute.googlecode.com/dm/vo-dml/v0.9}VODMLREF
class VODMLREF (pyxb.binding.datatypes.string):

    """
        Class representing the way ReferencableElements can be referenced in VO-DML.
        It must be possible to refer to elements in other, imported data models as well as in the current model.
        Hence the VODMLREF must identify both model and element.
        The element is identified by the VO-DML ID in the model, the model is identified using a
          prefix that MUST correspond to the vodml-id element of the current or an imported model.
          Note, references to element sin the current model MUST also have a prefix, there is no default model!
        TBD We could use an xsd:QName where VODMLREF is used, but that may have somewhat more sever syntax constraints than desired.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VODMLREF')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 56, 2)
    _Documentation = '\n        Class representing the way ReferencableElements can be referenced in VO-DML.\n        It must be possible to refer to elements in other, imported data models as well as in the current model.\n        Hence the VODMLREF must identify both model and element.\n        The element is identified by the VO-DML ID in the model, the model is identified using a\n          prefix that MUST correspond to the vodml-id element of the current or an imported model.\n          Note, references to element sin the current model MUST also have a prefix, there is no default model!\n        TBD We could use an xsd:QName where VODMLREF is used, but that may have somewhat more sever syntax constraints than desired.\n      '
VODMLREF._CF_pattern = pyxb.binding.facets.CF_pattern()
VODMLREF._CF_pattern.addPattern(pattern='[\\w_-]+:[\\w_\\-/\\./*]+')
VODMLREF._InitializeFacetMap(VODMLREF._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'VODMLREF', VODMLREF)

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.NCName):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 115, 8)
    _Documentation = None
STD_ANON._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minLength)

# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement with content type ELEMENT_ONLY
class ReferableElement (pyxb.binding.basis.complexTypeDefinition):
    """
        This is the base type for all types whose elements can be explicitly referenced.
        To this end it has a 'vodml-id' element of type VODMLID that allows explicit and unique identification of 
        these elements within the context of the model.
        Generally these are also elements that can be
        represented explicitly in alternative serialisations of
        a data model, such as a VOTable or a relational model.
        These should use the value of the utype element to "point into a data model" and identify a
        model element. VO-DML itself also has needs of pointing to other elements, sometimes in another model.
        The VODMLREF type is used for such references, which will always be named 'vodml-ref'.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferableElement')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 85, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element vodml-id uses Python identifier vodml_id
    __vodml_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vodml-id'), 'vodml_id', '__httpvolute_googlecode_comdmvo_dmlv0_9_ReferableElement_vodml_id', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6), )

    
    vodml_id = property(__vodml_id.value, __vodml_id.set, None, '\n              Identifier for its containing element.\n              Extracted as a separate type so that we can easily adapt to a different identifier design.\n          ')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpvolute_googlecode_comdmvo_dmlv0_9_ReferableElement_name', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6), )

    
    name = property(__name.value, __name.set, None, '\n            The name of the model element. \n            MUST NOT be an empty string.\n          ')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpvolute_googlecode_comdmvo_dmlv0_9_ReferableElement_description', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6), )

    
    description = property(__description.value, __description.set, None, '\n            Human readable description of the model element.\n          ')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpvolute_googlecode_comdmvo_dmlv0_9_ReferableElement_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 130, 4)
    __id._UseLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 130, 4)
    
    id = property(__id.value, __id.set, None, '\n          A referencable element may be given an @id attribute to reflect an identifier\n          defined in some source document form which a VO-DML model may have been derived.\n        ')

    _ElementMap.update({
        __vodml_id.name() : __vodml_id,
        __name.name() : __name,
        __description.name() : __description
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'ReferableElement', ReferableElement)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}ElementRef with content type ELEMENT_ONLY
class ElementRef (pyxb.binding.basis.complexTypeDefinition):
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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ElementRef')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 141, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element vodml-ref uses Python identifier vodml_ref
    __vodml_ref = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vodml-ref'), 'vodml_ref', '__httpvolute_googlecode_comdmvo_dmlv0_9_ElementRef_vodml_ref', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 156, 6), )

    
    vodml_ref = property(__vodml_ref.value, __vodml_ref.set, None, '\n            The element identifying the referenced target element.\n            See the documentation for the VODMLREF type.\n          ')

    _ElementMap.update({
        __vodml_ref.name() : __vodml_ref
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ElementRef', ElementRef)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Model with content type ELEMENT_ONLY
class Model (pyxb.binding.basis.complexTypeDefinition):
    """
                Represents a complete data model and is the type of the (single) declared root element for
                VO-DML/XML representation documents.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Model')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 171, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_name', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 179, 12), )

    
    name = property(__name.value, __name.set, None, '\n                        Short name of the model.\n                        NOTE this name MUST be used as prefix in any utype reference to elements in this model.\n                    ')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_description', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 187, 12), )

    
    description = property(__description.value, __description.set, None, '\n                        The description of the model.\n                    ')

    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_title', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 194, 12), )

    
    title = property(__title.value, __title.set, None, '\n              The title of the model by which it is officially known.\n          ')

    
    # Element author uses Python identifier author
    __author = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'author'), 'author', '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_author', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 201, 12), )

    
    author = property(__author.value, __author.set, None, '\n                    List of authors of the model, only defined by name so far.\n            TBD could be expanded with email, affiliation and so on.\n          ')

    
    # Element version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_version', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 209, 6), )

    
    version = property(__version.value, __version.set, None, '\n            Label giving the version of the model.\n          ')

    
    # Element previousVersion uses Python identifier previousVersion
    __previousVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'previousVersion'), 'previousVersion', '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_previousVersion', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 216, 6), )

    
    previousVersion = property(__previousVersion.value, __previousVersion.set, None, '\n            URI identifying a VO-DML model that is the version from which the current version of model is derived.\n            TBD could be an IVO Identifier once models get properly registered?\n          ')

    
    # Element lastModified uses Python identifier lastModified
    __lastModified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lastModified'), 'lastModified', '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_lastModified', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 224, 6), )

    
    lastModified = property(__lastModified.value, __lastModified.set, None, '\n            Timestamp when the last change to the current model was made.\n          ')

    
    # Element import uses Python identifier import_
    __import = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'import'), 'import_', '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_import', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 231, 6), )

    
    import_ = property(__import.value, __import.set, None, "\n            An 'import' element indicates a dependency on an external, predefined VO-DML data model.\n            Types from that model may be used for referencing, extension and assignment to\n            attributes.\n            Types from the external model MUST NOT be used for\n            composition relationships.\n            'identification' relations to elements from that model may be used to indicate some kind of\n            equivalence between\n            elements in the current model and the external elements.\n          \n            TBD We might require that every data model MUST include a version of the IVOA data model\n            to gain access to the standard\n            primitive types and some other types.\n            We may require that that standard model should be included *completely*,\n            i.e. including all its type definitions explicitly.\n            This would be similar to treating it as a UML Profile, rather than an import.\n            This would mean that the most common type assignments for attributes\n            can be checked within the model and not require\n            importing the remote model during validation.\n          ")

    
    # Element primitiveType uses Python identifier primitiveType
    __primitiveType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'primitiveType'), 'primitiveType', '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_primitiveType', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 256, 12), )

    
    primitiveType = property(__primitiveType.value, __primitiveType.set, None, '\n                        Collection of PrimitiveType definitions directly under the model, i.e. not contained in a\n                        Package.\n                    ')

    
    # Element enumeration uses Python identifier enumeration
    __enumeration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'enumeration'), 'enumeration', '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_enumeration', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 264, 12), )

    
    enumeration = property(__enumeration.value, __enumeration.set, None, '\n                        Collection of Enumeration definitions directly under the model, i.e. not contained in a Package.\n                    ')

    
    # Element dataType uses Python identifier dataType
    __dataType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dataType'), 'dataType', '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_dataType', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 271, 12), )

    
    dataType = property(__dataType.value, __dataType.set, None, '\n                        Collection of DataType definitions directly under the model, i.e. not contained in a Package.\n                    ')

    
    # Element objectType uses Python identifier objectType
    __objectType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'objectType'), 'objectType', '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_objectType', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 278, 12), )

    
    objectType = property(__objectType.value, __objectType.set, None, '\n                        Collection of ObjectType definitions directly under the model, i.e. not contained in a Package.\n                    ')

    
    # Element package uses Python identifier package
    __package = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'package'), 'package', '__httpvolute_googlecode_comdmvo_dmlv0_9_Model_package', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 285, 12), )

    
    package = property(__package.value, __package.set, None, '\n                        The collection of packages which can contain further detailed name spacing to\n                        the type definitions in the model.\n                    ')

    _ElementMap.update({
        __name.name() : __name,
        __description.name() : __description,
        __title.name() : __title,
        __author.name() : __author,
        __version.name() : __version,
        __previousVersion.name() : __previousVersion,
        __lastModified.name() : __lastModified,
        __import.name() : __import,
        __primitiveType.name() : __primitiveType,
        __enumeration.name() : __enumeration,
        __dataType.name() : __dataType,
        __objectType.name() : __objectType,
        __package.name() : __package
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Model', Model)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}ModelImport with content type ELEMENT_ONLY
class ModelImport (pyxb.binding.basis.complexTypeDefinition):
    """
        A "proxy" for an external model that is being used by the current model. 
        Defines the url where the VO-DML representation of that model can be retrieved, and
        replicates its name that MUST be used when making references to
        elements in that model using a VODMLREF element.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ModelImport')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 297, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpvolute_googlecode_comdmvo_dmlv0_9_ModelImport_name', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 307, 8), )

    
    name = property(__name.value, __name.set, None, "\n                    Name by which imported model is used in the current model and its documentation.\n                    This name MUST be the same as the 'name' of the model definition in that remote document.\n                    For all utypes pointing to elements in the imported model MUST use this name as prefix.\n                ")

    
    # Element version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpvolute_googlecode_comdmvo_dmlv0_9_ModelImport_version', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 316, 8), )

    
    version = property(__version.value, __version.set, None, '\n                    Version of the imported model.\n                ')

    
    # Element url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__httpvolute_googlecode_comdmvo_dmlv0_9_ModelImport_url', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 323, 6), )

    
    url = property(__url.value, __url.set, None, '\n            URL from which the VO-DML model document can be downloaded.\n            Note, could likely be done through a registry once ivoId is known.\n            TBD SHOULD this be a generic URI, or can we insits on URL?\n          ')

    
    # Element documentationURL uses Python identifier documentationURL
    __documentationURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'documentationURL'), 'documentationURL', '__httpvolute_googlecode_comdmvo_dmlv0_9_ModelImport_documentationURL', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 332, 6), )

    
    documentationURL = property(__documentationURL.value, __documentationURL.set, None, '\n            URL where a documentation HTML file for the remote model can be downloaded.\n            This SHOULD be a document that contains anchors for each element thta has as name attribute the vodml-id of that element.\n            I.e. it is assumed that the\n            vodml-id-s of the imported types can be added onto this documentationURL\n            (should end with a #?) so that a direct link to the documentation for a referenced data model element can be found.\n          ')

    _ElementMap.update({
        __name.name() : __name,
        __version.name() : __version,
        __url.name() : __url,
        __documentationURL.name() : __documentationURL
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ModelImport', ModelImport)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}SKOSConcept with content type ELEMENT_ONLY
class SKOSConcept (pyxb.binding.basis.complexTypeDefinition):
    """
        Type used to indicate on attributes that they take values representing a concept defined in
        an identified SKOS vocabulary, and/or restricted by being narrower than an
        identified "broadest" concept.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SKOSConcept')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 690, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element broadestSKOSConcept uses Python identifier broadestSKOSConcept
    __broadestSKOSConcept = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'broadestSKOSConcept'), 'broadestSKOSConcept', '__httpvolute_googlecode_comdmvo_dmlv0_9_SKOSConcept_broadestSKOSConcept', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 699, 6), )

    
    broadestSKOSConcept = property(__broadestSKOSConcept.value, __broadestSKOSConcept.set, None, '\n            A URI identifiying a SKOS concept that corresponds to the concept in the model.\n            Values of a corresponding attributes must be URI-s identifiying objects that are narrower\n            than the identified concept. This attribute may be null as\n            certain vocabularies may not have a\n          ')

    
    # Element vocabularyURI uses Python identifier vocabularyURI
    __vocabularyURI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vocabularyURI'), 'vocabularyURI', '__httpvolute_googlecode_comdmvo_dmlv0_9_SKOSConcept_vocabularyURI', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 709, 6), )

    
    vocabularyURI = property(__vocabularyURI.value, __vocabularyURI.set, None, '\n            If no broadestSKOSConcept is defined, one or more explicit vocabularies can be provided from which the\n            value must be obtained.\n          ')

    _ElementMap.update({
        __broadestSKOSConcept.name() : __broadestSKOSConcept,
        __vocabularyURI.name() : __vocabularyURI
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SKOSConcept', SKOSConcept)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Multiplicity with content type ELEMENT_ONLY
class Multiplicity (pyxb.binding.basis.complexTypeDefinition):
    """
        Also called "Cardinality". Indicates how many instances of a datatype can/must be associated to a given role.
        Unless
        Follows model in XSD, i.e. with explicit lower bound and upper bound on number of instances.
        maxOccurs must be gte minOccurs, unless it is negative, in which case it corresponds to unbounded.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Multiplicity')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 808, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element minOccurs uses Python identifier minOccurs
    __minOccurs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'minOccurs'), 'minOccurs', '__httpvolute_googlecode_comdmvo_dmlv0_9_Multiplicity_minOccurs', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 818, 6), )

    
    minOccurs = property(__minOccurs.value, __minOccurs.set, None, '\n          Lower bound on number of instances/values.\n          ')

    
    # Element maxOccurs uses Python identifier maxOccurs
    __maxOccurs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'maxOccurs'), 'maxOccurs', '__httpvolute_googlecode_comdmvo_dmlv0_9_Multiplicity_maxOccurs', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 825, 6), )

    
    maxOccurs = property(__maxOccurs.value, __maxOccurs.set, None, '\n          When negative, unbounded.\n          ')

    _ElementMap.update({
        __minOccurs.name() : __minOccurs,
        __maxOccurs.name() : __maxOccurs
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Multiplicity', Multiplicity)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Package with content type ELEMENT_ONLY
class Package (ReferableElement):
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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Package')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 347, 4)
    _ElementMap = ReferableElement._ElementMap.copy()
    _AttributeMap = ReferableElement._AttributeMap.copy()
    # Base type is ReferableElement
    
    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element primitiveType uses Python identifier primitiveType
    __primitiveType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'primitiveType'), 'primitiveType', '__httpvolute_googlecode_comdmvo_dmlv0_9_Package_primitiveType', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 374, 20), )

    
    primitiveType = property(__primitiveType.value, __primitiveType.set, None, '\n                                Collection of PrimitiveType-s defined in this package.\n                            ')

    
    # Element enumeration uses Python identifier enumeration
    __enumeration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'enumeration'), 'enumeration', '__httpvolute_googlecode_comdmvo_dmlv0_9_Package_enumeration', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 381, 20), )

    
    enumeration = property(__enumeration.value, __enumeration.set, None, '\n                                Collection of Enumeration-s defined in this package.\n                            ')

    
    # Element dataType uses Python identifier dataType
    __dataType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dataType'), 'dataType', '__httpvolute_googlecode_comdmvo_dmlv0_9_Package_dataType', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 388, 20), )

    
    dataType = property(__dataType.value, __dataType.set, None, '\n                                Collection of DataType-s defined in this package.\n                            ')

    
    # Element objectType uses Python identifier objectType
    __objectType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'objectType'), 'objectType', '__httpvolute_googlecode_comdmvo_dmlv0_9_Package_objectType', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 395, 20), )

    
    objectType = property(__objectType.value, __objectType.set, None, '\n                                Collection of ObjectType-s defined in this package.\n                            ')

    
    # Element package uses Python identifier package
    __package = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'package'), 'package', '__httpvolute_googlecode_comdmvo_dmlv0_9_Package_package', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 402, 20), )

    
    package = property(__package.value, __package.set, None, '\n                                Collection of child Package-s defined in this package.\n                            ')

    
    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    _ElementMap.update({
        __primitiveType.name() : __primitiveType,
        __enumeration.name() : __enumeration,
        __dataType.name() : __dataType,
        __objectType.name() : __objectType,
        __package.name() : __package
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Package', Package)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Type with content type ELEMENT_ONLY
class Type (ReferableElement):
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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Type')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 416, 4)
    _ElementMap = ReferableElement._ElementMap.copy()
    _AttributeMap = ReferableElement._AttributeMap.copy()
    # Base type is ReferableElement
    
    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element extends uses Python identifier extends
    __extends = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'extends'), 'extends', '__httpvolute_googlecode_comdmvo_dmlv0_9_Type_extends', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 431, 10), )

    
    extends = property(__extends.value, __extends.set, None, "\n                Reference to a type (called the base-type) that is extended by the current type (called the subtype).\n                This implements the typical is-a inheritance relationship, similar to the extends relations in XSD and Java,\n                the\n                generaliation in UML, or the subclassOf relation in RDF. Note, VO-DML does not support multiple inheritance.\n                Instances of a subtype are automatic instances of a base type.\n                Polymorphism is assumed: When a role (see below) defines a base type\n                as its datatype, instances of any subtype\n                can be uased as value of the role.\n                Roles defined on a base type are inherited by the subtypes.\n                Relations inherited from a basetype can be 'subsetted', which is similar to overriding their definition.\n                See the definiton of this property on the Relation type.\n              ")

    
    # Element constraint uses Python identifier constraint
    __constraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'constraint'), 'constraint', '__httpvolute_googlecode_comdmvo_dmlv0_9_Type_constraint', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 448, 12), )

    
    constraint = property(__constraint.value, __constraint.set, None, '\n                        Constraints defining valid instances of the type.\n                        May be an AttributeConstraint or an expression in some language.\n                    ')

    
    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Attribute abstract uses Python identifier abstract
    __abstract = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'abstract'), 'abstract', '__httpvolute_googlecode_comdmvo_dmlv0_9_Type_abstract', pyxb.binding.datatypes.boolean, unicode_default='false')
    __abstract._DeclarationLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 458, 8)
    __abstract._UseLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 458, 8)
    
    abstract = property(__abstract.value, __abstract.set, None, None)

    _ElementMap.update({
        __extends.name() : __extends,
        __constraint.name() : __constraint
    })
    _AttributeMap.update({
        __abstract.name() : __abstract
    })
Namespace.addCategoryObject('typeBinding', 'Type', Type)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}EnumLiteral with content type ELEMENT_ONLY
class EnumLiteral (ReferableElement):
    """Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}EnumLiteral with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EnumLiteral')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 574, 2)
    _ElementMap = ReferableElement._ElementMap.copy()
    _AttributeMap = ReferableElement._AttributeMap.copy()
    # Base type is ReferableElement
    
    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'EnumLiteral', EnumLiteral)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Role with content type ELEMENT_ONLY
class Role (ReferableElement):
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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Role')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 583, 2)
    _ElementMap = ReferableElement._ElementMap.copy()
    _AttributeMap = ReferableElement._AttributeMap.copy()
    # Base type is ReferableElement
    
    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element datatype uses Python identifier datatype
    __datatype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'datatype'), 'datatype', '__httpvolute_googlecode_comdmvo_dmlv0_9_Role_datatype', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 609, 10), )

    
    datatype = property(__datatype.value, __datatype.set, None, '\n                Reference to the type that plays the role represented by this Role.\n              ')

    
    # Element multiplicity uses Python identifier multiplicity
    __multiplicity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'multiplicity'), 'multiplicity', '__httpvolute_googlecode_comdmvo_dmlv0_9_Role_multiplicity', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 616, 10), )

    
    multiplicity = property(__multiplicity.value, __multiplicity.set, None, '\n                The multiplicity of the role (also called cardinality) indicates whether it must have a\n                value or may be without value, or possibly how many values are allowed.\n              ')

    
    # Element subsets uses Python identifier subsets
    __subsets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'subsets'), 'subsets', '__httpvolute_googlecode_comdmvo_dmlv0_9_Role_subsets', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 624, 10), )

    
    subsets = property(__subsets.value, __subsets.set, None, '\n                Represents the UML subsetted property. Indicates that a particular relation refines the definition\n                of another relation. ONly a relation inherited form a base class can\n                be subsetted. Typical usage is\n                that the base class has a\n                relation to a class A, and the subclass refines this to indicating that\n                the relation should be to a subclass of A.\n\n                The value should identify the subsetted property.\n                TBD IF we are going to use utype-s to refer to elements also inside this\n                document, we should use an\n                appropriate keyref\n              \n                TBD this is a somewhat abstract, but very useful modeling concept.\n                It implements a very common modeling design pattern.\n                It exists in UML2.\n              ')

    
    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    _ElementMap.update({
        __datatype.name() : __datatype,
        __multiplicity.name() : __multiplicity,
        __subsets.name() : __subsets
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Role', Role)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Constraint with content type ELEMENT_ONLY
class Constraint (ReferableElement):
    """
      Constraint represents rules that instances of Type-s must obey to be valid.  
      A Constraint is a referable element. Its description element describes the constrait in English.
      In future versions of the language extra elements may be added that give a more formal
      definition of the constraint. In particular we may add expressions in a language
      such as OCL or subset thereof tuned to VO-DML.
      In terms of OCL, VO-DML COnstraint-s are invariants of a Type.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Constraint')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 836, 4)
    _ElementMap = ReferableElement._ElementMap.copy()
    _AttributeMap = ReferableElement._AttributeMap.copy()
    # Base type is ReferableElement
    
    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Constraint', Constraint)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}ObjectType with content type ELEMENT_ONLY
class ObjectType (Type):
    """
        TBD use description form VO-DML specification document. to ...
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ObjectType')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 463, 2)
    _ElementMap = Type._ElementMap.copy()
    _AttributeMap = Type._AttributeMap.copy()
    # Base type is Type
    
    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element extends (extends) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    
    # Element constraint (constraint) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    
    # Element attribute uses Python identifier attribute
    __attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'attribute'), 'attribute', '__httpvolute_googlecode_comdmvo_dmlv0_9_ObjectType_attribute', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 472, 10), )

    
    attribute = property(__attribute.value, __attribute.set, None, '\n                TODO\n              ')

    
    # Element collection uses Python identifier collection
    __collection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'collection'), 'collection', '__httpvolute_googlecode_comdmvo_dmlv0_9_ObjectType_collection', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 479, 12), )

    
    collection = property(__collection.value, __collection.set, None, '\n                TODO\n              ')

    
    # Element reference uses Python identifier reference
    __reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reference'), 'reference', '__httpvolute_googlecode_comdmvo_dmlv0_9_ObjectType_reference', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 486, 10), )

    
    reference = property(__reference.value, __reference.set, None, '\n                TODO\n              ')

    
    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Attribute abstract inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    _ElementMap.update({
        __attribute.name() : __attribute,
        __collection.name() : __collection,
        __reference.name() : __reference
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ObjectType', ObjectType)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}ValueType with content type ELEMENT_ONLY
class ValueType (Type):
    """
        Base class of all valaue types, i.e. those types identified by their value, rather than a separate explicit identifier.
        These are the types that can be assigned to Attribute-s.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValueType')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 499, 2)
    _ElementMap = Type._ElementMap.copy()
    _AttributeMap = Type._AttributeMap.copy()
    # Base type is Type
    
    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element extends (extends) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    
    # Element constraint (constraint) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    
    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Attribute abstract inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ValueType', ValueType)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Attribute with content type ELEMENT_ONLY
class Attribute (Role):
    """
        An Attribute is a Role where the target datatype is a ValueType.
        It represent "simple" properties of its container type, which can be an ObjectType or a DataType.
      
        Must refer to a ValueType.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Attribute')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 651, 2)
    _ElementMap = Role._ElementMap.copy()
    _AttributeMap = Role._AttributeMap.copy()
    # Base type is Role
    
    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element datatype (datatype) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role
    
    # Element multiplicity (multiplicity) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role
    
    # Element subsets (subsets) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role
    
    # Element skosconcept uses Python identifier skosconcept
    __skosconcept = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'skosconcept'), 'skosconcept', '__httpvolute_googlecode_comdmvo_dmlv0_9_Attribute_skosconcept', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 664, 10), )

    
    skosconcept = property(__skosconcept.value, __skosconcept.set, None, '\n                It is possible to assign a SKOSConcept to an attribute definition.\n                This means that the values of the attribute have to comply with the definition of the SKOSConcept.\n                This can be done in two manners. Either the SKOSConcept\n                gives a link to a SKOS vocabulary, in which case the value must be a\n                concept defined in that vocabulary.\n                Or it defines a broadest SKOS concept, in which case the value must be a SKOS concept that is explicitly\n                declared to be (narrower than)\n                that concept, or a concept that is narrower than that concept.\n                The latter definition allows custom SKOS vocabularies to be used.\n                TBD it must be decided HOW the SKOS concept are to be represented as values.\n                By URI? By preferredLabel/en [??] as\n                defined in the vocabulary?\n                Maybe this needs to be part of the SKOSConcept definition.\n              ')

    
    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    _ElementMap.update({
        __skosconcept.name() : __skosconcept
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Attribute', Attribute)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Relation with content type ELEMENT_ONLY
class Relation (Role):
    """
        A relation is a Role where the target datatype is an ObjectType.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Relation')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 720, 2)
    _ElementMap = Role._ElementMap.copy()
    _AttributeMap = Role._AttributeMap.copy()
    # Base type is Role
    
    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element datatype (datatype) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role
    
    # Element multiplicity (multiplicity) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role
    
    # Element subsets (subsets) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role
    
    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Relation', Relation)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}PrimitiveType with content type ELEMENT_ONLY
class PrimitiveType (ValueType):
    """
        Atomic/simple type. Defined by a single value. Generally a built in type from the IVOA profile model,
        or a subclass of one of those types.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PrimitiveType')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 513, 2)
    _ElementMap = ValueType._ElementMap.copy()
    _AttributeMap = ValueType._AttributeMap.copy()
    # Base type is ValueType
    
    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element extends (extends) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    
    # Element constraint (constraint) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    
    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Attribute abstract inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'PrimitiveType', PrimitiveType)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}DataType with content type ELEMENT_ONLY
class DataType (ValueType):
    """Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}DataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataType')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 526, 2)
    _ElementMap = ValueType._ElementMap.copy()
    _AttributeMap = ValueType._AttributeMap.copy()
    # Base type is ValueType
    
    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element extends (extends) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    
    # Element constraint (constraint) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    
    # Element attribute uses Python identifier attribute
    __attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'attribute'), 'attribute', '__httpvolute_googlecode_comdmvo_dmlv0_9_DataType_attribute', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 530, 10), )

    
    attribute = property(__attribute.value, __attribute.set, None, '\n                TODO\n              ')

    
    # Element reference uses Python identifier reference
    __reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reference'), 'reference', '__httpvolute_googlecode_comdmvo_dmlv0_9_DataType_reference', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 537, 10), )

    
    reference = property(__reference.value, __reference.set, None, '\n                TODO\n              ')

    
    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Attribute abstract inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    _ElementMap.update({
        __attribute.name() : __attribute,
        __reference.name() : __reference
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DataType', DataType)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Reference with content type ELEMENT_ONLY
class Reference (Relation):
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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Reference')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 734, 2)
    _ElementMap = Relation._ElementMap.copy()
    _AttributeMap = Relation._AttributeMap.copy()
    # Base type is Relation
    
    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element datatype (datatype) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role
    
    # Element multiplicity (multiplicity) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role
    
    # Element subsets (subsets) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role
    
    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Reference', Reference)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Composition with content type ELEMENT_ONLY
class Composition (Relation):
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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Composition')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 764, 4)
    _ElementMap = Relation._ElementMap.copy()
    _AttributeMap = Relation._AttributeMap.copy()
    # Base type is Relation
    
    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element datatype (datatype) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role
    
    # Element multiplicity (multiplicity) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role
    
    # Element subsets (subsets) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Role
    
    # Element isOrdered uses Python identifier isOrdered
    __isOrdered = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'isOrdered'), 'isOrdered', '__httpvolute_googlecode_comdmvo_dmlv0_9_Composition_isOrdered', False, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 795, 10), )

    
    isOrdered = property(__isOrdered.value, __isOrdered.set, None, '\n                If true, this collection preserves the ordering of object insertions.\n              ')

    
    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    _ElementMap.update({
        __isOrdered.name() : __isOrdered
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Composition', Composition)


# Complex type {http://volute.googlecode.com/dm/vo-dml/v0.9}Enumeration with content type ELEMENT_ONLY
class Enumeration (PrimitiveType):
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
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Enumeration')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 549, 2)
    _ElementMap = PrimitiveType._ElementMap.copy()
    _AttributeMap = PrimitiveType._AttributeMap.copy()
    # Base type is PrimitiveType
    
    # Element vodml_id (vodml-id) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element name (name) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element description (description) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Element extends (extends) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    
    # Element constraint (constraint) inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    
    # Element literal uses Python identifier literal
    __literal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'literal'), 'literal', '__httpvolute_googlecode_comdmvo_dmlv0_9_Enumeration_literal', True, pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 562, 10), )

    
    literal = property(__literal.value, __literal.set, None, '\n                TODO\n              ')

    
    # Attribute id inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}ReferableElement
    
    # Attribute abstract inherited from {http://volute.googlecode.com/dm/vo-dml/v0.9}Type
    _ElementMap.update({
        __literal.name() : __literal
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Enumeration', Enumeration)


model = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'model'), Model, documentation="\n        Every VO-DML/XML document must start with a 'model' element, no other root elements are supported by this spec.\n      ", location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 855, 2))
Namespace.addCategoryObject('elementBinding', model.name().localName(), model)



ReferableElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vodml-id'), VODMLID, scope=ReferableElement, documentation='\n              Identifier for its containing element.\n              Extracted as a separate type so that we can easily adapt to a different identifier design.\n          ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6)))

ReferableElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), STD_ANON, scope=ReferableElement, documentation='\n            The name of the model element. \n            MUST NOT be an empty string.\n          ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6)))

ReferableElement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=ReferableElement, documentation='\n            Human readable description of the model element.\n          ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReferableElement._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-id')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferableElement._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReferableElement._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
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
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReferableElement._Automaton = _BuildAutomaton()




ElementRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vodml-ref'), VODMLREF, scope=ElementRef, documentation='\n            The element identifying the referenced target element.\n            See the documentation for the VODMLREF type.\n          ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 156, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ElementRef._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-ref')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 156, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ElementRef._Automaton = _BuildAutomaton_()




Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), ModelName, scope=Model, documentation='\n                        Short name of the model.\n                        NOTE this name MUST be used as prefix in any utype reference to elements in this model.\n                    ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 179, 12)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=Model, documentation='\n                        The description of the model.\n                    ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 187, 12)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'title'), pyxb.binding.datatypes.string, scope=Model, documentation='\n              The title of the model by which it is officially known.\n          ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 194, 12)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'author'), pyxb.binding.datatypes.string, scope=Model, documentation='\n                    List of authors of the model, only defined by name so far.\n            TBD could be expanded with email, affiliation and so on.\n          ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 201, 12)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'version'), pyxb.binding.datatypes.string, scope=Model, documentation='\n            Label giving the version of the model.\n          ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 209, 6)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'previousVersion'), pyxb.binding.datatypes.anyURI, scope=Model, documentation='\n            URI identifying a VO-DML model that is the version from which the current version of model is derived.\n            TBD could be an IVO Identifier once models get properly registered?\n          ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 216, 6)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lastModified'), pyxb.binding.datatypes.dateTime, scope=Model, documentation='\n            Timestamp when the last change to the current model was made.\n          ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 224, 6)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'import'), ModelImport, scope=Model, documentation="\n            An 'import' element indicates a dependency on an external, predefined VO-DML data model.\n            Types from that model may be used for referencing, extension and assignment to\n            attributes.\n            Types from the external model MUST NOT be used for\n            composition relationships.\n            'identification' relations to elements from that model may be used to indicate some kind of\n            equivalence between\n            elements in the current model and the external elements.\n          \n            TBD We might require that every data model MUST include a version of the IVOA data model\n            to gain access to the standard\n            primitive types and some other types.\n            We may require that that standard model should be included *completely*,\n            i.e. including all its type definitions explicitly.\n            This would be similar to treating it as a UML Profile, rather than an import.\n            This would mean that the most common type assignments for attributes\n            can be checked within the model and not require\n            importing the remote model during validation.\n          ", location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 231, 6)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'primitiveType'), PrimitiveType, scope=Model, documentation='\n                        Collection of PrimitiveType definitions directly under the model, i.e. not contained in a\n                        Package.\n                    ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 256, 12)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'enumeration'), Enumeration, scope=Model, documentation='\n                        Collection of Enumeration definitions directly under the model, i.e. not contained in a Package.\n                    ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 264, 12)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dataType'), DataType, scope=Model, documentation='\n                        Collection of DataType definitions directly under the model, i.e. not contained in a Package.\n                    ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 271, 12)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'objectType'), ObjectType, scope=Model, documentation='\n                        Collection of ObjectType definitions directly under the model, i.e. not contained in a Package.\n                    ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 278, 12)))

Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'package'), Package, scope=Model, documentation='\n                        The collection of packages which can contain further detailed name spacing to\n                        the type definitions in the model.\n                    ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 285, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 187, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 201, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 216, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 231, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 256, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 264, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 271, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 278, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 285, 12))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 179, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 187, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, 'title')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 194, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, 'author')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 201, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, 'version')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 209, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, 'previousVersion')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 216, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, 'lastModified')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 224, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, 'import')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 231, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, 'primitiveType')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 256, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, 'enumeration')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 264, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, 'dataType')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 271, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, 'objectType')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 278, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, 'package')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 285, 12))
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
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
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
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Model._Automaton = _BuildAutomaton_2()




ModelImport._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), ModelName, scope=ModelImport, documentation="\n                    Name by which imported model is used in the current model and its documentation.\n                    This name MUST be the same as the 'name' of the model definition in that remote document.\n                    For all utypes pointing to elements in the imported model MUST use this name as prefix.\n                ", location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 307, 8)))

ModelImport._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'version'), pyxb.binding.datatypes.string, scope=ModelImport, documentation='\n                    Version of the imported model.\n                ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 316, 8)))

ModelImport._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'url'), pyxb.binding.datatypes.anyURI, scope=ModelImport, documentation='\n            URL from which the VO-DML model document can be downloaded.\n            Note, could likely be done through a registry once ivoId is known.\n            TBD SHOULD this be a generic URI, or can we insits on URL?\n          ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 323, 6)))

ModelImport._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'documentationURL'), pyxb.binding.datatypes.anyURI, scope=ModelImport, documentation='\n            URL where a documentation HTML file for the remote model can be downloaded.\n            This SHOULD be a document that contains anchors for each element thta has as name attribute the vodml-id of that element.\n            I.e. it is assumed that the\n            vodml-id-s of the imported types can be added onto this documentationURL\n            (should end with a #?) so that a direct link to the documentation for a referenced data model element can be found.\n          ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 332, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 316, 8))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModelImport._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 307, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModelImport._UseForTag(pyxb.namespace.ExpandedName(None, 'version')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 316, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModelImport._UseForTag(pyxb.namespace.ExpandedName(None, 'url')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 323, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ModelImport._UseForTag(pyxb.namespace.ExpandedName(None, 'documentationURL')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 332, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ModelImport._Automaton = _BuildAutomaton_3()




SKOSConcept._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'broadestSKOSConcept'), pyxb.binding.datatypes.anyURI, scope=SKOSConcept, documentation='\n            A URI identifiying a SKOS concept that corresponds to the concept in the model.\n            Values of a corresponding attributes must be URI-s identifiying objects that are narrower\n            than the identified concept. This attribute may be null as\n            certain vocabularies may not have a\n          ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 699, 6)))

SKOSConcept._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vocabularyURI'), pyxb.binding.datatypes.anyURI, scope=SKOSConcept, documentation='\n            If no broadestSKOSConcept is defined, one or more explicit vocabularies can be provided from which the\n            value must be obtained.\n          ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 709, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 699, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 709, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SKOSConcept._UseForTag(pyxb.namespace.ExpandedName(None, 'broadestSKOSConcept')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 699, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SKOSConcept._UseForTag(pyxb.namespace.ExpandedName(None, 'vocabularyURI')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 709, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SKOSConcept._Automaton = _BuildAutomaton_4()




Multiplicity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'minOccurs'), pyxb.binding.datatypes.nonNegativeInteger, scope=Multiplicity, documentation='\n          Lower bound on number of instances/values.\n          ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 818, 6), unicode_default='1'))

Multiplicity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'maxOccurs'), pyxb.binding.datatypes.int, scope=Multiplicity, documentation='\n          When negative, unbounded.\n          ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 825, 6), unicode_default='1'))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Multiplicity._UseForTag(pyxb.namespace.ExpandedName(None, 'minOccurs')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 818, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Multiplicity._UseForTag(pyxb.namespace.ExpandedName(None, 'maxOccurs')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 825, 6))
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




Package._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'primitiveType'), PrimitiveType, scope=Package, documentation='\n                                Collection of PrimitiveType-s defined in this package.\n                            ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 374, 20)))

Package._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'enumeration'), Enumeration, scope=Package, documentation='\n                                Collection of Enumeration-s defined in this package.\n                            ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 381, 20)))

Package._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dataType'), DataType, scope=Package, documentation='\n                                Collection of DataType-s defined in this package.\n                            ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 388, 20)))

Package._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'objectType'), ObjectType, scope=Package, documentation='\n                                Collection of ObjectType-s defined in this package.\n                            ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 395, 20)))

Package._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'package'), Package, scope=Package, documentation='\n                                Collection of child Package-s defined in this package.\n                            ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 402, 20)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 374, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 381, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 388, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 395, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 402, 20))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-id')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, 'primitiveType')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 374, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, 'enumeration')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 381, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, 'dataType')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 388, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, 'objectType')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 395, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Package._UseForTag(pyxb.namespace.ExpandedName(None, 'package')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 402, 20))
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
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Package._Automaton = _BuildAutomaton_6()




Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'extends'), ElementRef, scope=Type, documentation="\n                Reference to a type (called the base-type) that is extended by the current type (called the subtype).\n                This implements the typical is-a inheritance relationship, similar to the extends relations in XSD and Java,\n                the\n                generaliation in UML, or the subclassOf relation in RDF. Note, VO-DML does not support multiple inheritance.\n                Instances of a subtype are automatic instances of a base type.\n                Polymorphism is assumed: When a role (see below) defines a base type\n                as its datatype, instances of any subtype\n                can be uased as value of the role.\n                Roles defined on a base type are inherited by the subtypes.\n                Relations inherited from a basetype can be 'subsetted', which is similar to overriding their definition.\n                See the definiton of this property on the Relation type.\n              ", location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 431, 10)))

Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'constraint'), Constraint, scope=Type, documentation='\n                        Constraints defining valid instances of the type.\n                        May be an AttributeConstraint or an expression in some language.\n                    ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 448, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 431, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 448, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Type._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-id')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Type._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Type._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Type._UseForTag(pyxb.namespace.ExpandedName(None, 'extends')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 431, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Type._UseForTag(pyxb.namespace.ExpandedName(None, 'constraint')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 448, 12))
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
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Type._Automaton = _BuildAutomaton_7()




def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EnumLiteral._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-id')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EnumLiteral._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EnumLiteral._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
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
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EnumLiteral._Automaton = _BuildAutomaton_8()




Role._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'datatype'), ElementRef, scope=Role, documentation='\n                Reference to the type that plays the role represented by this Role.\n              ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 609, 10)))

Role._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'multiplicity'), Multiplicity, scope=Role, documentation='\n                The multiplicity of the role (also called cardinality) indicates whether it must have a\n                value or may be without value, or possibly how many values are allowed.\n              ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 616, 10)))

Role._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'subsets'), ElementRef, scope=Role, documentation='\n                Represents the UML subsetted property. Indicates that a particular relation refines the definition\n                of another relation. ONly a relation inherited form a base class can\n                be subsetted. Typical usage is\n                that the base class has a\n                relation to a class A, and the subclass refines this to indicating that\n                the relation should be to a subclass of A.\n\n                The value should identify the subsetted property.\n                TBD IF we are going to use utype-s to refer to elements also inside this\n                document, we should use an\n                appropriate keyref\n              \n                TBD this is a somewhat abstract, but very useful modeling concept.\n                It implements a very common modeling design pattern.\n                It exists in UML2.\n              ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 624, 10)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 624, 10))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Role._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-id')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Role._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Role._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Role._UseForTag(pyxb.namespace.ExpandedName(None, 'datatype')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 609, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Role._UseForTag(pyxb.namespace.ExpandedName(None, 'multiplicity')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 616, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Role._UseForTag(pyxb.namespace.ExpandedName(None, 'subsets')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 624, 10))
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
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
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
        fac.UpdateInstruction(cc_1, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Role._Automaton = _BuildAutomaton_9()




def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Constraint._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-id')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Constraint._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Constraint._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
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
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Constraint._Automaton = _BuildAutomaton_10()




ObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'attribute'), Attribute, scope=ObjectType, documentation='\n                TODO\n              ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 472, 10)))

ObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'collection'), Composition, scope=ObjectType, documentation='\n                TODO\n              ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 479, 12)))

ObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reference'), Reference, scope=ObjectType, documentation='\n                TODO\n              ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 486, 10)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 431, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 448, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 472, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 479, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 486, 10))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-id')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'extends')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 431, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'constraint')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 448, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'attribute')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 472, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'collection')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 479, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ObjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'reference')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 486, 10))
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
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ObjectType._Automaton = _BuildAutomaton_11()




def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 431, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 448, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueType._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-id')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ValueType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ValueType._UseForTag(pyxb.namespace.ExpandedName(None, 'extends')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 431, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ValueType._UseForTag(pyxb.namespace.ExpandedName(None, 'constraint')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 448, 12))
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
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ValueType._Automaton = _BuildAutomaton_12()




Attribute._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'skosconcept'), SKOSConcept, scope=Attribute, documentation='\n                It is possible to assign a SKOSConcept to an attribute definition.\n                This means that the values of the attribute have to comply with the definition of the SKOSConcept.\n                This can be done in two manners. Either the SKOSConcept\n                gives a link to a SKOS vocabulary, in which case the value must be a\n                concept defined in that vocabulary.\n                Or it defines a broadest SKOS concept, in which case the value must be a SKOS concept that is explicitly\n                declared to be (narrower than)\n                that concept, or a concept that is narrower than that concept.\n                The latter definition allows custom SKOS vocabularies to be used.\n                TBD it must be decided HOW the SKOS concept are to be represented as values.\n                By URI? By preferredLabel/en [??] as\n                defined in the vocabulary?\n                Maybe this needs to be part of the SKOSConcept definition.\n              ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 664, 10)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 624, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 664, 10))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Attribute._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-id')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Attribute._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Attribute._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Attribute._UseForTag(pyxb.namespace.ExpandedName(None, 'datatype')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 609, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Attribute._UseForTag(pyxb.namespace.ExpandedName(None, 'multiplicity')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 616, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Attribute._UseForTag(pyxb.namespace.ExpandedName(None, 'subsets')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 624, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Attribute._UseForTag(pyxb.namespace.ExpandedName(None, 'skosconcept')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 664, 10))
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
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
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
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Attribute._Automaton = _BuildAutomaton_13()




def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 624, 10))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relation._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-id')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relation._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relation._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relation._UseForTag(pyxb.namespace.ExpandedName(None, 'datatype')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 609, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Relation._UseForTag(pyxb.namespace.ExpandedName(None, 'multiplicity')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 616, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Relation._UseForTag(pyxb.namespace.ExpandedName(None, 'subsets')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 624, 10))
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
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
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
        fac.UpdateInstruction(cc_1, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Relation._Automaton = _BuildAutomaton_14()




def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 431, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 448, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PrimitiveType._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-id')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PrimitiveType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PrimitiveType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PrimitiveType._UseForTag(pyxb.namespace.ExpandedName(None, 'extends')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 431, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PrimitiveType._UseForTag(pyxb.namespace.ExpandedName(None, 'constraint')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 448, 12))
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
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PrimitiveType._Automaton = _BuildAutomaton_15()




DataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'attribute'), Attribute, scope=DataType, documentation='\n                TODO\n              ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 530, 10)))

DataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reference'), Reference, scope=DataType, documentation='\n                TODO\n              ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 537, 10)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 431, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 448, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 530, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 537, 10))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-id')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(None, 'extends')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 431, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(None, 'constraint')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 448, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(None, 'attribute')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 530, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DataType._UseForTag(pyxb.namespace.ExpandedName(None, 'reference')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 537, 10))
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
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DataType._Automaton = _BuildAutomaton_16()




def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 624, 10))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-id')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, 'datatype')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 609, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, 'multiplicity')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 616, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Reference._UseForTag(pyxb.namespace.ExpandedName(None, 'subsets')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 624, 10))
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
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
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
        fac.UpdateInstruction(cc_1, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Reference._Automaton = _BuildAutomaton_17()




Composition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'isOrdered'), pyxb.binding.datatypes.boolean, scope=Composition, documentation='\n                If true, this collection preserves the ordering of object insertions.\n              ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 795, 10), unicode_default='false'))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 624, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 795, 10))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-id')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, 'datatype')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 609, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, 'multiplicity')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 616, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, 'subsets')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 624, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Composition._UseForTag(pyxb.namespace.ExpandedName(None, 'isOrdered')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 795, 10))
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
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
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
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Composition._Automaton = _BuildAutomaton_18()




Enumeration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'literal'), EnumLiteral, scope=Enumeration, documentation='\n                TODO\n              ', location=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 562, 10)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 431, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 448, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Enumeration._UseForTag(pyxb.namespace.ExpandedName(None, 'vodml-id')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 100, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Enumeration._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Enumeration._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Enumeration._UseForTag(pyxb.namespace.ExpandedName(None, 'extends')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 431, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Enumeration._UseForTag(pyxb.namespace.ExpandedName(None, 'constraint')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 448, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Enumeration._UseForTag(pyxb.namespace.ExpandedName(None, 'literal')), pyxb.utils.utility.Location('c:\\Users\\Omar\\PycharmProjects\\volib\\volib\\resources\\vo-dml.xsd', 562, 10))
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
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Enumeration._Automaton = _BuildAutomaton_19()

