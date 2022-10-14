from lexical.core import LexicalAnalyser
from semantic.enums import Errors, Kinds, SemanticRules, States 
from semantic.objects import BOOL, CHR, ID, LI, NUM, STR, T, Alias, Object, Var, Array, t_attrib
from semantic.scopeAnalyzer import Define, EndBlock, Find, NewBlock, RaiseError, Search
from semantic.typeAnalyzer import IS_TYPE_KIND, int_, char_, bool_, string_, universal_

StackSem = []

def SemanticAnalysis(lexical: LexicalAnalyser, ruleNumber: int):
    match SemanticRules(ruleNumber):
        case SemanticRules.IDD_Id:
            name = lexical.secondary_token
            p = Search(name)

            if(p != None):
                RaiseError(lexical, Errors.ERR_REDECL)
            else:
                p = Define(name)
            
            IDD_ = t_attrib(States.ID, ID(name, p))
            StackSem.append(IDD_)
        case SemanticRules.IDU_Id:
            name = lexical.secondary_token
            p = Find(name)

            if(p == None):
                RaiseError(lexical, Errors.ERR_NOT_DECL)
                p = Define(name)
            
            IDU_ = t_attrib(States.IDU, ID(name, p))
            StackSem.append(IDU_)
        case SemanticRules.ID_Id:
            name = lexical.secondary_token
            ID_ = t_attrib(States.ID, ID(name))
            StackSem.append(ID_)
        case SemanticRules.NB:
            NewBlock()
        case SemanticRules.DT:
            EndBlock()
        case SemanticRules.DF:
            EndBlock()
        case SemanticRules.T_Integer:
            T_ = t_attrib(States.T, T(int_))
            StackSem.append(T_)
        case SemanticRules.T_Char:
            T_ = t_attrib(States.T, T(char_))
            StackSem.append(T_)
        case SemanticRules.T_Boolean:
            T_ = t_attrib(States.T, T(bool_))
            StackSem.append(T_)
        case SemanticRules.T_String:
            T_ = t_attrib(States.T, T(string_))
            StackSem.append(T_)
        case SemanticRules.T_IDU:
            IDU_: t_attrib = StackSem.pop()
            p: Object = IDU_._.object

            if IS_TYPE_KIND(p.eKind) or p.eKind == Kinds.UNIVERSAL_:
                T_ = t_attrib(States.T, T(p))
            else:
                T_ = t_attrib(States.T, universal_)
                RaiseError(Errors.ERR_TYPE_EXPECTED)
            StackSem.append(T_)
        case SemanticRules.LI_IDD:
            IDD_: t_attrib = StackSem.pop()
            LI_ = t_attrib(States.LI, LI(IDD_._.object))
            StackSem.append(LI_)
        case SemanticRules.LI_COMMA_IDD:
            IDD_: t_attrib = StackSem.pop()
            LI1_: t_attrib = StackSem.pop()
            LI0_ = t_attrib(States.LI, LI(LI1_._.object))
            StackSem.append(LI0_)
        case SemanticRules.DV_VAR:
            T_: t_attrib = StackSem.pop()
            LI_: t_attrib = StackSem.pop()
            
            p:Object = LI_._.list
            t:Object = T_._.type

            while(p != None and p.eKind == Kinds.NO_KIND_DEF_):
                p.eKind = Kinds.VAR_
                p._ = Var(t)
                p = p.pNext
            # TODO: Precisa adicionar DV_ na pilha?
        case SemanticRules.TRUE:
            TRUE_ = t_attrib(States.TRUE, BOOL(True))
            StackSem.append(TRUE_)
        case SemanticRules.FALSE:
            FALSE_ = t_attrib(States.TRUE, BOOL(False))
            StackSem.append(FALSE_)
        case SemanticRules.CHR:
            pos = lexical.secondary_token
            CHR_ = t_attrib(States.CHR, CHR(lexical.get_const(pos), pos))
            StackSem.append(CHR_)
        case SemanticRules.STR:
            pos = lexical.secondary_token
            STR_ = t_attrib(States.STR, STR(lexical.get_const(pos), pos))
            StackSem.append(STR_)
        case SemanticRules.NUM:
            pos = lexical.secondary_token
            NUM_ = t_attrib(States.NUM, NUM(lexical.get_const(pos), pos))
            StackSem.append(NUM_)
        case SemanticRules.DT_ARRAY:
            T_ = StackSem.pop()
            NUM_ = StackSem.pop()
            IDD_ = StackSem.pop()

            p:Object = IDD_._.object
            t:Object = T_._.type
            n:int = NUM_._.val

            p.eKind = Kinds.ARRAY_TYPE_
            p._ = Array(t, n)
            # TODO: Precisa adicionar DT_ na pilha?
        case SemanticRules.DT_ALIAS:
            T_ = StackSem.pop()
            IDD_ = StackSem.pop()

            p:Object = IDD_._.object
            t:Object = T_._.type

            p.eKind = Kinds.ALIAS_TYPE_
            p._ = Alias(t)
            # TODO: Precisa adicionar DT_ na pilha?
        
        

            

        
        