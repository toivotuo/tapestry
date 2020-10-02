# ./separouting_v3.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2020-10-02 23:04:43.608390 by PyXB version 1.2.6 using Python 3.7.3.final.0
# Namespace AbsentNamespace0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:833f3298-04ea-11eb-afa2-04d3b0c539f1')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
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


# Atomic simple type: filetypeType
class filetypeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'filetypeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 6, 0)
    _Documentation = None
filetypeType._CF_pattern = pyxb.binding.facets.CF_pattern()
filetypeType._CF_pattern.addPattern(pattern='full|delta')
filetypeType._InitializeFacetMap(filetypeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'filetypeType', filetypeType)
_module_typeBindings.filetypeType = filetypeType

# Atomic simple type: modification_flagType
class modification_flagType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'modification_flagType')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 11, 0)
    _Documentation = None
modification_flagType._CF_pattern = pyxb.binding.facets.CF_pattern()
modification_flagType._CF_pattern.addPattern(pattern='A|M|D')
modification_flagType._InitializeFacetMap(modification_flagType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'modification_flagType', modification_flagType)
_module_typeBindings.modification_flagType = modification_flagType

# Atomic simple type: bicType
class bicType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'bicType')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 16, 0)
    _Documentation = None
bicType._CF_pattern = pyxb.binding.facets.CF_pattern()
bicType._CF_pattern.addPattern(pattern='[0-9A-Z]{11}')
bicType._InitializeFacetMap(bicType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'bicType', bicType)
_module_typeBindings.bicType = bicType

# Atomic simple type: dateType
class dateType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dateType')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 21, 0)
    _Documentation = None
dateType._CF_pattern = pyxb.binding.facets.CF_pattern()
dateType._CF_pattern.addPattern(pattern='[0-9]{8}')
dateType._InitializeFacetMap(dateType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'dateType', dateType)
_module_typeBindings.dateType = dateType

# Atomic simple type: iso_country_codeType
class iso_country_codeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'iso_country_codeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 26, 0)
    _Documentation = None
iso_country_codeType._CF_pattern = pyxb.binding.facets.CF_pattern()
iso_country_codeType._CF_pattern.addPattern(pattern='[A-Z]{2}')
iso_country_codeType._InitializeFacetMap(iso_country_codeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'iso_country_codeType', iso_country_codeType)
_module_typeBindings.iso_country_codeType = iso_country_codeType

# Atomic simple type: sp_record_keyType
class sp_record_keyType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sp_record_keyType')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 32, 0)
    _Documentation = None
sp_record_keyType._CF_pattern = pyxb.binding.facets.CF_pattern()
sp_record_keyType._CF_pattern.addPattern(pattern='SP[0-9A-Z]{10}')
sp_record_keyType._InitializeFacetMap(sp_record_keyType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'sp_record_keyType', sp_record_keyType)
_module_typeBindings.sp_record_keyType = sp_record_keyType

# Atomic simple type: schemeType
class schemeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'schemeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 37, 0)
    _Documentation = None
schemeType._CF_pattern = pyxb.binding.facets.CF_pattern()
schemeType._CF_pattern.addPattern(pattern='SCT|SDD B2B|SDD CORE')
schemeType._InitializeFacetMap(schemeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'schemeType', schemeType)
_module_typeBindings.schemeType = schemeType

# Atomic simple type: preferredType
class preferredType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'preferredType')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 42, 0)
    _Documentation = None
preferredType._CF_pattern = pyxb.binding.facets.CF_pattern()
preferredType._CF_pattern.addPattern(pattern='P')
preferredType._InitializeFacetMap(preferredType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'preferredType', preferredType)
_module_typeBindings.preferredType = preferredType

# Atomic simple type: reachabilityType
class reachabilityType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'reachabilityType')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 47, 0)
    _Documentation = None
reachabilityType._CF_pattern = pyxb.binding.facets.CF_pattern()
reachabilityType._CF_pattern.addPattern(pattern='D|I')
reachabilityType._InitializeFacetMap(reachabilityType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'reachabilityType', reachabilityType)
_module_typeBindings.reachabilityType = reachabilityType

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 84, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element modification_flag uses Python identifier modification_flag
    __modification_flag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'modification_flag'), 'modification_flag', '__AbsentNamespace0_CTD_ANON_modification_flag', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 54, 0), )

    
    modification_flag = property(__modification_flag.value, __modification_flag.set, None, None)

    
    # Element record_key uses Python identifier record_key
    __record_key = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'record_key'), 'record_key', '__AbsentNamespace0_CTD_ANON_record_key', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 55, 0), )

    
    record_key = property(__record_key.value, __record_key.set, None, None)

    
    # Element bic uses Python identifier bic
    __bic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bic'), 'bic', '__AbsentNamespace0_CTD_ANON_bic', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 56, 0), )

    
    bic = property(__bic.value, __bic.set, None, None)

    
    # Element institution_name uses Python identifier institution_name
    __institution_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'institution_name'), 'institution_name', '__AbsentNamespace0_CTD_ANON_institution_name', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 57, 0), )

    
    institution_name = property(__institution_name.value, __institution_name.set, None, None)

    
    # Element city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__AbsentNamespace0_CTD_ANON_city', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 58, 0), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element iso_country_code uses Python identifier iso_country_code
    __iso_country_code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'iso_country_code'), 'iso_country_code', '__AbsentNamespace0_CTD_ANON_iso_country_code', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 59, 0), )

    
    iso_country_code = property(__iso_country_code.value, __iso_country_code.set, None, None)

    
    # Element scheme uses Python identifier scheme
    __scheme = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scheme'), 'scheme', '__AbsentNamespace0_CTD_ANON_scheme', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 60, 0), )

    
    scheme = property(__scheme.value, __scheme.set, None, None)

    
    # Element adherence_bic uses Python identifier adherence_bic
    __adherence_bic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'adherence_bic'), 'adherence_bic', '__AbsentNamespace0_CTD_ANON_adherence_bic', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 61, 0), )

    
    adherence_bic = property(__adherence_bic.value, __adherence_bic.set, None, None)

    
    # Element adherence_start_date uses Python identifier adherence_start_date
    __adherence_start_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'adherence_start_date'), 'adherence_start_date', '__AbsentNamespace0_CTD_ANON_adherence_start_date', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 62, 0), )

    
    adherence_start_date = property(__adherence_start_date.value, __adherence_start_date.set, None, None)

    
    # Element adherence_stop_date uses Python identifier adherence_stop_date
    __adherence_stop_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'adherence_stop_date'), 'adherence_stop_date', '__AbsentNamespace0_CTD_ANON_adherence_stop_date', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 63, 0), )

    
    adherence_stop_date = property(__adherence_stop_date.value, __adherence_stop_date.set, None, None)

    
    # Element payment_channel_id uses Python identifier payment_channel_id
    __payment_channel_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'payment_channel_id'), 'payment_channel_id', '__AbsentNamespace0_CTD_ANON_payment_channel_id', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 64, 0), )

    
    payment_channel_id = property(__payment_channel_id.value, __payment_channel_id.set, None, None)

    
    # Element preferred_channel_flag uses Python identifier preferred_channel_flag
    __preferred_channel_flag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'preferred_channel_flag'), 'preferred_channel_flag', '__AbsentNamespace0_CTD_ANON_preferred_channel_flag', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 65, 0), )

    
    preferred_channel_flag = property(__preferred_channel_flag.value, __preferred_channel_flag.set, None, None)

    
    # Element reachability uses Python identifier reachability
    __reachability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reachability'), 'reachability', '__AbsentNamespace0_CTD_ANON_reachability', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 66, 0), )

    
    reachability = property(__reachability.value, __reachability.set, None, None)

    
    # Element intermediary_institution_bic uses Python identifier intermediary_institution_bic
    __intermediary_institution_bic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'intermediary_institution_bic'), 'intermediary_institution_bic', '__AbsentNamespace0_CTD_ANON_intermediary_institution_bic', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 67, 0), )

    
    intermediary_institution_bic = property(__intermediary_institution_bic.value, __intermediary_institution_bic.set, None, None)

    
    # Element start_date uses Python identifier start_date
    __start_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'start_date'), 'start_date', '__AbsentNamespace0_CTD_ANON_start_date', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 68, 0), )

    
    start_date = property(__start_date.value, __start_date.set, None, None)

    
    # Element stop_date uses Python identifier stop_date
    __stop_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stop_date'), 'stop_date', '__AbsentNamespace0_CTD_ANON_stop_date', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 69, 0), )

    
    stop_date = property(__stop_date.value, __stop_date.set, None, None)

    
    # Element aos uses Python identifier aos
    __aos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'aos'), 'aos', '__AbsentNamespace0_CTD_ANON_aos', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 70, 0), )

    
    aos = property(__aos.value, __aos.set, None, None)

    
    # Element field_a uses Python identifier field_a
    __field_a = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'field_a'), 'field_a', '__AbsentNamespace0_CTD_ANON_field_a', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 71, 0), )

    
    field_a = property(__field_a.value, __field_a.set, None, None)

    
    # Element field_b uses Python identifier field_b
    __field_b = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'field_b'), 'field_b', '__AbsentNamespace0_CTD_ANON_field_b', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 72, 0), )

    
    field_b = property(__field_b.value, __field_b.set, None, None)

    _ElementMap.update({
        __modification_flag.name() : __modification_flag,
        __record_key.name() : __record_key,
        __bic.name() : __bic,
        __institution_name.name() : __institution_name,
        __city.name() : __city,
        __iso_country_code.name() : __iso_country_code,
        __scheme.name() : __scheme,
        __adherence_bic.name() : __adherence_bic,
        __adherence_start_date.name() : __adherence_start_date,
        __adherence_stop_date.name() : __adherence_stop_date,
        __payment_channel_id.name() : __payment_channel_id,
        __preferred_channel_flag.name() : __preferred_channel_flag,
        __reachability.name() : __reachability,
        __intermediary_institution_bic.name() : __intermediary_institution_bic,
        __start_date.name() : __start_date,
        __stop_date.name() : __stop_date,
        __aos.name() : __aos,
        __field_a.name() : __field_a,
        __field_b.name() : __field_b
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 81, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element separouting_v3 uses Python identifier separouting_v3
    __separouting_v3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'separouting_v3'), 'separouting_v3', '__AbsentNamespace0_CTD_ANON__separouting_v3', True, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 83, 3), )

    
    separouting_v3 = property(__separouting_v3.value, __separouting_v3.set, None, None)

    
    # Attribute product uses Python identifier product
    __product = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'product'), 'product', '__AbsentNamespace0_CTD_ANON__product', pyxb.binding.datatypes.string, required=True)
    __product._DeclarationLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 75, 0)
    __product._UseLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 109, 2)
    
    product = property(__product.value, __product.set, None, None)

    
    # Attribute filetype uses Python identifier filetype
    __filetype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'filetype'), 'filetype', '__AbsentNamespace0_CTD_ANON__filetype', _module_typeBindings.filetypeType, required=True)
    __filetype._DeclarationLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 76, 0)
    __filetype._UseLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 110, 2)
    
    filetype = property(__filetype.value, __filetype.set, None, None)

    
    # Attribute filedate uses Python identifier filedate
    __filedate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, 'filedate'), 'filedate', '__AbsentNamespace0_CTD_ANON__filedate', _module_typeBindings.dateType, required=True)
    __filedate._DeclarationLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 77, 0)
    __filedate._UseLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 111, 2)
    
    filedate = property(__filedate.value, __filedate.set, None, None)

    _ElementMap.update({
        __separouting_v3.name() : __separouting_v3
    })
    _AttributeMap.update({
        __product.name() : __product,
        __filetype.name() : __filetype,
        __filedate.name() : __filedate
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


institution_name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'institution_name'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 57, 0))
Namespace.addCategoryObject('elementBinding', institution_name.name().localName(), institution_name)

city = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 58, 0))
Namespace.addCategoryObject('elementBinding', city.name().localName(), city)

payment_channel_id = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'payment_channel_id'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 64, 0))
Namespace.addCategoryObject('elementBinding', payment_channel_id.name().localName(), payment_channel_id)

aos = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aos'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 70, 0))
Namespace.addCategoryObject('elementBinding', aos.name().localName(), aos)

field_a = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'field_a'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 71, 0))
Namespace.addCategoryObject('elementBinding', field_a.name().localName(), field_a)

field_b = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'field_b'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 72, 0))
Namespace.addCategoryObject('elementBinding', field_b.name().localName(), field_b)

modification_flag = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'modification_flag'), modification_flagType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 54, 0))
Namespace.addCategoryObject('elementBinding', modification_flag.name().localName(), modification_flag)

record_key = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'record_key'), sp_record_keyType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 55, 0))
Namespace.addCategoryObject('elementBinding', record_key.name().localName(), record_key)

bic = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bic'), bicType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 56, 0))
Namespace.addCategoryObject('elementBinding', bic.name().localName(), bic)

iso_country_code = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'iso_country_code'), iso_country_codeType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 59, 0))
Namespace.addCategoryObject('elementBinding', iso_country_code.name().localName(), iso_country_code)

scheme = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheme'), schemeType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 60, 0))
Namespace.addCategoryObject('elementBinding', scheme.name().localName(), scheme)

adherence_bic = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'adherence_bic'), bicType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 61, 0))
Namespace.addCategoryObject('elementBinding', adherence_bic.name().localName(), adherence_bic)

adherence_start_date = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'adherence_start_date'), dateType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 62, 0))
Namespace.addCategoryObject('elementBinding', adherence_start_date.name().localName(), adherence_start_date)

adherence_stop_date = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'adherence_stop_date'), dateType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 63, 0))
Namespace.addCategoryObject('elementBinding', adherence_stop_date.name().localName(), adherence_stop_date)

preferred_channel_flag = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'preferred_channel_flag'), preferredType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 65, 0))
Namespace.addCategoryObject('elementBinding', preferred_channel_flag.name().localName(), preferred_channel_flag)

reachability = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reachability'), reachabilityType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 66, 0))
Namespace.addCategoryObject('elementBinding', reachability.name().localName(), reachability)

intermediary_institution_bic = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'intermediary_institution_bic'), bicType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 67, 0))
Namespace.addCategoryObject('elementBinding', intermediary_institution_bic.name().localName(), intermediary_institution_bic)

start_date = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'start_date'), dateType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 68, 0))
Namespace.addCategoryObject('elementBinding', start_date.name().localName(), start_date)

stop_date = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stop_date'), dateType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 69, 0))
Namespace.addCategoryObject('elementBinding', stop_date.name().localName(), stop_date)

dataexport = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dataexport'), CTD_ANON_, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 80, 0))
Namespace.addCategoryObject('elementBinding', dataexport.name().localName(), dataexport)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'modification_flag'), modification_flagType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 54, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'record_key'), sp_record_keyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 55, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bic'), bicType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 56, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'institution_name'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 57, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 58, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'iso_country_code'), iso_country_codeType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 59, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheme'), schemeType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 60, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'adherence_bic'), bicType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 61, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'adherence_start_date'), dateType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 62, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'adherence_stop_date'), dateType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 63, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'payment_channel_id'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 64, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'preferred_channel_flag'), preferredType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 65, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reachability'), reachabilityType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 66, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'intermediary_institution_bic'), bicType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 67, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'start_date'), dateType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 68, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stop_date'), dateType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 69, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'aos'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 70, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'field_a'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 71, 0)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'field_b'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 72, 0)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 90, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 93, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 94, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 95, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 97, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 98, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 99, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 100, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 101, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 102, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 103, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 104, 6))
    counters.add(cc_11)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'modification_flag')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 86, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'record_key')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 87, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bic')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 88, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'institution_name')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 89, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'city')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 90, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'iso_country_code')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 91, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheme')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 92, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'adherence_bic')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 93, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'adherence_start_date')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 94, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'adherence_stop_date')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 95, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'payment_channel_id')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 96, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'preferred_channel_flag')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 97, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reachability')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 98, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'intermediary_institution_bic')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 99, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'start_date')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 100, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stop_date')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 101, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'aos')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 102, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'field_a')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 103, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'field_b')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 104, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'separouting_v3'), CTD_ANON, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 83, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'separouting_v3')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/separouting_v3.xsd', 83, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()

