from __future__ import annotations
from enums import Kinds, States


class Object:
    nName: int = None
    pNext: Object = None
    eKind: Kinds = Kinds.NO_KIND_DEF_
    _ = None

    def __init__(self):
        pass

    def __init__(self,
                 nName: int = None,
                 pNext: Object = None,
                 eKind: Kinds = Kinds.NO_KIND_DEF_):
        self.nName = nName
        self.pNext = pNext
        self.eKind = eKind


class Var:
    pType: Object = None


class Param:
    pType: Object = None


class Field:
    pType: Object = None


class Function:
    pRetType: Object = None
    pParams: Object = None


class Array:
    pElemType: Object = None
    nNumElems: int


class Struct:
    pFields: Object = None


class Alias:
    pBaseType: Object = None


class t_attrib:
    nont: States = None
    _ = None
