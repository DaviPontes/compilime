from typing import List
from objects import *

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