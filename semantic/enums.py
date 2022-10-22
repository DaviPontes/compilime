from enum import Enum


# TODO: Change to syntactic folder
class States(Enum):
    NOT = 43
    NOT_EQUAL = 34
    AND = 28
    LEFT_PARENTHESIS = 26
    RIGHT_PARENTHESIS = 27
    TIMES = 40
    PLUS = 36
    PLUS_PLUS = 37
    COMMA = 20
    MINUS = 38
    MINUS_MINUS = 39
    DOT = 42
    DIVIDE = 41
    COLON = 18
    SEMI_COLON = 19
    LESS_THAN = 30
    LESS_OR_EQUAL = 32
    EQUALS = 21
    EQUAL_EQUAL = 35
    GREATER_THAN = 31
    GREATER_OR_EQUAL = 33
    LEFT_SQUARE = 22
    RIGHT_SQUARE = 23
    ARRAY = 0
    BOOLEAN = 1
    BREAK = 2
    CHAR = 3
    CONTINUE = 4
    DO = 5
    ELSE = 6
    FUNCTION = 8
    ID = 47
    IF = 9
    INTEGER = 10
    OF = 11
    STRING = 12
    STRUCT = 13
    TYPE = 15
    VAR = 16
    WHILE = 17
    LEFT_BRACES = 24
    OR = 29
    RIGHT_BRACES = 25
    EOF = 49
    CHR = 44
    FALSE = 7
    NUM = 45
    STR = 46
    TRUE = 14
    UNKNOWN = 48
    DC = 56
    DE = 52
    DF = 53
    DT = 54
    DV = 62
    E = 64
    F = 69
    IDD = 80
    IDU = 81
    L = 66
    LDE = 51
    LDV = 60
    LE = 70
    LI = 57
    LP = 58
    LS = 61
    LV = 65
    P = 50
    R = 67
    S = 63
    T = 55
    Y = 68
    C = 82
    N = 83
    s = 84
    true = 85
    false = 86
    B = 59
    MC = 87
    MF = 88
    NB = 89
    NF = 90
    id = 91


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
    P_LDE_RULE = 60 #P LDE
    LDE_LDE_RULE = 40 #LDE LDE DE
    LDE_DE_RULE = 41 #LDE DE
    DE_DF_RULE = 5 #DE DF
    DE_DT_RULE = 6 #DE DT
    T_INTEGER_RULE = 73 #T integer
    T_CHAR_RULE = 74 #T char
    T_BOOL_RULE = 75 #T boolean
    T_STRING_RULE = 76 #T string
    T_IDU_RULE = 77 #T IDU
    DT_ARRAY_RULE = 8 #DT type IDD = array [ NUM ] of T
    DT_STRUCT_RULE = 9 #DT type IDD = struct NB { DC }
    DT_ALIAS_RULE = 10 #DT type IDD = T
    DC_DC_RULE = 3 #DC DC ; LI : T
    DC_LI_RULE = 4 #DC LI : T
    DF_RULE = 7 #DF function IDD NB ( LP ) : T MF B
    LP_LP_RULE = 48 #LP LP , IDD : T
    LP_IDD_RULE = 49 #LP IDD : T
    B_LS_RULE = 1 #B { LDV LS }
    LDV_LDV_RULE = 42 #LDV LDV DV
    LDV_DV_RULE = 43 #LDV DV
    LS_LS_RULE = 50 #LS LS S
    LS_S_RULE = 51 #LS S
    DV_VAR_RULE = 11 #DV var LI : T ;
    LI_COMMA_RULE = 46 #LI LI , IDD
    LI_IDD_RULE = 47 #LI IDD
    M_IF_RULE = 64 #S if ( E ) S
    M_IF_ELSE_M_RULE = 65 #S if ( E ) S else S
    M_WHILE_RULE = 66 #S while ( E ) S
    M_DO_WHILE_RULE = 67 #S do S while ( E ) ;
    M_BLOCK_RULE = 68 #S B
    M_E_SEMICOLON_RULE = 69 #S LV = E ;
    M_BREAK_RULE = 70 #S break ;
    M_CONTINUE_RULE = 71 #S continue ;
    E_AND_RULE = 12 #E E && L
    E_OR_RULE = 13 #E E || L
    E_L_RULE = 14 #E L
    L_LESS_THAN_RULE = 33 #L L < R
    L_GREATER_THAN_RULE = 34 #L L > R
    L_LESS_EQUAL_RULE = 35 #L L <= R
    L_GREATER_EQUAL_RULE = 36 #L L >= R
    L_EQUAL_EQUAL_RULE = 37 #L L == R
    L_NOT_EQUAL_RULE = 38 #L L != R
    L_R_RULE = 39 #L R
    R_PLUS_RULE = 61 #R R + Y
    R_MINUS_RULE = 62 #R R - Y
    R_Y_RULE =63 #R Y
    Y_TIMES_RULE = 79 #Y Y * F
    Y_DIVIDE_RULE = 80 #Y Y / F
    Y_F_RULE = 81 #Y F
    F_LV_RULE = 15 #F LV
    F_LEFT_PLUS_PLUS_RULE = 16 #F ++ LV
    F_LEFT_MINUS_MINUS_RULE = 17 #F -- LV
    F_RIGHT_PLUS_PLUS_RULE = 18 #F LV ++
    F_RIGHT_MINUS_MINUS_RULE = 19 #F LV --
    F_PARENTHESIS_E_RULE = 20 #F ( E )
    F_IDU_MC_RULE = 21 #F IDU MC ( LE )
    F_MINUS_F_RULE = 22 #F - F
    F_NOT_F_RULE = 23 #F ! F
    F_TRUE_RULE = 24 #F TRUE
    F_FALSE_RULE = 25 #F FALSE
    F_CHR_RULE = 26 #F CHR
    F_STR_RULE = 27 #F STR
    F_NUM_RULE = 28 #F NUM
    LE_LE_RULE = 44 #LE LE , E
    LE_E_RULE = 45 #LE E
    LV_DOT_RULE =52 #LV LV . IDU
    LV_SQUARE_RULE = 53 #LV LV [ E ]
    LV_IDU_RULE = 54 #LV IDU
    ID_RULE = 30 #ID id
    IDD_RULE = 31 # IDD id
    IDU_RULE = 32 #IDU id
    TRUE_RULE = 78 #TRUE true
    FALSE_RULE = 29 #FALSE false
    CHR_RULE = 2 #CHR c
    STR_RULE = 72 #STR s
    NUM_RULE = 59 #NUM n
    MC_RULE = 55
    MF_RULE = 56
    NB_RULE = 57
    NF_RULE = 58
    MT_RULE = 82
    ME_RULE = 83
    MW_RULE = 84
