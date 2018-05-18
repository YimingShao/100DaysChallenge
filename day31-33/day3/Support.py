import csv

import logbook

csvfile = 'battle-table.csv'


class Roll:
    def __init__(self, name):
        self.name = name

    def vs(self, other, windict):
        if other.name in windict:
            return 1
        if self.name == other.name:
            return 0
        else:
            return -1


class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0

