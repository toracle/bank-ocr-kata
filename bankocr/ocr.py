# -*- coding: utf-8 -*-

class Ocr(object):
    def __init__(self):
        self.data = {
            '   \n  |\n  |\n   \n': 1,
            ' _ \n _|\n|_ \n   \n': 2,
            ' _ \n _|\n _|\n   \n': 3,
            '   \n|_|\n  |\n   \n': 4,
            ' _ \n|_ \n _|\n   \n': 5,
            ' _ \n|_ \n|_|\n   \n': 6,
            ' _ \n  |\n  |\n   \n': 7,
            ' _ \n|_|\n|_|\n   \n': 8,
            ' _ \n|_|\n _|\n   \n': 9
        }

    def parseDigit(self, s):
        return self.data[s]

    # def parsePanel(self, s):
    #     pass
