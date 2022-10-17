from Syntatical.states import *

action_table = init_table()


class SyntaticalAnalyser:
    parser = None
    syntatical_error = False

    def __init__(self, parser):
        self.parser = parser

    def IS_SHIFT(self, p):
        return p > 0

    def IS_REDUCTION(self, p):
        return p < 0

    def get_next_token(self):
        token = self.parser.next_token()
        a = token_tab(token)
        return a

    def RULE(self, p):
        return (-1) * p

    def syntax_check(self):

        state_stack = []
        q = 0
        state_stack.append(q)
        a = self.get_next_token()
        final = "acc"

        while action_table[q + 1][a] != final:

            p = int(action_table[q + 1][a])

            if self.IS_SHIFT(p):
                state_stack.append(p)
                a = self.get_next_token()

            elif self.IS_REDUCTION(p):
                r = self.RULE(p)
                for x in range(LEN[r - 1]):
                    state_stack.pop()
                if state_stack:
                    state_stack.append(
                        int(action_table[state_stack[-1] + 1][token_tab(
                            LEFT[r - 1])]))
                else:
                    self.syntatical_error = True
                    print("Syntax Error")
                    break
                SemanticAnalysis(self.parser, r)

            else:
                self.syntatical_error = True
                print("Syntax Error")
                break
            q = state_stack[-1]

        if (self.syntatical_error == False):
            print("No Syntax Error")
