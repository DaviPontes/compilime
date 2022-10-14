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


class Errors(Enum):
    ERR_REDECL = 0  #ok
    ERR_NOT_DECL = 1  #ok
    ERR_TYPE_EXPECTED = 2  #ok
    ERR_BOOL_TYPE_EXPECTED = 3
    ERR_TYPE_MISMATCH = 4
    ERR_INVALID_TYPE = 5
    ERR_KIND_NOT_STRUCT = 6
    ERR_FIELD_NOT_DECL = 7
    ERR_KIND_NOT_ARRAY = 8
    ERR_INVALID_INDEX_TYPE = 9
    ERR_KIND_NOT_VAR = 10
    ERR_KIND_NOT_FUNCTION = 11
    ERR_TOO_MANY_ARG = 12
    ERR_PARAM_TYPE = 13
    ERR_TOO_FEW_ARGS = 14
    ERR_RETURN_TYPE_MISMATCH = 15


class SemanticRules(Enum):
    IDD_Id = 0
    IDU_Id = 1
    ID_Id = 2
    NB = 3
    DT = 4
    DF = 5
    T_Integer = 6
    T_Char = 7
    T_Boolean = 8
    T_String = 9
    T_IDU = 10
    LI_IDD = 11
    LI_COMMA_IDD = 12
    DV_VAR = 13
    TRUE = 14
    FALSE = 15
    CHR = 16
    STR = 17
    NUM = 18
    DT_ARRAY = 19
    DT_ALIAS = 20
