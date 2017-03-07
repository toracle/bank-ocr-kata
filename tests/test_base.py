# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from bankocr.ocr import Ocr


'''
    _  _     _  _  _  _  _ \n
  | _| _||_||_ |_   ||_||_|\n
  ||_  _|  | _||_|  ||_| _|\n
                           \n
'''

def fixture_panel():
    return '    _  _     _  _  _  _  _ \n' \
           '  | _| _||_||_ |_   ||_||_|\n' \
           '  ||_  _|  | _||_|  ||_| _|\n' \
           '                           \n'

def fixture_one():
    return '   \n  |\n  |\n   \n'

def fixture_two():
    return ' _ \n _|\n|_ \n   \n'

def fixture_three():
    return ' _ \n _|\n _|\n   \n'

def fixture_four():
    return '   \n|_|\n  |\n   \n'

def fixture_five():
    return ' _ \n|_ \n _|\n   \n'

def fixture_six():
    return ' _ \n|_ \n|_|\n   \n'

def fixture_seven():
    return ' _ \n  |\n  |\n   \n'

def fixture_eight():
    return ' _ \n|_|\n|_|\n   \n'

def fixture_nine():
    return ' _ \n|_|\n _|\n   \n'

def test_parse_one():
    ocr = Ocr()
    assert ocr.parse_digit(fixture_one()) == 1

def test_parse_two():
    ocr = Ocr()
    assert ocr.parse_digit(fixture_two()) == 2

def test_parse_three():
    ocr = Ocr()
    assert ocr.parse_digit(fixture_three()) == 3

def test_parse_four():
    ocr = Ocr()
    assert ocr.parse_digit(fixture_four()) == 4

def test_parse_five():
    ocr = Ocr()
    assert ocr.parse_digit(fixture_five()) == 5

def test_parse_six():
    ocr = Ocr()
    assert ocr.parse_digit(fixture_six()) == 6

def test_parse_seven():
    ocr = Ocr()
    assert ocr.parse_digit(fixture_seven()) == 7

def test_parse_eight():
    ocr = Ocr()
    assert ocr.parse_digit(fixture_eight()) == 8

def test_parse_nine():
    ocr = Ocr()
    assert ocr.parse_digit(fixture_nine()) == 9

def test_divide_digits():
    ocr = Ocr()
    assert ocr.divide_digit(fixture_panel()) == [
        '   \n  |\n  |\n   \n',
        ' _ \n _|\n|_ \n   \n',
        ' _ \n _|\n _|\n   \n',
        '   \n|_|\n  |\n   \n',
        ' _ \n|_ \n _|\n   \n',
        ' _ \n|_ \n|_|\n   \n',
        ' _ \n  |\n  |\n   \n',
        ' _ \n|_|\n|_|\n   \n',
        ' _ \n|_|\n _|\n   \n'
    ]

def test_parse_panel():
    ocr = Ocr()
    assert ocr.parse_panel(fixture_panel()) == 123456789
