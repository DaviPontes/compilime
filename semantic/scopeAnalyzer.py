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