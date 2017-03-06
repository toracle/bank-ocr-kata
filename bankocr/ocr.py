# -*- coding: utf-8 -*-

class Ocr(object):
    def parseDigit(self, s):
        if s == '   \n  |\n  |\n   \n':
            return 1
