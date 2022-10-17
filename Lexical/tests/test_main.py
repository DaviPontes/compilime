import sys

# setting path
sys.path.append('..')

from core import LexicalAnalyser


def test_file_one():
    file = open('test-file-1.txt', 'r', encoding='utf-8')
    lexical = LexicalAnalyser(file)
    assert lexical.check() == True
    file.close()


def test_file_two():
    file = open('test-file-2.txt', 'r', encoding='utf-8')
    lexical = LexicalAnalyser(file)
    assert lexical.check() == True
    file.close()


def test_file_three():
    file = open('test-file-3.txt', 'r', encoding='utf-8')
    lexical = LexicalAnalyser(file)
    assert lexical.check() == False
    file.close()
