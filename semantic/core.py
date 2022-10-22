from lexical.core import LexicalAnalyser
from semantic.enums import Errors, Kinds, SemanticRules, States 
from semantic.objects import BOOL, CHR, DC, ID, LI, LP, NUM, STR, T, Alias, Field, Function, Object, Param, Struct, Var, Array, t_attrib
from semantic.scopeAnalyzer import Define, EndBlock, Find, NewBlock, RaiseError, Search
from semantic.typeAnalyzer import IS_TYPE_KIND, int_, char_, bool_, string_, universal_

StackSem = []
label = 0

def SemanticAnalysis(lexical: LexicalAnalyser, ruleNumber: int):
    
    code_generation = open("generated_code.txt", "a+")
    match SemanticRules(ruleNumber):
        case SemanticRules.IDD_RULE:
            name = lexical.secondary_token
            p = Search(name)

            if(p != None):
                RaiseError(lexical, Errors.ERR_REDECL)
            else:
                p = Define(name)
            
            IDD_ = t_attrib(States.ID, ID(name, p))
            StackSem.append(IDD_)
        case SemanticRules.IDU_RULE:
            name = lexical.secondary_token
            p = Find(name)

            if(p == None):
                RaiseError(lexical, Errors.ERR_NOT_DECL)
                p = Define(name)
            
            IDU_ = t_attrib(States.IDU, ID(name, p))
            StackSem.append(IDU_)
        case SemanticRules.ID_RULE:
            name = lexical.secondary_token
            ID_ = t_attrib(States.ID, ID(name))
            StackSem.append(ID_)
        case SemanticRules.NB_RULE:
            NewBlock()
            NB_ = t_attrib(States.NB)
            StackSem(NB_)
        case SemanticRules.DF_RULE:
            B_ = StackSem.pop()
            MF_ = StackSem.pop()
            T_ = StackSem.pop()
            LP_ = StackSem.pop()
            NB_ = StackSem.pop()
            IDD_ = StackSem.pop()
            EndBlock()
            DF_ = t_attrib(States.DF)
            StackSem(DF_)
        case SemanticRules.T_INTEGER_RULE:
            T_ = t_attrib(States.T, T(int_))
            StackSem.append(T_)
        case SemanticRules.T_CHAR_RULE:
            T_ = t_attrib(States.T, T(char_))
            StackSem.append(T_)
        case SemanticRules.T_BOOL_RULE:
            T_ = t_attrib(States.T, T(bool_))
            StackSem.append(T_)
        case SemanticRules.T_STRING_RULE:
            T_ = t_attrib(States.T, T(string_))
            StackSem.append(T_)
        case SemanticRules.T_IDU_RULE:
            IDU_: t_attrib = StackSem.pop()
            p: Object = IDU_._.object

            if IS_TYPE_KIND(p.eKind) or p.eKind == Kinds.UNIVERSAL_:
                T_ = t_attrib(States.T, T(p))
            else:
                T_ = t_attrib(States.T, universal_)
                RaiseError(Errors.ERR_TYPE_EXPECTED)
            StackSem.append(T_)
        case SemanticRules.LI_IDD_RULE:
            IDD_: t_attrib = StackSem.pop()
            LI_ = t_attrib(States.LI, LI(IDD_._.object))
            StackSem.append(LI_)
        case SemanticRules.LI_COMMA_RULE:
            IDD_: t_attrib = StackSem.pop()
            LI1_: t_attrib = StackSem.pop()
            LI0_ = t_attrib(States.LI, LI(LI1_._.object))
            StackSem.append(LI0_)
        case SemanticRules.DV_VAR_RULE:
            T_: t_attrib = StackSem.pop()
            LI_: t_attrib = StackSem.pop()
            
            p:Object = LI_._.list
            t:Object = T_._.type

            while(p != None and p.eKind == Kinds.NO_KIND_DEF_):
                p.eKind = Kinds.VAR_
                p._ = Var(t)
                p = p.pNext
            
            DV_ = t_attrib(States.DV)
            StackSem.append(DV_)
        case SemanticRules.TRUE_RULE:
            TRUE_ = t_attrib(States.TRUE, BOOL(True))
            StackSem.append(TRUE_)
        case SemanticRules.FALSE_RULE:
            FALSE_ = t_attrib(States.TRUE, BOOL(False))
            StackSem.append(FALSE_)
        case SemanticRules.CHR_RULE:
            pos = lexical.secondary_token
            CHR_ = t_attrib(States.CHR, CHR(lexical.get_const(pos), pos))
            StackSem.append(CHR_)
        case SemanticRules.STR_RULE:
            pos = lexical.secondary_token
            STR_ = t_attrib(States.STR, STR(lexical.get_const(pos), pos))
            StackSem.append(STR_)
        case SemanticRules.NUM_RULE:
            pos = lexical.secondary_token
            NUM_ = t_attrib(States.NUM, NUM(lexical.get_const(pos), pos))
            StackSem.append(NUM_)
        case SemanticRules.DT_ARRAY_RULE:
            T_ = StackSem.pop()
            NUM_ = StackSem.pop()
            IDD_ = StackSem.pop()

            p:Object = IDD_._.object
            t:Object = T_._.type
            n:int = NUM_._.val

            p.eKind = Kinds.ARRAY_TYPE_
            p._ = Array(t, n)

            DT_ = t_attrib(States.DT)
            StackSem.append(DT_)
        case SemanticRules.DT_ALIAS_RULE:
            T_ = StackSem.pop()
            IDD_ = StackSem.pop()

            p:Object = IDD_._.object
            t:Object = T_._.type

            p.eKind = Kinds.ALIAS_TYPE_
            p._ = Alias(t)

            DT_ = t_attrib(States.DT)
            StackSem.append(DT_)
        case SemanticRules.DC_LI_RULE:
            T_ = StackSem.pop()
            LI_ = StackSem.pop()

            p:Object = LI_._.list
            t:Object = T_._.type

            while p != None and p.eKind == Kinds.NO_KIND_DEF_:
                p.eKind = Kinds.FIELD_
                p._ = Field(t)
                p = p.pNext

            DC_ = t_attrib(States.DC, DC(LI_.list))
            StackSem.append(DC_)
        case SemanticRules.DC_DC_RULE:
            T_ = StackSem.pop()
            LI_ = StackSem.pop()
            DC1_ = StackSem.pop()

            p:Object = LI_._.list
            t:Object = T_._.type

            while p != None and p.eKind == Kinds.NO_KIND_DEF_:
                p.eKind = Kinds.FIELD_
                p._ = Field(t)
                p = p.pNext

            DC0_ = t_attrib(States.DC, DC(DC1_.list))
            StackSem.append(DC0_)
        case SemanticRules.DT_STRUCT_RULE:
            DC_ = StackSem.pop()
            NB_ = StackSem.pop()
            IDD_ = StackSem.pop()

            p: Object = IDD_._.object

            p.eKind = Kinds.STRUCT_TYPE_
            p._ = Struct(DC_._.list)

            EndBlock()

            DT_ = t_attrib(States.DT)
            StackSem.append(DT_)
        case SemanticRules.LP_IDD_RULE:
            T_ = StackSem.pop()
            IDD_ = StackSem.pop()

            p: Object = IDD_._.object
            t: Object = T_._.type

            p.eKind = Kinds.PARAM_
            p._ = Param(t)

            LP_ = t_attrib(States.LP, LP(p))
            StackSem.append(LP_)
        case SemanticRules.LP_LP_RULE:
            T_ = StackSem.pop()
            IDD_ = StackSem.pop()
            LP1_ = StackSem.pop()

            p: Object = IDD_._.object
            t: Object = T_._.type

            p.eKind = Kinds.PARAM_
            p._ = Param(t)

            LP0_ = t_attrib(States.LP, LP(LP1_._.list))
            StackSem.append(LP0_)
        case SemanticRules.MF_RULE:
            T_:t_attrib = StackSem[len(StackSem) - 1]
            LP_:t_attrib = StackSem[len(StackSem) - 2]
            NB_:t_attrib = StackSem[len(StackSem) - 3]
            IDD_:t_attrib = StackSem[len(StackSem) - 4]

            f:Object = IDD_._.object

            f.eKind = Kinds.ARRAY_TYPE_
            f._ = Function(T_._.type, LP_._.list)
