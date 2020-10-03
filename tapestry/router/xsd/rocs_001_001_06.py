# ./rocs_001_001_06.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:773c90f497e436d1d77c516158a28d04643e1370
# Generated 2020-10-03 21:24:26.794283 by PyXB version 1.2.6 using Python 3.7.3.final.0
# Namespace urn:rocs.001.001.06

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:ab5b1f2e-05a5-11eb-afa2-04d3b0c539f1')

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
Namespace = pyxb.namespace.NamespaceForURI('urn:rocs.001.001.06', create_if_missing=True)
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


# Atomic simple type: {urn:rocs.001.001.06}AnyBICIdentifier
class AnyBICIdentifier (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnyBICIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 7, 2)
    _Documentation = None
AnyBICIdentifier._CF_pattern = pyxb.binding.facets.CF_pattern()
AnyBICIdentifier._CF_pattern.addPattern(pattern='[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}')
AnyBICIdentifier._InitializeFacetMap(AnyBICIdentifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'AnyBICIdentifier', AnyBICIdentifier)
_module_typeBindings.AnyBICIdentifier = AnyBICIdentifier

# Atomic simple type: {urn:rocs.001.001.06}CountryCode
class CountryCode (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CountryCode')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 17, 2)
    _Documentation = None
CountryCode._CF_pattern = pyxb.binding.facets.CF_pattern()
CountryCode._CF_pattern.addPattern(pattern='[A-Z]{2,2}')
CountryCode._InitializeFacetMap(CountryCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CountryCode', CountryCode)
_module_typeBindings.CountryCode = CountryCode

# Atomic simple type: {urn:rocs.001.001.06}CurrencyAndAmount_SimpleType
class CurrencyAndAmount_SimpleType (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrencyAndAmount_SimpleType')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 35, 2)
    _Documentation = None
CurrencyAndAmount_SimpleType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=CurrencyAndAmount_SimpleType, value=pyxb.binding.datatypes.decimal('0.0'))
CurrencyAndAmount_SimpleType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
CurrencyAndAmount_SimpleType._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(5))
CurrencyAndAmount_SimpleType._InitializeFacetMap(CurrencyAndAmount_SimpleType._CF_minInclusive,
   CurrencyAndAmount_SimpleType._CF_totalDigits,
   CurrencyAndAmount_SimpleType._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'CurrencyAndAmount_SimpleType', CurrencyAndAmount_SimpleType)
_module_typeBindings.CurrencyAndAmount_SimpleType = CurrencyAndAmount_SimpleType

# Atomic simple type: {urn:rocs.001.001.06}CurrencyCode
class CurrencyCode (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrencyCode')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 42, 2)
    _Documentation = None
CurrencyCode._CF_pattern = pyxb.binding.facets.CF_pattern()
CurrencyCode._CF_pattern.addPattern(pattern='[A-Z]{3,3}')
CurrencyCode._InitializeFacetMap(CurrencyCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CurrencyCode', CurrencyCode)
_module_typeBindings.CurrencyCode = CurrencyCode

# Atomic simple type: {urn:rocs.001.001.06}ISODateTime
class ISODateTime (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ISODateTime')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 87, 2)
    _Documentation = None
ISODateTime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ISODateTime', ISODateTime)
_module_typeBindings.ISODateTime = ISODateTime

# Atomic simple type: {urn:rocs.001.001.06}ISOTime
class ISOTime (pyxb.binding.datatypes.time):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ISOTime')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 90, 2)
    _Documentation = None
ISOTime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ISOTime', ISOTime)
_module_typeBindings.ISOTime = ISOTime

# Atomic simple type: {urn:rocs.001.001.06}Max140Text
class Max140Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max140Text')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 107, 2)
    _Documentation = None
Max140Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max140Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(140))
Max140Text._InitializeFacetMap(Max140Text._CF_minLength,
   Max140Text._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'Max140Text', Max140Text)
_module_typeBindings.Max140Text = Max140Text

# Atomic simple type: {urn:rocs.001.001.06}Max16Text
class Max16Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max16Text')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 113, 2)
    _Documentation = None
Max16Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max16Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16))
Max16Text._InitializeFacetMap(Max16Text._CF_minLength,
   Max16Text._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'Max16Text', Max16Text)
_module_typeBindings.Max16Text = Max16Text

# Atomic simple type: {urn:rocs.001.001.06}Max35Text
class Max35Text (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max35Text')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 119, 2)
    _Documentation = None
Max35Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max35Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
Max35Text._InitializeFacetMap(Max35Text._CF_minLength,
   Max35Text._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'Max35Text', Max35Text)
_module_typeBindings.Max35Text = Max35Text

# Complex type {urn:rocs.001.001.06}AOSList with content type ELEMENT_ONLY
class AOSList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}AOSList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AOSList')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 12, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}AOSId uses Python identifier AOSId
    __AOSId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AOSId'), 'AOSId', '__urnrocs_001_001_06_AOSList_urnrocs_001_001_06AOSId', True, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 14, 6), )

    
    AOSId = property(__AOSId.value, __AOSId.set, None, None)

    _ElementMap.update({
        __AOSId.name() : __AOSId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AOSList = AOSList
Namespace.addCategoryObject('typeBinding', 'AOSList', AOSList)


# Complex type {urn:rocs.001.001.06}CSMIdentifier with content type ELEMENT_ONLY
class CSMIdentifier (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}CSMIdentifier with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CSMIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 22, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}PtyId uses Python identifier PtyId
    __PtyId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PtyId'), 'PtyId', '__urnrocs_001_001_06_CSMIdentifier_urnrocs_001_001_06PtyId', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 24, 6), )

    
    PtyId = property(__PtyId.value, __PtyId.set, None, None)

    
    # Element {urn:rocs.001.001.06}PreferredIndicator uses Python identifier PreferredIndicator
    __PreferredIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PreferredIndicator'), 'PreferredIndicator', '__urnrocs_001_001_06_CSMIdentifier_urnrocs_001_001_06PreferredIndicator', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 25, 6), )

    
    PreferredIndicator = property(__PreferredIndicator.value, __PreferredIndicator.set, None, None)

    _ElementMap.update({
        __PtyId.name() : __PtyId,
        __PreferredIndicator.name() : __PreferredIndicator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CSMIdentifier = CSMIdentifier
Namespace.addCategoryObject('typeBinding', 'CSMIdentifier', CSMIdentifier)


# Complex type {urn:rocs.001.001.06}CutOffType with content type ELEMENT_ONLY
class CutOffType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}CutOffType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CutOffType')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 47, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}Time uses Python identifier Time
    __Time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Time'), 'Time', '__urnrocs_001_001_06_CutOffType_urnrocs_001_001_06Time', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 49, 6), )

    
    Time = property(__Time.value, __Time.set, None, None)

    
    # Element {urn:rocs.001.001.06}RelDays uses Python identifier RelDays
    __RelDays = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RelDays'), 'RelDays', '__urnrocs_001_001_06_CutOffType_urnrocs_001_001_06RelDays', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 50, 6), )

    
    RelDays = property(__RelDays.value, __RelDays.set, None, None)

    
    # Element {urn:rocs.001.001.06}TimeZone uses Python identifier TimeZone
    __TimeZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimeZone'), 'TimeZone', '__urnrocs_001_001_06_CutOffType_urnrocs_001_001_06TimeZone', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 51, 6), )

    
    TimeZone = property(__TimeZone.value, __TimeZone.set, None, None)

    _ElementMap.update({
        __Time.name() : __Time,
        __RelDays.name() : __RelDays,
        __TimeZone.name() : __TimeZone
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CutOffType = CutOffType
Namespace.addCategoryObject('typeBinding', 'CutOffType', CutOffType)


# Complex type {urn:rocs.001.001.06}DateTimePeriod with content type ELEMENT_ONLY
class DateTimePeriod (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}DateTimePeriod with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateTimePeriod')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 54, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}FrDtTm uses Python identifier FrDtTm
    __FrDtTm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FrDtTm'), 'FrDtTm', '__urnrocs_001_001_06_DateTimePeriod_urnrocs_001_001_06FrDtTm', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 56, 6), )

    
    FrDtTm = property(__FrDtTm.value, __FrDtTm.set, None, None)

    
    # Element {urn:rocs.001.001.06}ToDtTm uses Python identifier ToDtTm
    __ToDtTm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ToDtTm'), 'ToDtTm', '__urnrocs_001_001_06_DateTimePeriod_urnrocs_001_001_06ToDtTm', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 57, 6), )

    
    ToDtTm = property(__ToDtTm.value, __ToDtTm.set, None, None)

    _ElementMap.update({
        __FrDtTm.name() : __FrDtTm,
        __ToDtTm.name() : __ToDtTm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DateTimePeriod = DateTimePeriod
Namespace.addCategoryObject('typeBinding', 'DateTimePeriod', DateTimePeriod)


# Complex type {urn:rocs.001.001.06}Document with content type ELEMENT_ONLY
class Document_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}Document with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Document')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 60, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}rocs.001.001.06 uses Python identifier rocs_001_001_06
    __rocs_001_001_06 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rocs.001.001.06'), 'rocs_001_001_06', '__urnrocs_001_001_06_Document__urnrocs_001_001_06rocs_001_001_06', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 62, 6), )

    
    rocs_001_001_06 = property(__rocs_001_001_06.value, __rocs_001_001_06.set, None, None)

    _ElementMap.update({
        __rocs_001_001_06.name() : __rocs_001_001_06
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Document_ = Document_
Namespace.addCategoryObject('typeBinding', 'Document', Document_)


# Complex type {urn:rocs.001.001.06}FinancialInstitutionIdentification with content type ELEMENT_ONLY
class FinancialInstitutionIdentification (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}FinancialInstitutionIdentification with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FinancialInstitutionIdentification')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 65, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}BIC uses Python identifier BIC
    __BIC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BIC'), 'BIC', '__urnrocs_001_001_06_FinancialInstitutionIdentification_urnrocs_001_001_06BIC', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 67, 6), )

    
    BIC = property(__BIC.value, __BIC.set, None, None)

    
    # Element {urn:rocs.001.001.06}NmAndAdr uses Python identifier NmAndAdr
    __NmAndAdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NmAndAdr'), 'NmAndAdr', '__urnrocs_001_001_06_FinancialInstitutionIdentification_urnrocs_001_001_06NmAndAdr', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 68, 6), )

    
    NmAndAdr = property(__NmAndAdr.value, __NmAndAdr.set, None, None)

    _ElementMap.update({
        __BIC.name() : __BIC,
        __NmAndAdr.name() : __NmAndAdr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.FinancialInstitutionIdentification = FinancialInstitutionIdentification
Namespace.addCategoryObject('typeBinding', 'FinancialInstitutionIdentification', FinancialInstitutionIdentification)


# Complex type {urn:rocs.001.001.06}GenericIdentification1 with content type ELEMENT_ONLY
class GenericIdentification1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}GenericIdentification1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericIdentification1')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 71, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__urnrocs_001_001_06_GenericIdentification1_urnrocs_001_001_06Id', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 73, 6), )

    
    Id = property(__Id.value, __Id.set, None, None)

    
    # Element {urn:rocs.001.001.06}SchmeNm uses Python identifier SchmeNm
    __SchmeNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm'), 'SchmeNm', '__urnrocs_001_001_06_GenericIdentification1_urnrocs_001_001_06SchmeNm', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 74, 6), )

    
    SchmeNm = property(__SchmeNm.value, __SchmeNm.set, None, None)

    
    # Element {urn:rocs.001.001.06}Issr uses Python identifier Issr
    __Issr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Issr'), 'Issr', '__urnrocs_001_001_06_GenericIdentification1_urnrocs_001_001_06Issr', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 75, 6), )

    
    Issr = property(__Issr.value, __Issr.set, None, None)

    _ElementMap.update({
        __Id.name() : __Id,
        __SchmeNm.name() : __SchmeNm,
        __Issr.name() : __Issr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GenericIdentification1 = GenericIdentification1
Namespace.addCategoryObject('typeBinding', 'GenericIdentification1', GenericIdentification1)


# Complex type {urn:rocs.001.001.06}GroupHeader with content type ELEMENT_ONLY
class GroupHeader (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}GroupHeader with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GroupHeader')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 78, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}MsgId uses Python identifier MsgId
    __MsgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MsgId'), 'MsgId', '__urnrocs_001_001_06_GroupHeader_urnrocs_001_001_06MsgId', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 80, 6), )

    
    MsgId = property(__MsgId.value, __MsgId.set, None, None)

    
    # Element {urn:rocs.001.001.06}CreDtTm uses Python identifier CreDtTm
    __CreDtTm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CreDtTm'), 'CreDtTm', '__urnrocs_001_001_06_GroupHeader_urnrocs_001_001_06CreDtTm', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 81, 6), )

    
    CreDtTm = property(__CreDtTm.value, __CreDtTm.set, None, None)

    
    # Element {urn:rocs.001.001.06}PtyId uses Python identifier PtyId
    __PtyId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PtyId'), 'PtyId', '__urnrocs_001_001_06_GroupHeader_urnrocs_001_001_06PtyId', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 82, 6), )

    
    PtyId = property(__PtyId.value, __PtyId.set, None, None)

    
    # Element {urn:rocs.001.001.06}FullTable uses Python identifier FullTable
    __FullTable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FullTable'), 'FullTable', '__urnrocs_001_001_06_GroupHeader_urnrocs_001_001_06FullTable', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 83, 6), )

    
    FullTable = property(__FullTable.value, __FullTable.set, None, None)

    
    # Element {urn:rocs.001.001.06}FileValidityDate uses Python identifier FileValidityDate
    __FileValidityDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FileValidityDate'), 'FileValidityDate', '__urnrocs_001_001_06_GroupHeader_urnrocs_001_001_06FileValidityDate', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 84, 6), )

    
    FileValidityDate = property(__FileValidityDate.value, __FileValidityDate.set, None, None)

    _ElementMap.update({
        __MsgId.name() : __MsgId,
        __CreDtTm.name() : __CreDtTm,
        __PtyId.name() : __PtyId,
        __FullTable.name() : __FullTable,
        __FileValidityDate.name() : __FileValidityDate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GroupHeader = GroupHeader
Namespace.addCategoryObject('typeBinding', 'GroupHeader', GroupHeader)


# Complex type {urn:rocs.001.001.06}LongNameAndAddress2 with content type ELEMENT_ONLY
class LongNameAndAddress2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}LongNameAndAddress2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LongNameAndAddress2')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 93, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnrocs_001_001_06_LongNameAndAddress2_urnrocs_001_001_06Nm', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 95, 6), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:rocs.001.001.06}Adr uses Python identifier Adr
    __Adr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Adr'), 'Adr', '__urnrocs_001_001_06_LongNameAndAddress2_urnrocs_001_001_06Adr', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 96, 6), )

    
    Adr = property(__Adr.value, __Adr.set, None, None)

    _ElementMap.update({
        __Nm.name() : __Nm,
        __Adr.name() : __Adr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LongNameAndAddress2 = LongNameAndAddress2
Namespace.addCategoryObject('typeBinding', 'LongNameAndAddress2', LongNameAndAddress2)


# Complex type {urn:rocs.001.001.06}LongPostalAddress1Choice with content type ELEMENT_ONLY
class LongPostalAddress1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}LongPostalAddress1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LongPostalAddress1Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 99, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}Ustrd uses Python identifier Ustrd
    __Ustrd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ustrd'), 'Ustrd', '__urnrocs_001_001_06_LongPostalAddress1Choice_urnrocs_001_001_06Ustrd', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 102, 8), )

    
    Ustrd = property(__Ustrd.value, __Ustrd.set, None, None)

    
    # Element {urn:rocs.001.001.06}Strd uses Python identifier Strd
    __Strd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Strd'), 'Strd', '__urnrocs_001_001_06_LongPostalAddress1Choice_urnrocs_001_001_06Strd', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 103, 8), )

    
    Strd = property(__Strd.value, __Strd.set, None, None)

    _ElementMap.update({
        __Ustrd.name() : __Ustrd,
        __Strd.name() : __Strd
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LongPostalAddress1Choice = LongPostalAddress1Choice
Namespace.addCategoryObject('typeBinding', 'LongPostalAddress1Choice', LongPostalAddress1Choice)


# Complex type {urn:rocs.001.001.06}NameAndAddress2 with content type ELEMENT_ONLY
class NameAndAddress2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}NameAndAddress2 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NameAndAddress2')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 125, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm', '__urnrocs_001_001_06_NameAndAddress2_urnrocs_001_001_06Nm', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 127, 6), )

    
    Nm = property(__Nm.value, __Nm.set, None, None)

    
    # Element {urn:rocs.001.001.06}Adr uses Python identifier Adr
    __Adr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Adr'), 'Adr', '__urnrocs_001_001_06_NameAndAddress2_urnrocs_001_001_06Adr', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 128, 6), )

    
    Adr = property(__Adr.value, __Adr.set, None, None)

    _ElementMap.update({
        __Nm.name() : __Nm,
        __Adr.name() : __Adr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NameAndAddress2 = NameAndAddress2
Namespace.addCategoryObject('typeBinding', 'NameAndAddress2', NameAndAddress2)


# Complex type {urn:rocs.001.001.06}PartyIdentification1Choice with content type ELEMENT_ONLY
class PartyIdentification1Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}PartyIdentification1Choice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartyIdentification1Choice')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 131, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}BICOrBEI uses Python identifier BICOrBEI
    __BICOrBEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BICOrBEI'), 'BICOrBEI', '__urnrocs_001_001_06_PartyIdentification1Choice_urnrocs_001_001_06BICOrBEI', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 134, 8), )

    
    BICOrBEI = property(__BICOrBEI.value, __BICOrBEI.set, None, None)

    
    # Element {urn:rocs.001.001.06}PrtryId uses Python identifier PrtryId
    __PrtryId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrtryId'), 'PrtryId', '__urnrocs_001_001_06_PartyIdentification1Choice_urnrocs_001_001_06PrtryId', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 135, 8), )

    
    PrtryId = property(__PrtryId.value, __PrtryId.set, None, None)

    
    # Element {urn:rocs.001.001.06}NmAndAdr uses Python identifier NmAndAdr
    __NmAndAdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NmAndAdr'), 'NmAndAdr', '__urnrocs_001_001_06_PartyIdentification1Choice_urnrocs_001_001_06NmAndAdr', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 136, 8), )

    
    NmAndAdr = property(__NmAndAdr.value, __NmAndAdr.set, None, None)

    _ElementMap.update({
        __BICOrBEI.name() : __BICOrBEI,
        __PrtryId.name() : __PrtryId,
        __NmAndAdr.name() : __NmAndAdr
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PartyIdentification1Choice = PartyIdentification1Choice
Namespace.addCategoryObject('typeBinding', 'PartyIdentification1Choice', PartyIdentification1Choice)


# Complex type {urn:rocs.001.001.06}PriceIndication with content type ELEMENT_ONLY
class PriceIndication (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}PriceIndication with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PriceIndication')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 140, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}Amount uses Python identifier Amount
    __Amount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Amount'), 'Amount', '__urnrocs_001_001_06_PriceIndication_urnrocs_001_001_06Amount', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 142, 6), )

    
    Amount = property(__Amount.value, __Amount.set, None, None)

    
    # Element {urn:rocs.001.001.06}Indication uses Python identifier Indication
    __Indication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Indication'), 'Indication', '__urnrocs_001_001_06_PriceIndication_urnrocs_001_001_06Indication', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 143, 6), )

    
    Indication = property(__Indication.value, __Indication.set, None, None)

    _ElementMap.update({
        __Amount.name() : __Amount,
        __Indication.name() : __Indication
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PriceIndication = PriceIndication
Namespace.addCategoryObject('typeBinding', 'PriceIndication', PriceIndication)


# Complex type {urn:rocs.001.001.06}ProductIdentifier with content type ELEMENT_ONLY
class ProductIdentifier (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}ProductIdentifier with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 146, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}ProductName uses Python identifier ProductName
    __ProductName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProductName'), 'ProductName', '__urnrocs_001_001_06_ProductIdentifier_urnrocs_001_001_06ProductName', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 148, 6), )

    
    ProductName = property(__ProductName.value, __ProductName.set, None, None)

    _ElementMap.update({
        __ProductName.name() : __ProductName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProductIdentifier = ProductIdentifier
Namespace.addCategoryObject('typeBinding', 'ProductIdentifier', ProductIdentifier)


# Complex type {urn:rocs.001.001.06}ReachEntry with content type ELEMENT_ONLY
class ReachEntry (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}ReachEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReachEntry')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 151, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}Status uses Python identifier Status
    __Status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Status'), 'Status', '__urnrocs_001_001_06_ReachEntry_urnrocs_001_001_06Status', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 153, 6), )

    
    Status = property(__Status.value, __Status.set, None, None)

    
    # Element {urn:rocs.001.001.06}Validity uses Python identifier Validity
    __Validity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validity'), 'Validity', '__urnrocs_001_001_06_ReachEntry_urnrocs_001_001_06Validity', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 154, 6), )

    
    Validity = property(__Validity.value, __Validity.set, None, None)

    
    # Element {urn:rocs.001.001.06}Participant uses Python identifier Participant
    __Participant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Participant'), 'Participant', '__urnrocs_001_001_06_ReachEntry_urnrocs_001_001_06Participant', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 155, 6), )

    
    Participant = property(__Participant.value, __Participant.set, None, None)

    
    # Element {urn:rocs.001.001.06}Product uses Python identifier Product
    __Product = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Product'), 'Product', '__urnrocs_001_001_06_ReachEntry_urnrocs_001_001_06Product', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 156, 6), )

    
    Product = property(__Product.value, __Product.set, None, None)

    
    # Element {urn:rocs.001.001.06}CSM uses Python identifier CSM
    __CSM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CSM'), 'CSM', '__urnrocs_001_001_06_ReachEntry_urnrocs_001_001_06CSM', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 157, 6), )

    
    CSM = property(__CSM.value, __CSM.set, None, None)

    
    # Element {urn:rocs.001.001.06}CutOff uses Python identifier CutOff
    __CutOff = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CutOff'), 'CutOff', '__urnrocs_001_001_06_ReachEntry_urnrocs_001_001_06CutOff', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 158, 6), )

    
    CutOff = property(__CutOff.value, __CutOff.set, None, None)

    
    # Element {urn:rocs.001.001.06}SettlmConfirm uses Python identifier SettlmConfirm
    __SettlmConfirm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SettlmConfirm'), 'SettlmConfirm', '__urnrocs_001_001_06_ReachEntry_urnrocs_001_001_06SettlmConfirm', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 159, 6), )

    
    SettlmConfirm = property(__SettlmConfirm.value, __SettlmConfirm.set, None, None)

    
    # Element {urn:rocs.001.001.06}SupportedAOS uses Python identifier SupportedAOS
    __SupportedAOS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SupportedAOS'), 'SupportedAOS', '__urnrocs_001_001_06_ReachEntry_urnrocs_001_001_06SupportedAOS', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 160, 6), )

    
    SupportedAOS = property(__SupportedAOS.value, __SupportedAOS.set, None, None)

    
    # Element {urn:rocs.001.001.06}PriceIndicator uses Python identifier PriceIndicator
    __PriceIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PriceIndicator'), 'PriceIndicator', '__urnrocs_001_001_06_ReachEntry_urnrocs_001_001_06PriceIndicator', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 161, 6), )

    
    PriceIndicator = property(__PriceIndicator.value, __PriceIndicator.set, None, None)

    _ElementMap.update({
        __Status.name() : __Status,
        __Validity.name() : __Validity,
        __Participant.name() : __Participant,
        __Product.name() : __Product,
        __CSM.name() : __CSM,
        __CutOff.name() : __CutOff,
        __SettlmConfirm.name() : __SettlmConfirm,
        __SupportedAOS.name() : __SupportedAOS,
        __PriceIndicator.name() : __PriceIndicator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ReachEntry = ReachEntry
Namespace.addCategoryObject('typeBinding', 'ReachEntry', ReachEntry)


# Complex type {urn:rocs.001.001.06}rocs.001.001.06 with content type ELEMENT_ONLY
class rocs_001_001_06 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}rocs.001.001.06 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rocs.001.001.06')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 164, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}GrpHdr uses Python identifier GrpHdr
    __GrpHdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GrpHdr'), 'GrpHdr', '__urnrocs_001_001_06_rocs_001_001_06_urnrocs_001_001_06GrpHdr', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 166, 6), )

    
    GrpHdr = property(__GrpHdr.value, __GrpHdr.set, None, None)

    
    # Element {urn:rocs.001.001.06}RchEntry uses Python identifier RchEntry
    __RchEntry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RchEntry'), 'RchEntry', '__urnrocs_001_001_06_rocs_001_001_06_urnrocs_001_001_06RchEntry', True, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 167, 6), )

    
    RchEntry = property(__RchEntry.value, __RchEntry.set, None, None)

    _ElementMap.update({
        __GrpHdr.name() : __GrpHdr,
        __RchEntry.name() : __RchEntry
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.rocs_001_001_06 = rocs_001_001_06
Namespace.addCategoryObject('typeBinding', 'rocs.001.001.06', rocs_001_001_06)


# Complex type {urn:rocs.001.001.06}SettlementConfirmation with content type ELEMENT_ONLY
class SettlementConfirmation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}SettlementConfirmation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SettlementConfirmation')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 170, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}GuaranteedTime uses Python identifier GuaranteedTime
    __GuaranteedTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GuaranteedTime'), 'GuaranteedTime', '__urnrocs_001_001_06_SettlementConfirmation_urnrocs_001_001_06GuaranteedTime', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 172, 6), )

    
    GuaranteedTime = property(__GuaranteedTime.value, __GuaranteedTime.set, None, None)

    
    # Element {urn:rocs.001.001.06}DaysDelay uses Python identifier DaysDelay
    __DaysDelay = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DaysDelay'), 'DaysDelay', '__urnrocs_001_001_06_SettlementConfirmation_urnrocs_001_001_06DaysDelay', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 173, 6), )

    
    DaysDelay = property(__DaysDelay.value, __DaysDelay.set, None, None)

    
    # Element {urn:rocs.001.001.06}TimeZone uses Python identifier TimeZone
    __TimeZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimeZone'), 'TimeZone', '__urnrocs_001_001_06_SettlementConfirmation_urnrocs_001_001_06TimeZone', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 174, 6), )

    
    TimeZone = property(__TimeZone.value, __TimeZone.set, None, None)

    _ElementMap.update({
        __GuaranteedTime.name() : __GuaranteedTime,
        __DaysDelay.name() : __DaysDelay,
        __TimeZone.name() : __TimeZone
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.SettlementConfirmation = SettlementConfirmation
Namespace.addCategoryObject('typeBinding', 'SettlementConfirmation', SettlementConfirmation)


# Complex type {urn:rocs.001.001.06}StructuredLongPostalAddress1 with content type ELEMENT_ONLY
class StructuredLongPostalAddress1 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}StructuredLongPostalAddress1 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StructuredLongPostalAddress1')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 177, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:rocs.001.001.06}BldgNm uses Python identifier BldgNm
    __BldgNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BldgNm'), 'BldgNm', '__urnrocs_001_001_06_StructuredLongPostalAddress1_urnrocs_001_001_06BldgNm', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 179, 6), )

    
    BldgNm = property(__BldgNm.value, __BldgNm.set, None, None)

    
    # Element {urn:rocs.001.001.06}StrtNm uses Python identifier StrtNm
    __StrtNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StrtNm'), 'StrtNm', '__urnrocs_001_001_06_StructuredLongPostalAddress1_urnrocs_001_001_06StrtNm', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 180, 6), )

    
    StrtNm = property(__StrtNm.value, __StrtNm.set, None, None)

    
    # Element {urn:rocs.001.001.06}StrtBldgId uses Python identifier StrtBldgId
    __StrtBldgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StrtBldgId'), 'StrtBldgId', '__urnrocs_001_001_06_StructuredLongPostalAddress1_urnrocs_001_001_06StrtBldgId', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 181, 6), )

    
    StrtBldgId = property(__StrtBldgId.value, __StrtBldgId.set, None, None)

    
    # Element {urn:rocs.001.001.06}Flr uses Python identifier Flr
    __Flr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Flr'), 'Flr', '__urnrocs_001_001_06_StructuredLongPostalAddress1_urnrocs_001_001_06Flr', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 182, 6), )

    
    Flr = property(__Flr.value, __Flr.set, None, None)

    
    # Element {urn:rocs.001.001.06}TwnNm uses Python identifier TwnNm
    __TwnNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TwnNm'), 'TwnNm', '__urnrocs_001_001_06_StructuredLongPostalAddress1_urnrocs_001_001_06TwnNm', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 183, 6), )

    
    TwnNm = property(__TwnNm.value, __TwnNm.set, None, None)

    
    # Element {urn:rocs.001.001.06}DstrctNm uses Python identifier DstrctNm
    __DstrctNm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DstrctNm'), 'DstrctNm', '__urnrocs_001_001_06_StructuredLongPostalAddress1_urnrocs_001_001_06DstrctNm', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 184, 6), )

    
    DstrctNm = property(__DstrctNm.value, __DstrctNm.set, None, None)

    
    # Element {urn:rocs.001.001.06}RgnId uses Python identifier RgnId
    __RgnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RgnId'), 'RgnId', '__urnrocs_001_001_06_StructuredLongPostalAddress1_urnrocs_001_001_06RgnId', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 185, 6), )

    
    RgnId = property(__RgnId.value, __RgnId.set, None, None)

    
    # Element {urn:rocs.001.001.06}Stat uses Python identifier Stat
    __Stat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Stat'), 'Stat', '__urnrocs_001_001_06_StructuredLongPostalAddress1_urnrocs_001_001_06Stat', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 186, 6), )

    
    Stat = property(__Stat.value, __Stat.set, None, None)

    
    # Element {urn:rocs.001.001.06}CtyId uses Python identifier CtyId
    __CtyId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtyId'), 'CtyId', '__urnrocs_001_001_06_StructuredLongPostalAddress1_urnrocs_001_001_06CtyId', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 187, 6), )

    
    CtyId = property(__CtyId.value, __CtyId.set, None, None)

    
    # Element {urn:rocs.001.001.06}Ctry uses Python identifier Ctry
    __Ctry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), 'Ctry', '__urnrocs_001_001_06_StructuredLongPostalAddress1_urnrocs_001_001_06Ctry', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 188, 6), )

    
    Ctry = property(__Ctry.value, __Ctry.set, None, None)

    
    # Element {urn:rocs.001.001.06}PstCdId uses Python identifier PstCdId
    __PstCdId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PstCdId'), 'PstCdId', '__urnrocs_001_001_06_StructuredLongPostalAddress1_urnrocs_001_001_06PstCdId', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 189, 6), )

    
    PstCdId = property(__PstCdId.value, __PstCdId.set, None, None)

    
    # Element {urn:rocs.001.001.06}POB uses Python identifier POB
    __POB = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'POB'), 'POB', '__urnrocs_001_001_06_StructuredLongPostalAddress1_urnrocs_001_001_06POB', False, pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 190, 6), )

    
    POB = property(__POB.value, __POB.set, None, None)

    _ElementMap.update({
        __BldgNm.name() : __BldgNm,
        __StrtNm.name() : __StrtNm,
        __StrtBldgId.name() : __StrtBldgId,
        __Flr.name() : __Flr,
        __TwnNm.name() : __TwnNm,
        __DstrctNm.name() : __DstrctNm,
        __RgnId.name() : __RgnId,
        __Stat.name() : __Stat,
        __CtyId.name() : __CtyId,
        __Ctry.name() : __Ctry,
        __PstCdId.name() : __PstCdId,
        __POB.name() : __POB
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StructuredLongPostalAddress1 = StructuredLongPostalAddress1
Namespace.addCategoryObject('typeBinding', 'StructuredLongPostalAddress1', StructuredLongPostalAddress1)


# Complex type {urn:rocs.001.001.06}CurrencyAndAmount with content type SIMPLE
class CurrencyAndAmount (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:rocs.001.001.06}CurrencyAndAmount with content type SIMPLE"""
    _TypeDefinition = CurrencyAndAmount_SimpleType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrencyAndAmount')
    _XSDLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 28, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is CurrencyAndAmount_SimpleType
    
    # Attribute Ccy uses Python identifier Ccy
    __Ccy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Ccy'), 'Ccy', '__urnrocs_001_001_06_CurrencyAndAmount_Ccy', _module_typeBindings.CurrencyCode, required=True)
    __Ccy._DeclarationLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 31, 8)
    __Ccy._UseLocation = pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 31, 8)
    
    Ccy = property(__Ccy.value, __Ccy.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Ccy.name() : __Ccy
    })
_module_typeBindings.CurrencyAndAmount = CurrencyAndAmount
Namespace.addCategoryObject('typeBinding', 'CurrencyAndAmount', CurrencyAndAmount)


Document = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Document'), Document_, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 6, 2))
Namespace.addCategoryObject('elementBinding', Document.name().localName(), Document)



AOSList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AOSId'), pyxb.binding.datatypes.decimal, scope=AOSList, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 14, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AOSList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AOSId')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 14, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AOSList._Automaton = _BuildAutomaton()




CSMIdentifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PtyId'), PartyIdentification1Choice, scope=CSMIdentifier, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 24, 6)))

CSMIdentifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PreferredIndicator'), pyxb.binding.datatypes.boolean, scope=CSMIdentifier, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 25, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CSMIdentifier._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PtyId')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 24, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CSMIdentifier._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PreferredIndicator')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 25, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CSMIdentifier._Automaton = _BuildAutomaton_()




CutOffType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Time'), ISOTime, scope=CutOffType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 49, 6)))

CutOffType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RelDays'), pyxb.binding.datatypes.nonNegativeInteger, scope=CutOffType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 50, 6)))

CutOffType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeZone'), Max16Text, scope=CutOffType, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 51, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CutOffType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Time')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 49, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CutOffType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RelDays')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 50, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CutOffType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeZone')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 51, 6))
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CutOffType._Automaton = _BuildAutomaton_2()




DateTimePeriod._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FrDtTm'), ISODateTime, scope=DateTimePeriod, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 56, 6)))

DateTimePeriod._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ToDtTm'), ISODateTime, scope=DateTimePeriod, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 57, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 57, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DateTimePeriod._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FrDtTm')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 56, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DateTimePeriod._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ToDtTm')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 57, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DateTimePeriod._Automaton = _BuildAutomaton_3()




Document_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rocs.001.001.06'), rocs_001_001_06, scope=Document_, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 62, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Document_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rocs.001.001.06')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 62, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Document_._Automaton = _BuildAutomaton_4()




FinancialInstitutionIdentification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BIC'), AnyBICIdentifier, scope=FinancialInstitutionIdentification, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 67, 6)))

FinancialInstitutionIdentification._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NmAndAdr'), LongNameAndAddress2, scope=FinancialInstitutionIdentification, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 68, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FinancialInstitutionIdentification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BIC')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 67, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FinancialInstitutionIdentification._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NmAndAdr')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 68, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FinancialInstitutionIdentification._Automaton = _BuildAutomaton_5()




GenericIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Max35Text, scope=GenericIdentification1, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 73, 6)))

GenericIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm'), Max35Text, scope=GenericIdentification1, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 74, 6)))

GenericIdentification1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Issr'), Max35Text, scope=GenericIdentification1, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 75, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 74, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 75, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenericIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 73, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GenericIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SchmeNm')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 74, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GenericIdentification1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Issr')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 75, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GenericIdentification1._Automaton = _BuildAutomaton_6()




GroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MsgId'), Max35Text, scope=GroupHeader, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 80, 6)))

GroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CreDtTm'), ISODateTime, scope=GroupHeader, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 81, 6)))

GroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PtyId'), PartyIdentification1Choice, scope=GroupHeader, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 82, 6)))

GroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FullTable'), pyxb.binding.datatypes.boolean, scope=GroupHeader, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 83, 6)))

GroupHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FileValidityDate'), ISODateTime, scope=GroupHeader, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 84, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MsgId')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 80, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CreDtTm')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 81, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PtyId')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 82, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FullTable')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 83, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GroupHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FileValidityDate')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 84, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GroupHeader._Automaton = _BuildAutomaton_7()




LongNameAndAddress2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max140Text, scope=LongNameAndAddress2, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 95, 6)))

LongNameAndAddress2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Adr'), LongPostalAddress1Choice, scope=LongNameAndAddress2, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 96, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 96, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LongNameAndAddress2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 95, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LongNameAndAddress2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Adr')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 96, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LongNameAndAddress2._Automaton = _BuildAutomaton_8()




LongPostalAddress1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ustrd'), Max140Text, scope=LongPostalAddress1Choice, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 102, 8)))

LongPostalAddress1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Strd'), StructuredLongPostalAddress1, scope=LongPostalAddress1Choice, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 103, 8)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LongPostalAddress1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ustrd')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 102, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LongPostalAddress1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Strd')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 103, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LongPostalAddress1Choice._Automaton = _BuildAutomaton_9()




NameAndAddress2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max35Text, scope=NameAndAddress2, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 127, 6)))

NameAndAddress2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Adr'), LongPostalAddress1Choice, scope=NameAndAddress2, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 128, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 128, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NameAndAddress2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 127, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NameAndAddress2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Adr')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 128, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
NameAndAddress2._Automaton = _BuildAutomaton_10()




PartyIdentification1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BICOrBEI'), AnyBICIdentifier, scope=PartyIdentification1Choice, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 134, 8)))

PartyIdentification1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrtryId'), GenericIdentification1, scope=PartyIdentification1Choice, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 135, 8)))

PartyIdentification1Choice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NmAndAdr'), NameAndAddress2, scope=PartyIdentification1Choice, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 136, 8)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PartyIdentification1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BICOrBEI')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 134, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PartyIdentification1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrtryId')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 135, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PartyIdentification1Choice._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NmAndAdr')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 136, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PartyIdentification1Choice._Automaton = _BuildAutomaton_11()




PriceIndication._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Amount'), CurrencyAndAmount, scope=PriceIndication, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 142, 6)))

PriceIndication._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Indication'), Max35Text, scope=PriceIndication, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 143, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PriceIndication._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Amount')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 142, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PriceIndication._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Indication')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 143, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PriceIndication._Automaton = _BuildAutomaton_12()




ProductIdentifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProductName'), Max16Text, scope=ProductIdentifier, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 148, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ProductIdentifier._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProductName')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 148, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProductIdentifier._Automaton = _BuildAutomaton_13()




ReachEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Status'), Max16Text, scope=ReachEntry, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 153, 6)))

ReachEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validity'), DateTimePeriod, scope=ReachEntry, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 154, 6)))

ReachEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Participant'), FinancialInstitutionIdentification, scope=ReachEntry, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 155, 6)))

ReachEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Product'), ProductIdentifier, scope=ReachEntry, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 156, 6)))

ReachEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CSM'), CSMIdentifier, scope=ReachEntry, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 157, 6)))

ReachEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CutOff'), CutOffType, scope=ReachEntry, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 158, 6)))

ReachEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SettlmConfirm'), SettlementConfirmation, scope=ReachEntry, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 159, 6)))

ReachEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupportedAOS'), AOSList, scope=ReachEntry, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 160, 6)))

ReachEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PriceIndicator'), PriceIndication, scope=ReachEntry, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 161, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 157, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 159, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 160, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 161, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReachEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Status')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 153, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReachEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validity')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 154, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReachEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Participant')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 155, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReachEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Product')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 156, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReachEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CSM')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 157, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReachEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CutOff')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 158, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ReachEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SettlmConfirm')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 159, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ReachEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SupportedAOS')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 160, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ReachEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PriceIndicator')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 161, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReachEntry._Automaton = _BuildAutomaton_14()




rocs_001_001_06._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GrpHdr'), GroupHeader, scope=rocs_001_001_06, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 166, 6)))

rocs_001_001_06._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RchEntry'), ReachEntry, scope=rocs_001_001_06, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 167, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(rocs_001_001_06._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GrpHdr')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 166, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(rocs_001_001_06._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RchEntry')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 167, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
rocs_001_001_06._Automaton = _BuildAutomaton_15()




SettlementConfirmation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GuaranteedTime'), ISOTime, scope=SettlementConfirmation, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 172, 6)))

SettlementConfirmation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DaysDelay'), pyxb.binding.datatypes.nonNegativeInteger, scope=SettlementConfirmation, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 173, 6)))

SettlementConfirmation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeZone'), Max16Text, scope=SettlementConfirmation, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 174, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SettlementConfirmation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GuaranteedTime')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 172, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SettlementConfirmation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DaysDelay')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 173, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SettlementConfirmation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeZone')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 174, 6))
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SettlementConfirmation._Automaton = _BuildAutomaton_16()




StructuredLongPostalAddress1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BldgNm'), Max35Text, scope=StructuredLongPostalAddress1, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 179, 6)))

StructuredLongPostalAddress1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StrtNm'), Max35Text, scope=StructuredLongPostalAddress1, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 180, 6)))

StructuredLongPostalAddress1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StrtBldgId'), Max35Text, scope=StructuredLongPostalAddress1, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 181, 6)))

StructuredLongPostalAddress1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Flr'), Max16Text, scope=StructuredLongPostalAddress1, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 182, 6)))

StructuredLongPostalAddress1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TwnNm'), Max35Text, scope=StructuredLongPostalAddress1, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 183, 6)))

StructuredLongPostalAddress1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DstrctNm'), Max35Text, scope=StructuredLongPostalAddress1, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 184, 6)))

StructuredLongPostalAddress1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RgnId'), Max35Text, scope=StructuredLongPostalAddress1, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 185, 6)))

StructuredLongPostalAddress1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Stat'), Max35Text, scope=StructuredLongPostalAddress1, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 186, 6)))

StructuredLongPostalAddress1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtyId'), Max35Text, scope=StructuredLongPostalAddress1, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 187, 6)))

StructuredLongPostalAddress1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ctry'), CountryCode, scope=StructuredLongPostalAddress1, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 188, 6)))

StructuredLongPostalAddress1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PstCdId'), Max16Text, scope=StructuredLongPostalAddress1, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 189, 6)))

StructuredLongPostalAddress1._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'POB'), Max16Text, scope=StructuredLongPostalAddress1, location=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 190, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 179, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 180, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 181, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 182, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 184, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 185, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 186, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 187, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 190, 6))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StructuredLongPostalAddress1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BldgNm')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 179, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StructuredLongPostalAddress1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StrtNm')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 180, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StructuredLongPostalAddress1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StrtBldgId')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 181, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StructuredLongPostalAddress1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Flr')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 182, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StructuredLongPostalAddress1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TwnNm')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 183, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StructuredLongPostalAddress1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DstrctNm')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 184, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StructuredLongPostalAddress1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RgnId')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 185, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StructuredLongPostalAddress1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Stat')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 186, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StructuredLongPostalAddress1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtyId')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 187, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StructuredLongPostalAddress1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ctry')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 188, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StructuredLongPostalAddress1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PstCdId')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 189, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(StructuredLongPostalAddress1._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'POB')), pyxb.utils.utility.Location('/home/toivotuo/Dropbox/Personal/Studies/UoH/tlbop/tapestry/tapestry/router/xsd/rocs.001.001.06.xsd', 190, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StructuredLongPostalAddress1._Automaton = _BuildAutomaton_17()

