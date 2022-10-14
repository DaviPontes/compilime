from enums import Kinds
from objects import Object

int_ = Object(-1, None, Kinds.SCALAR_TYPE_)
char_ = Object(-1, None, Kinds.SCALAR_TYPE_)
bool_ = Object(-1, None, Kinds.SCALAR_TYPE_)
string_ = Object(-1, None, Kinds.SCALAR_TYPE_)
universal_ = Object(-1, None, Kinds.UNIVERSAL_)


def IS_TYPE_KIND(eKind: Kinds):
    return eKind in [
        Kinds.ARRAY_TYPE_, Kinds.STRUCT_TYPE_, Kinds.ALIAS_TYPE_,
        Kinds.SCALAR_TYPE_
    ]
