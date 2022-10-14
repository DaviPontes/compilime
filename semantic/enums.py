from enum import Enum


# TODO: Change to syntactic folder
class States(Enum):
    P = 50
    LDE = 51
    DE = 52
    DF = 53
    DT = 54
    T = 55
    DC = 56
    LI = 57
    LP = 58
    B = 59
    LDV = 60
    LS = 61
    DV = 62
    S = 63
    E = 64
    LV = 65
    L = 66
    R = 67
    Y = 68
    F = 69
    LE = 70
    ID = 71
    TRUE = 72
    FALSE = 73
    CHR = 74
    STR = 75
    NUM = 76
    PLINHA = 77
    M = 78
    U = 79
    IDD = 80
    IDU = 81
    NB = 82
    MF = 83
    MC = 84
    NF = 85
    MT = 86
    ME = 87
    MW = 88


class Kinds(Enum):
    NO_KIND_DEF_ = -1
    VAR_ = 0
    PARAM_ = 1
    FUNCTION_ = 2
    FIELD_ = 3
    ARRAY_TYPE_ = 4
    STRUCT_TYPE_ = 5
    ALIAS_TYPE_ = 6
    SCALAR_TYPE_ = 7
    UNIVERSAL_ = 8


class SemanticRules(Enum):
    IDD_lalala = 10
