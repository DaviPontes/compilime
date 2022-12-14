from enum import Enum


class KeyWords(Enum):
    # Reserved Words
    ARRAY = 0
    BOOLEAN = 1
    BREAK = 2
    CHAR = 3
    CONTINUE = 4
    DO = 5
    ELSE = 6
    FALSE = 7
    FUNCTION = 8
    IF = 9
    INTEGER = 10
    OF = 11
    STRING = 12
    STRUCT = 13
    TRUE = 14
    TYPE = 15
    VAR = 16
    WHILE = 17

    # Symbols
    COLON = 18
    SEMI_COLON = 19
    COMMA = 20
    EQUALS = 21
    LEFT_SQUARE = 22
    RIGHT_SQUARE = 23
    LEFT_BRACES = 24
    RIGHT_BRACES = 25
    LEFT_PARENTHESIS = 26
    RIGHT_PARENTHESIS = 27
    AND = 28
    OR = 29
    LESS_THAN = 30
    GREATER_THAN = 31
    LESS_OR_EQUAL = 32
    GREATER_OR_EQUAL = 33
    NOT_EQUAL = 34
    EQUAL_EQUAL = 35
    PLUS = 36
    PLUS_PLUS = 37
    MINUS = 38
    MINUS_MINUS = 39
    TIMES = 40
    DIVIDE = 41
    DOT = 42
    NOT = 43

    # Regular Tokens
    CHARACTER = 44
    NUMERAL = 45
    STRINGVAL = 46
    ID = 47

    # Unknown Tokens
    UNKNOWN = 48
    EOF = 49


# Reserved Words
reserved_words = [
    "array",
    "boolean",
    "break",
    "char",
    "continue",
    "do",
    "else",
    "false",
    "function",
    "if",
    "integer",
    "of",
    "string",
    "struct",
    "true",
    "type",
    "var",
    "while"
]
