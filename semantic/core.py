from lexical.core import LexicalAnalyser
from semantic.enums import Errors, Kinds, SemanticRules, States 
from semantic.objects import BOOL, CHR, DC, ID, LI, LP, NUM, STR, T, Alias, Field, Function, Object, Param, Struct, Var, Array, t_attrib
from semantic.scopeAnalyzer import Define, EndBlock, Find, NewBlock, RaiseError, Search
from semantic.typeAnalyzer import IS_TYPE_KIND, int_, char_, bool_, string_, universal_

StackSem = []
label = 0

def SemanticAnalysis(lexical: LexicalAnalyser, ruleNumber: int):
    
 
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
            f.eKind = Kinds.FUNCTION_
            f._ = Function(T_._.type,LP_._.list,f._.nIndex,LP_.nSize,LP_.nSize)
            print("BEGIN_FUNC "+str(f._.nIndex)+" "+str(f._.nParams)+"\n")
        case SemanticRules.NF_RULE:
            IDD_ = StackSem[-1]
            f = IDD_._.object
            f.eKind = FUNCTION_
            f._ = Function(None,None)
            NewBlock()
        case SemanticRules.U_IF_RULE:
            MT_ = StackSem.pop()
            E_ = StackSem.pop()
            t = E_._.type
            if not type_check(t,bool_):
                RaiseError(lexical, ERR_BOOL_TYPE_EXPECTED)
            print("L"+str(MT_._.label)+"\n")
        case SemanticRules.U_IF_ELSE_U_RULE:
            ME_ = StackSem.pop()
            MT_ = StackSem.pop()
            E_ = StackSem.pop()
            t = E_._.type
            if not type_check(t,bool_):
                RaiseError(lexical, ERR_BOOL_TYPE_EXPECTED)
            print("L"+str(ME_._.label)+"\n")
        case SemanticRules.M_IF_ELSE_M_RULE:
            ME_ = StackSem.pop()
            MT_ = StackSem.pop()
            E_ = StackSem.pop()
            t = E_._.type
            if not type_check(t,bool_):
                RaiseError(lexical, ERR_BOOL_TYPE_EXPECTED)
            print("L"+str(ME_._.label)+"\n")
        case SemanticRules.M_WHILE_RULE:
            MT_ = StackSem.pop()
            E_ = StackSem.pop()
            MW_ = StackSem.pop()
            print(E_)
            print(E_._)
            t = E_._.type
            if not type_check(t,bool_):
                RaiseError(lexical, ERR_BOOL_TYPE_EXPECTED)
            print("\tJMP_BW L"+'0'+"\nL"+str(MT_._.label)+"\n")        
        case SemanticRules.M_DO_WHILE_RULE:
            E_ = StackSem.pop()
            MW_ = StackSem.pop()
            t = E_._.type
            if not type_check(t,bool_):
                RaiseError(lexical, ERR_BOOL_TYPE_EXPECTED)
            print("\tNOT\n\tTJMP_BW L"+str(MW_._.label)+"\n")  
        case SemanticRules.E_AND_RULE:
            L_ = StackSem.pop()
            E1_ = StackSem.pop()
            if not type_check(E1_._.type,bool_):
                RaiseError(lexical, ERR_BOOL_TYPE_EXPECTED)
            if not type_check(L_._.type,bool_):
                RaiseError(lexical, ERR_BOOL_TYPE_EXPECTED)
            E0_ = t_attrib(E,None,E(bool_))
            StackSem.append(E0_)
            print("\tAND"+"\n")
        case SemanticRules.E_OR_RULE:
            L_ = StackSem.pop()
            E1_ = StackSem.pop()
            if not type_check(E1_._.type,bool_):
                RaiseError(lexical, ERR_BOOL_TYPE_EXPECTED)
            if not type_check(L_._.type,bool_):
                RaiseError(lexical, ERR_BOOL_TYPE_EXPECTED)
            E0_ = t_attrib(E,None,E(bool_))
            StackSem.append(E0_)
            print("\tOR"+"\n")
        case SemanticRules.E_L_RULE:
            L_ = StackSem.pop()
            E_ = t_attrib(E,None,E(L_._.type))
            StackSem.append(E_)
        case SemanticRules.L_LESS_THAN_RULE:
            R_ = StackSem.pop()
            L1_ = StackSem.pop()
            if not type_check(L1_._.type,R_._.type):
                RaiseError(lexical, ERR_TYPE_MISMATCH)
            L0_ = t_attrib(L,None,L(bool_))
            StackSem.append(L0_)
            print("\tLT"+"\n")
        case SemanticRules.L_GREATER_THAN_RULE:
            R_ = StackSem.pop()
            L1_ = StackSem.pop()
            if not type_check(L1_._.type,R_._.type):
                RaiseError(lexical, ERR_TYPE_MISMATCH)
            L0_ = t_attrib(L,None,bool_)
            StackSem.append(L0_)
            print("\tGT"+"\n")
        case SemanticRules.L_LESS_EQUAL_RULE:
            R_ = StackSem.pop()
            L1_ = StackSem.pop()
            if not type_check(L1_._.type,R_._.type):
                RaiseError(lexical, ERR_TYPE_MISMATCH)
            L0_ = t_attrib(L,None,bool_)
            StackSem.append(L0_)
            print("\tLE"+"\n")
        case SemanticRules.L_GREATER_EQUAL_RULE:
            R_ = StackSem.pop()
            L1_ = StackSem.pop()
            if not type_check(L1_._.type,R_._.type):
                RaiseError(lexical, ERR_TYPE_MISMATCH)
            L0_ = t_attrib(L,None,bool_)
            StackSem.append(L0_)
            print("\tGE"+"\n")
        case SemanticRules.L_EQUAL_EQUAL_RULE:
            R_ = StackSem.pop()
            L1_ = StackSem.pop()
            if not type_check(L1_._.type,R_._.type):
                RaiseError(lexical, ERR_TYPE_MISMATCH)
            L0_ = t_attrib(L,None,bool_)
            StackSem.append(L0_)
            print("\tEQ"+"\n")
        case SemanticRules.L_NOT_EQUAL_RULE:
            R_ = StackSem.pop()
            L1_ = StackSem.pop()
            if not type_check(L1_._.type,R_._.type):
                RaiseError(lexical, ERR_TYPE_MISMATCH)
            L0_ = t_attrib(L,None,bool_)
            StackSem.append(L0_)
            print("\tNE"+"\n")
        case SemanticRules.L_R_RULE:
            R_ = StackSem.pop()
            L_ = t_attrib(L,None,L(R_._.type))
            StackSem.append(L_)
        case SemanticRules.R_PLUS_RULE:
            Y_ = StackSem.pop()
            R1_ = StackSem.pop()
            if not type_check(R1_._.type,Y_._.type):
                RaiseError(lexical, ERR_TYPE_MISMATCH)
            if not type_check(R1_._.type,int_) and not type_check(R1_._.type,string_):
                RaiseError(lexical, ERR_INVALID_TYPE)
            R0_ = t_attrib(R,None,R(R1_._.type))
            StackSem.append(R0_)
            print("\tADD"+"\n")
        case SemanticRules.R_MINUS_RULE:
            Y_ = StackSem.pop()
            R1_ = StackSem.pop()
            if not type_check(R1_._.type,Y_._.type):
                RaiseError(lexical, ERR_TYPE_MISMATCH)
            if not type_check(R1_._.type,int_):
                RaiseError(lexical, ERR_INVALID_TYPE)
            R0_ = t_attrib(R,None,R(R1_._.type))
            StackSem.append(R0_)
            print("\tSUB"+"\n")
        case SemanticRules.R_Y_RULE:
            Y_ = StackSem.pop()
            R_ = t_attrib(R,None,R(Y_._.type))
            StackSem.append(R_)
        case SemanticRules.Y_TIMES_RULE:
            F_ = StackSem.pop()
            Y1_ = StackSem.pop()
            if not type_check(Y1_._.type,F_._.type):
                RaiseError(lexical, ERR_TYPE_MISMATCH)
            if not type_check(Y1_._.type,int_):
                RaiseError(lexical, ERR_INVALID_TYPE)
            Y0_ = t_attrib(Y,None,Y(Y1_._.type))
            StackSem.append(Y0_)
            print("\tMUL"+"\n")
        case SemanticRules.Y_DIVIDE_RULE:
            F_ = StackSem.pop()
            Y1_ = StackSem.pop()
            if not type_check(Y1_._.type,F_._.type):
                RaiseError(lexical, ERR_TYPE_MISMATCH)
            if not type_check(Y1_._.type,int_):
                RaiseError(lexical, ERR_INVALID_TYPE)
            Y0_ = t_attrib(Y,None,Y(Y1_._.type))
            StackSem.append(Y0_)
            print("\tDIV"+"\n")
        case SemanticRules.Y_F_RULE:
            F_ = StackSem.pop()
            Y_ = t_attrib(Y,None,Y(F_._.type))
            StackSem.append(Y_)
        case SemanticRules.F_LV_RULE:
            LV_ = StackSem.pop()
            n = 0
            F_ = t_attrib(F,None,F(LV_._.type))
            StackSem.append(F_)
            print("\tDE_REF "+str(n)+"\n")
        case SemanticRules.F_LEFT_PLUS_PLUS_RULE:
            LV_ = StackSem.pop()
            t = LV_._.type
            if not type_check(t,int_):
                RaiseError(lexical, ERR_INVALID_TYPE)
            F_ = t_attrib(F,None,F(int_))
            print("\tDUP\n\tDUP\n\tDE_REF 1"+"\n")
            print("\tINC\n\tSTORE REF 1\n\tDE_REF 1"+"\n")
        case SemanticRules.F_LEFT_MINUS_MINUS_RULE:
            LV_ = StackSem.pop()
            t = LV_._.type
            if not type_check(t,int_):
                RaiseError(lexical, ERR_INVALID_TYPE)
            F_ = t_attrib(F,None,F(LV_._.type))
            StackSem.append(F_)
            print("\tDUP\n\tDUP\n\tDE_REF 1"+"\n")
            print("\tDEC\n\tSTORE_REF 1\n\tDE_REF 1"+"\n")
        case SemanticRules.F_RIGHT_PLUS_PLUS_RULE:
            LV_ = StackSem.pop()
            t = LV_._.type
            if not type_check(t,int_):
                RaiseError(lexical, ERR_INVALID_TYPE)
            F_ = t_attrib(F,None,F(LV_._.type))
            StackSem.append(F_)
            print("\tDUP\n\tDUP\n\tDE_REF 1"+"\n")
            print("\tINC\n\tSTORE_REF 1\n\tDE_REF 1"+"\n")
            print("\tDEC"+"\n")
        case SemanticRules.F_RIGHT_MINUS_MINUS_RULE:
            LV_ = StackSem.pop()
            t = LV_._.type
            if not type_check(t,int_):
                RaiseError(lexical, ERR_INVALID_TYPE)
            F_ = t_attrib(F,None,F(t))
            StackSem.append(F_)
            print("\tDUP\n\tDUP\n\tDE_REF 1"+"\n")
            print("\tDEC\n\tSTORE_REF 1\n\tDE_REF 1"+"\n")
            print("\tINC"+"\n")
        case SemanticRules.F_PARENTHESIS_E_RULE:
            E_ = StackSem.pop()
            F_ = t_attrib(F,None,F(E_._.type))
            StackSem.append(F_)
        case SemanticRules.F_MINUS_F_RULE:
            F1_ = StackSem.pop()
            t = F1_._.type
            if not type_check(t,int_):
                RaiseError(lexical, ERR_INVALID_TYPE)
            F0_ = t_attrib(F,None,F(t))
            StackSem.append(F0_)
            print("\tNEG"+"\n")
        case SemanticRules.F_NOT_F_RULE:
            F1_ = StackSem.pop()
            t = F1_._.type
            if not type_check(t,bool_):
                RaiseError(lexical, ERR_INVALID_TYPE)
            F0_ = t_attrib(F,None,F(t))
            StackSem.append(F0_)
            print("\tNOT"+"\n")
        case SemanticRules.F_TRUE_RULE:
            TRU_ = StackSem.pop()
            F_ = t_attrib(F,None,F(bool_))
            StackSem.append(F_)
            print("\tLOAD_TRUE"+"\n")
        case SemanticRules.F_FALSE_RULE:
            FALS_ = StackSem.pop()
            F_ = t_attrib(F,None,F(bool_))
            StackSem.append(F_)
            print("\tLOAD_FALSE"+"\n")
        case SemanticRules.F_CHR_RULE:
            CHR_ = StackSem.pop()
            F_ = t_attrib(F,None,F(char_))
            StackSem.append(F_)
            n = lexical.secondary_Token
            print("\tLOAD_CONST "+"\n")
        case SemanticRules.F_STR_RULE:
            STR_ = StackSem.pop()
            F_ = t_attrib(F,None,F(string_))
            StackSem.append(F_)
            n = lexical.secondary_Token
            print("\tLOAD_CONST "+"\n")
        case SemanticRules.F_NUM_RULE:
            NUM_ = StackSem.pop()
            F_ = t_attrib(F,None,F(int_))
            StackSem.append(F_)
            n = lexical.secondary_Token
            print("\tLOAD_CONST "+"\n")
        case SemanticRules.LV_DOT_RULE:
            ID_ = StackSem.pop()
            LV1_ = StackSem.pop()
            t = LV1_._.type
            if t.eKind != STRUCT_TYPE_:
                if t.eKind != UNIVERSAL_:
                    RaiseError(lexical, ERR_KIND_NOT_STRUCT)
                LV0_ = t_attrib(LV,None,LV(universal_))
            else:
                p = t._.pFields
                while p != None:
                    if p.aName == ID_._.name:
                        break
                    p = p.pNext
                if p == None:
                    RaiseError(lexical, ERR_FIELD_NOT_DECL)
                    LV0_ = t_attrib(LV,None,LV(universal_))
                else:
                    LV0_ = t_attrib(LV,None,LV(p._.pType))
            StackSem.append(LV0_)
            print("\tADD "+"\n")
        case SemanticRules.LV_SQUARE_RULE:
            E_ = StackSem.pop()
            LV1_ = StackSem.pop()
            t = LV1_._.type
            if type_check(t,string_):
                LV0_ = t_attrib(LV,None,LV(char_))
            elif t.eKind!=ARRAY_TYPE_:
                if t.eKind != UNIVERSAL_:
                    RaiseError(lexical, ERR_KIND_NOT_ARRAY)
                LV0_ = t_attrib(LV,None,LV(universal_))
            else:
                LV0_ = t_attrib(LV,None,LV(t._.tipoElemento))
                print("\tMUL "+str(n)+"\n")
                print("\tADD"+"\n")
            if not type_check(E_._.type,int_):
                RaiseError(lexical, ERR_INVALID_INDEX_TYPE)
            StackSem.append(LV0_)
        case SemanticRules.LV_IDU_RULE:
            IDU_ = StackSem.pop()
            p = IDU_._.object
            if p.eKind != VAR_ and p.eKind!=PARAM_:
                if p.eKind != UNIVERSAL_:
                    RaiseError(lexical, ERR_KIND_NOT_VAR)
                LV_ = t_attrib(LV,None,LV(universal_))
            else:
                LV_ = t_attrib(LV,None,LV(p._.type))
                print("\tLOAD_REF "+"\n")
            StackSem.append(LV_)
        case SemanticRules.MC_RULE:
            IDU_ = StackSem[-1]
            f = IDU_._.object
            if f.eKind != FUNCTION_:
                MC_ = t_attrib(MC,None,MC(universal_,None,True))
            else:
                MC_ = t_attrib(MC,None,MC(f._.pRetType,f._.pParams,False))
            StackSem.append(MC_)
        case SemanticRules.LE_E_RULE:
            E_ = StackSem.pop()
            MC_ = StackSem[-1]
            LE_ = t_attrib(LE,None,LE(None,None,MC_._.err,1))
            if not MC_._.err:
                p=MC_._.param 
                if p == None:
                    RaiseError(lexical, ERR_TOO_MANY_ARG)
                    LE_._.err = True
                else:
                    if not type_check(p._.tipo,E_._.type):
                        RaiseError(lexical, ERR_PARAM_TYPE)
                    LE_._.param = p.pNext
                    LE_._.n = n + 1
            StackSem.append(LE_)
        case SemanticRules.LE_LE_RULE:
            E_ = StackSem.pop()
            LE1_ = StackSem.pop()
            LE0_ = t_attrib(LE,None,LE(None,None,L1_._.err,LE1_._.n))
            if not LE1_._.err:
                p = LE1_._.param
                if p == None:
                    RaiseError(lexical, ERR_TOO_MANY_ARG)
                    LE0_._.err = True
                else:
                    if not type_check(p._.tipo,E_._.type):
                        RaiseError(lexical, ERR_PARAM_TYPE)
                    LE0_._.param = p.pNext
                    LE0_._.n = n+1
            StackSem.append(LE0_)
        case SemanticRules.F_IDU_MC_RULE:
            LE_ = StackSem.pop()
            MC_ = StackSem.pop()
            IDU_ = StackSem.pop()
            f = IDU_._.object
            F_ = t_attrib(F,None,F(MC_._.type))
            if not LE_._.err:
                if LE_._.n-1 < f._nParams and LE_._.n != 0:
                    RaiseError(lexical, ERR_TOO_FEW_ARGS)
                elif LE_._.n-1 > f._.nParams:
                    RaiseError(lexical, ERR_TOO_MANY_ARG)
            StackSem.append(F_)
            print("\tCALL "+"\n"
        case SemanticRules.MT_RULE:
            MT_ = t_attrib(MT,None,MT(label))
            StackSem.append(MT_)
            print("\tTJMP_FW L"+str()+"\n")
            label = label + 1
        case SemanticRules.ME_RULE:
            MT_ = StackSem[-1]
            ME_._.label = label
            ME_.t_nont = ME
            StackSem.append(ME_)
            print("\tTJMP_FW L"+str(label)+"\n")
            print("L"+str(MT_._.label)+"\n")
            label = label +1
        case SemanticRules.MW_RULE:
            print(MW_)
            MW_ = StackSem.pop() ##
            print(MW_._)
            MW_._.label = label
            StackSem.append(MW_)
            print("L"+str(label)+"\n")
            label = label +1
        case SemanticRules.M_BREAK_RULE:
            MT_ = StackSem[-1]
        case SemanticRules.M_CONTINUE_RULE:
            pass
        case SemanticRules.M_E_SEMICOLON:
            E_ = StackSem.pop()
            LV_ = StackSem.pop()
            if not type_check(LV_._.type,E_._.type):
                RaiseError(lexical, ERR_TYPE_MISMATCH)
            t = LV_._.type
            E0_._ = F(E_._.type)
            StackSem.append(E0_)
            if t._ == None:
                print("\tSTORE_REF 1\n")
            else:
                print("\tSTORE_REF "+"\n")

         
