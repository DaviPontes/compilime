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
    nIndex: int = None
    nSize: int = None

    def __init__(self, pType: Object, nIndex: int, nSize: int):
        self.pType = pType
        self.nIndex = nIndex
        self.nSize = nSize


class Param:
    pType: Object = None
    nIndex: int = None
    nSize: int = None

    def __init__(self, pType: Object, nIndex: int, nSize: int):
        self.pType = pType
        self.nIndex = nIndex
        self.nSize = nSize


class Field:
    pType: Object = None
    nIndex: int = None
    nSize: int = None

    def __init__(self, pType: Object, nIndex: int, nSize: int):
        self.pType = pType
        self.nIndex = nIndex
        self.nSize = nSize


class Function:
    pRetType: Object = None
    pParams: Object = None
    nIndex: int = None
    nParams: int = None
    nVars: int = None

    def __init__(self, pRetType: Object, pParams: Object, nIndex: int, nParams: int, nVars: int):
        self.pRetType = pRetType
        self.pParams = pParams
        self.nIndex = nIndex
        self.nParams = nParams
        self.nVars = nVars


class Array:
    pElemType: Object = None
    nNumElems: int = None
    nSize: int = None

    def __init__(self, pElemType: Object, nNumElems: int, nSize: int):
        self.pElemType = pElemType
        self.nNumElems = nNumElems
        self.nSize = nSize


class Struct:
    pFields: Object = None
    nSize: int = None

    def __init__(self, pFields: Object, nSize: int):
        self.pFields = pFields
        self.nSize = nSize


class Alias:
    pBaseType: Object = None
    nSize: int = None
    

    def __init__(self, pBaseType: Object, nSize: int):
        self.pBaseType = pBaseType
        self.nSize = nSize


class Type:
    pBaseType: Object = None
    nSize: int = None

    def __init__(self, pBaseType: Object, nSize: int):
        self.pBaseType = pBaseType
        self.nSize = nSize


class ID:
    name: int = None
    object: Object = None

    def __init__(self, name: int, object: Object = None):
        self.name = name
        self.object = object


class T:
    type: Object = None

    def __init__(self, type: Object):
        self.type = type


class LI:
    list: Object = None

    def __init__(self, list: Object):
        self.list = list


class BOOL:
    type: Object = None
    val: bool = None

    def __init__(
        self,
        val: bool,
        type: Object = bool_,
    ):
        self.val = val
        self.type = type
        
class E:
    type: Object = None

    def __init__(self, type: Object):
        self.type = type

class L:
    type: Object = None

    def __init__(self, type: Object):
        self.type = type

class R:
    type: Object = None

    def __init__(self, type: Object):
        self.type = type

class Y:
    type: Object = None

    def __init__(self, type: Object):
        self.type = type

class F:
    type: Object = None

    def __init__(self, type: Object):
        self.type = type

class LV:
    type: Object = None

    def __init__(self, type: Object):
        self.type = type

class MC:
    type: Object = None
    param: Object = None
    err: Object = None
        
    def __init__(self, type: Object, param: Object, err: Object):
        self.type = type
        self.param = param
        self.err = err

class MT:
    label: int = None
    def __init__(self, label: int):
        self.label = label   

class ME:
    label: int = None
    def __init__(self, label: int):
        self.label = label 

class MW:
    label: int = None
    def __init__(self, label: int):
        self.label = label 

class MA:
    label: int = None
    def __init__(self, label: int):
        self.label = label 

class LE:
    type: Object = None
    param: Object = None
    err: Object = None
    n: int = None
    def __init__(self, type: Object, param: Object, err: Object, n: int):
        self.type = type
        self.param = param
        self.err = err
        self.n = n


class TRUE:
    type: Object = None
    val: int = None
    def __init__(self, type: Object, val: int):
        self.type = type
        self.val = val

class FALSE:
    type: Object = None
    val: int = None
    def __init__(self, type: Object, val: int):
        self.type = type
        self.val = val



class CHR:
    type: Object
    pos: int = None
    val: str = None

    def __init__(self, val: str, pos: int, type: Object = char_):
        self.val = val
        self.pos = pos
        self.type = type


class STR:
    type: Object
    pos: int
    val: str

    def __init__(self, val: str, pos: int, type: Object = string_):
        self.val = val
        self.pos = pos
        self.type = type


class NUM:
    type: Object
    pos: int
    val: int

    def __init__(self, val: int, pos: int, type: Object = int_):
        self.val = val
        self.pos = pos
        self.type = type


class DC:
    list: Object

    def __init__(self, list: Object):
        self.list = list


class LP:
    list: Object

    def __init__(self, list: Object):
        self.list = list


class t_attrib:
    nont: States = None
    _ = None

    def __init__(self, nont: States, _=None):
        self.nont = nont
        self._ = _

        

