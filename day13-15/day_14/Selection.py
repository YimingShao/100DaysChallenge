import random

class Selection:
    def __init__(self, name):
        self.name = name


class player():
    def __init__(self, name):
        self.name = name
        self.score=0


class Rock(Selection):
    def vs(self, select):
        if select.name == 'Sissor':
            return True

class Sissor(Selection):
    def vs(self, select):
        if select.name == 'Paper':
            return True

class Paper(Selection):
    def vs(self, select):
        if select.name == 'Rock':
            return True
