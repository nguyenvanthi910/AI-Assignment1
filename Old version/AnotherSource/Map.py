#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Tiles:
    def __init__(self, isWeak = None):
        if isWeak is 1:
            self.weak = True
        elif isWeak is 2:
            self.weak = False
        elif isWeak is 0:
            self.weak = None
        else:
            self.weak = isWeak
    def canStand(self):
        return self.weak is not None and self.weak == False
    def canLie(self):
        return self.weak is not None
    def __repr__(self): return "%s" % str(self.weak)

class StartTiles(Tiles):
    def __init__(self, isWeak = False):
        self.weak = isWeak
    def canStand(self):
        return self.weak is not None and self.weak == False
    def canLie(self):
        return self.weak is not None

class GoalTiles(Tiles):
    def __init__(self, isWeak = False):
        self.weak = isWeak
    def canStand(self):
        return self.weak is not None and self.weak == False
    def canLie(self):
        return self.weak is not None

class TempGoal(Tiles):
    def __init__(self,row, col, isWeak = False):
        self.weak = isWeak
        self.row = row
        self.col = col
    def canStand(self):
        return self.weak is not None and self.weak == False
    def canLie(self):
        return self.weak is not None

class Map:
    def __init__(self, matrix, rowSize, colSize):
        self.matrix = matrix
        self.row = rowSize
        self.col = colSize
        self.tempGoal = None
        self.tiles = 0
        for i in self.matrix:
            for j in i:
                if j.weak != None: self.tiles += 1
    def isValid(self, row, col, stand = False):
        if row < 0 or col < 0 or row > self.row or col > self.col:
            return False
        else:
            if stand == True: return self.matrix[row][col].canStand()
            else: return self.matrix[row][col].canLie()
    def isGoal(selfs, row, col):
        try:
            if selfs.tempGoal != None:
                if selfs.tempGoal.row == row and selfs.tempGoal.col == col:
                    return True
                else: return False
            if isinstance(selfs.matrix[row][col], GoalTiles):
                return True
            return False
        except IndexError: return False
    def changeTiles(self, lsTiles):
        """Cấu trúc [(0,0,True), (0,1,False), (1,2,None)]"""
        for i, j, value in lsTiles:
            try:
                if self.matrix[int(i)][int(j)].weak != value:
                    self.matrix[int(i)][int(j)].weak = value
                    if value == None:
                        self.tiles -= 1
                    else: self.tiles += 1
            except IndexError:
                print("Error in changeTiles " + str(lsTiles))
    def distance(self):
        return abs(1)
    def __repr__(self): return "\n".join(str(i) for i in self.matrix)
