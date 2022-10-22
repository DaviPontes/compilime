from typing import List
from lexical.core import LexicalAnalyser
from objects import *
from semantic.enums import Errors

symbolTable: List[Object] = []
symbolTableLast: List[Object] = []
nCurrentLevel: int = -1


def NewBlock() -> int:
    global symbolTable, symbolTableLast, nCurrentLevel
    nCurrentLevel += 1
    symbolTable[nCurrentLevel] = None
    symbolTableLast[nCurrentLevel] = None
    return nCurrentLevel


def EndBlock() -> int:
    global nCurrentLevel
    nCurrentLevel -= 1
    return nCurrentLevel


def Define(aName: int) -> Object:
    global symbolTable, symbolTableLast, nCurrentLevel

    obj = Object(aName)

    if symbolTable[nCurrentLevel] == None:
        symbolTable[nCurrentLevel] = obj
        symbolTableLast[nCurrentLevel] = obj
    else:
        symbolTable[nCurrentLevel].pNext = obj
        symbolTableLast[nCurrentLevel] = obj

    return obj


def Search(aName: int) -> Object:
    global symbolTable, symbolTableLast, nCurrentLevel

    obj = symbolTable[nCurrentLevel]

    while obj != None:
        if obj.nName == aName:
            break
        obj = obj.pNext

    return obj


def Find(aName: int) -> Object:
    global symbolTable, symbolTableLast, nCurrentLevel

    obj = None
    for i in range(nCurrentLevel, -1, -1):
        obj = symbolTable[i]
        while obj != None:
            if obj.nName == aName:
                break
            obj = obj.pNext
        if obj != None:
            break

    return obj

def RaiseError(lexical: LexicalAnalyser, errCode: Errors):
    print(f"Raised error on line {lexical.line} - ")
    match errCode:
        case Errors.ERR_REDECL:
            print("Variable already declared")
        case Errors.ERR_NOT_DECL:
            print("Variable not declared")
        case Errors.ERR_TYPE_EXPECTED:
            print("Type expected")
        case Errors.ERR_BOOL_TYPE_EXPECTED:
            print("Type boolean expected")
        case Errors.ERR_TYPE_MISMATCH:
            print("Type not expected")
        case Errors.INVALID_TYPE:
            print("Invalid type")
        case Errors.ERR_KIND_NOT_STRUCT:
            print("Expected struct type")
        case Errors.ERR_FIELD_NOT_DECL:
            print("Field not declared")
        case Errors.ERR_KIND_NOT_ARRAY:
            print("Expected array type")
        case Errors.ERR_INVALID_INDEX_TYPE:
            print("Invalid Index type")
        case Errors.ERR_KIND_NOT_VAR:
            print("Expected Var type")
        case Errors.ERR_KIND_NOT_FUNCTION :
            print("Expected function type")
        case Errors.ERR_TOO_MANY_ARG:
            print("Too many parameters")
        case Errors.ERR_PARAM_TYPE:
            print("Parameter type not expected")
        case Errors.ERR_TOO_FEW_ARGS :
            print("Too few parameters")
        case Errors.ERR_RETURN_TYPE_MISMATCH :
            print("Invalid return type")
