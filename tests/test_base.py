# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from bankocr.ocr import Ocr


'''
    _  _     _  _  _  _  _
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _| 

'''

def fixture_one():
    return '   \n  |\n  |\n   \n'

def test_parse_one():
    ocr = Ocr()
    assert ocr.parseDigit(fixture_one()) == 1
