# -*- coding: utf-8 -*-

class Ocr(object):
    def parseDigit(self, s):
        if self.isDigitOne(s):
            return 1
        elif self.isDigitTwo(s):
            return 2

    def isDigitOne(self, s):
        if s == '   \n  |\n  |\n   \n':
            return True
        return False

    def isDigitTwo(self, s):
        if s == ' _ \n _|\n|_ \n   \n':
            return True
        return False
