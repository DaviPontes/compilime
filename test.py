from Lexical.core import LexicalAnalyser
from Syntatical.sint_comp import SyntaticalAnalyser

file = open('test-file-1.txt', 'r', encoding = 'utf-8')

lexical = LexicalAnalyser(file)
lexical.check()

lexical = LexicalAnalyser(file)
syntatical = SyntaticalAnalyser(lexical)
syntatical.syntax_check()

file.close()