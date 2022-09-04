from common import *


class LexicalAnalyser:
    identifiers = []
    v_consts = []
    arq = None
    lexical_error = False

    def __init__(self, file):
        file.seek(0)
        self.arq = file
        self.next_char = self.arq.read(1)

    def search_name(self, name):
        if name not in self.identifiers:
            self.identifiers.append(name)
        return self.identifiers.index(name)

    def search_key_word(self, name):
        left = 0
        right = len(reserved_words) - 1
        while left <= right:
            middle = (left + right) // 2
            if reserved_words[middle] == name:
                return KeyWords(middle)
            elif reserved_words[middle] > name:
                right = middle - 1
            else:
                left = middle + 1
        return KeyWords.ID

    def add_const(self, c):
        if c not in self.v_consts:
            self.v_consts.append(c)
        return self.v_consts.index(c)

    def next_token(self):
        sep = ""
        text = ""
        secondary_token = None

        while self.next_char.isspace():
            self.next_char = self.arq.read(1)

        if self.next_char == "":
            token = KeyWords.EOF

        elif self.next_char.isalpha():
            text_aux = []
            while self.next_char.isalpha() or self.next_char == '_' or self.next_char.isnumeric():
                text_aux.append(self.next_char)
                self.next_char = self.arq.read(1)
            text = sep.join(text_aux)
            token = self.search_key_word(text)
            if token == KeyWords.ID:
                secondary_token = self.search_name(text)

        elif self.next_char.isnumeric():
            num_aux = []
            i = 0
            while self.next_char.isnumeric():
                num_aux.append(self.next_char)
                self.next_char = self.arq.read(1)
                if self.next_char == '.' and i == 0:
                    i = i+1
                    num_aux.append(self.next_char)
                    self.next_char = self.arq.read(1)
            text = sep.join(num_aux)
            token = KeyWords.NUMERAL
            secondary_token = self.add_const(text)

        elif self.next_char == "\"":
            string_aux = []
            self.next_char = self.arq.read(1)
            while (self.next_char != "\""):
                string_aux.append(self.next_char)
                self.next_char = self.arq.read(1)
            self.next_char = self.arq.read(1)
            text = sep.join(string_aux)
            token = KeyWords.STRINGVAL
            secondary_token = self.add_const(text)

        else:
            if self.next_char == "\'":
                self.next_char = self.arq.read(1)
                text = self.next_char
                token = KeyWords.CHARACTER
                secondary_token = self.add_const(text)
                self.next_char = self.arq.read(2)
            elif self.next_char == ":":
                text = self.next_char
                self.next_char = self.arq.read(1)
                token = KeyWords.COLON
            elif self.next_char == "+":
                text = self.next_char
                self.next_char = self.arq.read(1)
                if self.next_char == "+":
                    text = "++"
                    token = KeyWords.PLUS_PLUS
                    self.next_char = self.arq.read(1)
                else:
                    token = KeyWords.PLUS
            elif self.next_char == "-":
                text = self.next_char
                self.next_char = self.arq.read(1)
                if self.next_char == "-":
                    text = "--"
                    token = KeyWords.MINUS_MINUS
                    self.next_char = self.arq.read(1)
                else:
                    token = KeyWords.MINUS
            elif self.next_char == ";":
                text = self.next_char
                self.next_char = self.arq.read(1)
                token = KeyWords.SEMI_COLON
            elif self.next_char == ",":
                text = self.next_char
                self.next_char = self.arq.read(1)
                token = KeyWords.COMMA
            elif self.next_char == "=":
                text = self.next_char
                self.next_char = self.arq.read(1)
                if self.next_char == "=":
                    text = "=="
                    token = KeyWords.EQUAL_EQUAL
                    self.next_char = self.arq.read(1)
                else:
                    token = KeyWords.EQUALS
            elif self.next_char == "[":
                text = self.next_char
                self.next_char = self.arq.read(1)
                token = KeyWords.LEFT_SQUARE
            elif self.next_char == "]":
                text = self.next_char
                self.next_char = self.arq.read(1)
                token = KeyWords.RIGHT_SQUARE
            elif self.next_char == "{":
                text = self.next_char
                self.next_char = self.arq.read(1)
                token = KeyWords.LEFT_BRACES
            elif self.next_char == "}":
                text = self.next_char
                self.next_char = self.arq.read(1)
                token = KeyWords.RIGHT_BRACES
            elif self.next_char == "(":
                text = self.next_char
                self.next_char = self.arq.read(1)
                token = KeyWords.LEFT_PARENTHESIS
            elif self.next_char == ")":
                text = self.next_char
                self.next_char = self.arq.read(1)
                token = KeyWords.RIGHT_PARENTHESIS
            elif self.next_char == "&":
                text = self.next_char
                self.next_char = self.arq.read(1)
                if self.next_char == "&":
                    text = "&&"
                    self.next_char = self.arq.read(1)
                    token = KeyWords.AND
                else:
                    token = KeyWords.UNKNOWN
            elif self.next_char == "|":
                text = self.next_char
                self.next_char = self.arq.read(1)
                if self.next_char == "|":
                    self.next_char = self.arq.read(1)
                    token = KeyWords.OR
                else:
                    token = KeyWords.UNKNOWN
            elif self.next_char == "<":
                text = self.next_char
                self.next_char = self.arq.read(1)
                if self.next_char == "=":
                    text = "<="
                    token = KeyWords.LESS_OR_EQUAL
                    self.next_char = self.arq.read(1)
                else:
                    token = KeyWords.LESS_THAN
            elif self.next_char == ">":
                text = self.next_char
                self.next_char = self.arq.read(1)
                if self.next_char == "=":
                    text = ">="
                    token = KeyWords.GREATER_OR_EQUAL
                    self.next_char = self.arq.read(1)
                else:
                    token = KeyWords.GREATER_THAN
            elif self.next_char == "!":
                text = self.next_char
                self.next_char = self.arq.read(1)
                if self.next_char == "=":
                    text = "!="
                    token = KeyWords.NOT_EQUAL
                    self.next_char = self.arq.read(1)
                else:
                    token = KeyWords.NOT
            elif self.next_char == "*":
                text = self.next_char
                self.next_char = self.arq.read(1)
                token = KeyWords.TIMES
            elif self.next_char == ".":
                text = self.next_char
                self.next_char = self.arq.read(1)
                token = KeyWords.DOT
            elif self.next_char == "/":
                text = self.next_char
                self.next_char = self.arq.read(1)
                token = KeyWords.DIVIDE
            else:
                self.next_char = self.arq.read(1)
                token = KeyWords.UNKNOWN

        if token == KeyWords.UNKNOWN:
            self.lexical_error = True
            print("<\"" + text + "\", " + token.name +
                  "> - Here is a lexical error\n")
        elif token != KeyWords.EOF and secondary_token != None:
            print("<\"" + text + "\", " + token.name +
                  ", Secondary Token: " + str(secondary_token) + ">\n")
        elif token != KeyWords.EOF:
            print("<\"" + text + "\", " + token.name + ">\n")
        return token

    def check(self):
        token_aux = self.next_token()
        while token_aux != KeyWords.EOF:
            token_aux = self.next_token()
        if self.lexical_error:
            print("There are lexical errors.")
        else:
            print("No lexical errors.")
