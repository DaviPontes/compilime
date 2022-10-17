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
    IDD_RULE = 30
    IDU_RULE = 31
    ID_RULE = 30
    NB_RULE = 57
    DT_STRUCT_RULE = 9
    DF_RULE = 7
    T_INTEGER_RULE = 68
    T_CHAR_RULE = 69
    T_BOOL_RULE = 70
    T_STRING_RULE = 71
    T_IDU_RULE = 72
    LI_IDD_RULE = 46
    LI_LI_IDD_RULE = 45
    DV_RULE = 11
    TRUE_RULE = 73
    FALSE_RULE = 29
    CHR_RULE = 2
    STR_RULE = 67
    NUM_RULE = 54
    DT_ARRAY_RULE = 8
    DT_IDD_RULE = 10
    DC_DC_LI_RULE = 4
    DC_DC_LI_T_RULE = 3
    LP_IDD_RULE = 48
    LP_LP_IDD_RULE = 47
    MF_RULE = 56
