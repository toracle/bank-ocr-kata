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

    def parse_digit(self, s):
        return self.data[s]

    # def parse_panel(self, s):
    #     pass

    def divide_digit(self, s):
        lines = s.split('\n')
        panel = {}
        for y, line in enumerate(lines):
            for x, i in enumerate(range(0, 27, 3)):
                col = line[i:i+3]
                panel[(y, x)] = col

        result = []
        for x in range(9):
            result.append('\n'.join([panel[(y, x)] for y in range(4)])+'\n')

        return result
