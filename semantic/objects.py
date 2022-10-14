from __future__ import annotations
from enums import Kinds, States
from typeAnalyzer import bool_, char_, string_, int_


class Object:
    nName: int = None
    pNext: Object = None
    eKind: Kinds = Kinds.NO_KIND_DEF_
    _ = None

    def __init__(self,
                 nName: int = None,
                 pNext: Object = None,
                 eKind: Kinds = Kinds.NO_KIND_DEF_):
        self.nName = nName
        self.pNext = pNext
        self.eKind = eKind


class Var:
    pType: Object = None

    def __init__(self, ptype: Object):
        self.ptype = ptype


class Param:
    pType: Object = None


class Field:
    pType: Object = None


class Function:
    pRetType: Object = None
    pParams: Object = None


class Array:
    pElemType: Object
    nNumElems: int

    def __init__(self, pElemType: Object, nNumElems: int):
        self.pElemType = pElemType
        self.nNumElems = nNumElems


class Struct:
    pFields: Object = None


class Alias:
    pBaseType: Object = None

    def __init__(self, pBaseType: Object):
        self.pBaseType = pBaseType


class Type:
    name: int
    object: Object

    def __init__(self, name: int, object: Object):
        self.name = name
        self.object = object


class ID:
    name: int
    object: Object

    def __init__(self, name: int, object: Object = None):
        self.name = name
        self.object = object


class T:
    type: Object

    def __init__(self, type: Object):
        self.type = type


class LI:
    list: Object

    def __init__(self, list: Object):
        self.list = list


class BOOL:
    type: Object
    val: bool

    def __init__(
        self,
        val: bool,
        type: Object = bool_,
    ):
        self.val = val
        self.type = type


class CHR:
    type: Object
    pos: int
    val: str

    def __init__(
        self,
        val: str,
        pos: int,
        type: Object = char_,
    ):
        self.val = val
        self.pos = pos
        self.type = type


class STR:
    type: Object
    pos: int
    val: str

    def __init__(
        self,
        val: str,
        pos: int,
        type: Object = string_,
    ):
        self.val = val
        self.pos = pos
        self.type = type


class NUM:
    type: Object
    pos: int
    val: int

    def __init__(
        self,
        val: int,
        pos: int,
        type: Object = int_,
    ):
        self.val = val
        self.pos = pos
        self.type = type


class t_attrib:
    nont: States = None
    _ = None

    def __init__(self, nont: States, _=None):
        self.nont = nont
        self._ = _
