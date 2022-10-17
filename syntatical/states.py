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

table_columns = [
    NOT, NOT_EQUAL, AND, LEFT_PARENTHESIS, RIGHT_PARENTHESIS, TIMES, PLUS,
    PLUS_PLUS, COMMA, MINUS, MINUS_MINUS, DOT, DIVIDE, COLON, SEMI_COLON,
    LESS_THAN, LESS_OR_EQUAL, EQUALS, EQUAL_EQUAL, GREATER_THAN,
    GREATER_OR_EQUAL, LEFT_SQUARE, RIGHT_SQUARE, ARRAY, BOOLEAN, BREAK, C,
    CHAR, CONTINUE, DO, ELSE, false, FUNCTION, ID, IF, INTEGER, N, OF, s,
    STRING, STRUCT, true, TYPE, VAR, WHILE, LEFT_BRACES, OR, RIGHT_BRACES, EOF,
    B, CHR, DC, DE, DF, DT, DV, E, F, FALSE, id, IDD, IDU, L, LDE, LDV, LE, LI,
    LP, LS, LV, MC, MF, NB, NF, NUM, P, R, S, STR, T, TRUE, Y
]

import csv


def init_table():
    action_table = list(
        csv.reader(open("syntatical/action_table.csv", "r"), delimiter=","))
    for i in range(1, 160):
        for j in range(78):
            if j == 0:
                action_table[i][j] = str(action_table[i][j])
            elif action_table[i][j] == '':
                action_table[i][j] = 0
            elif action_table[i][j].startswith('r'):
                action_table[i][j] = -59
            elif action_table[i][j] == 'a':
                action_table[i][j] = 'acc'
            else:
                action_table[i][j] = int(action_table[i][j])
    return action_table


LEN = [
    4, 1, 5, 3, 1, 1, 10, 9, 8, 4, 5, 3, 3, 1, 1, 2, 2, 2, 2, 3, 5, 2, 2, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 2, 1, 2, 1, 3, 1, 3, 1, 5, 3, 2,
    1, 3, 4, 1, 0, 0, 0, 0, 1, 1, 3, 3, 1, 5, 7, 5, 7, 2, 4, 2, 2, 1, 1, 1, 1,
    1, 1, 1, 3, 3, 1
]

LEFT = [
    B, CHR, DC, DC, DE, DE, DF, DT, DT, DT, DV, E, E, E, F, F, F, F, F, F, F,
    F, F, F, F, F, F, F, FALSE, ID, IDD, IDU, L, L, L, L, L, L, L, LDE, LDE,
    LDV, LDV, LE, LE, LI, LI, LP, LP, LS, LS, LV, LV, LV, MC, MF, NB, NF, NUM,
    P, R, R, R, S, S, S, S, S, S, S, S, STR, T, T, T, T, T, TRUE, Y, Y, Y
]


def token_tab(a):
    return table_columns.index(a) + 1
