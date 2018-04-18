#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Tiles:
    '''
    weak: nếu ô đó chỉ cho phép block nằm ngang thì True, nếu cho phép
        nằm dọc là False và nếu không cho phéo block đi qua thì None
    before: để lưu giá trị trước đó để thực hiện chức năng show/hide/toggle
    isBlur: để lưu giá trị của giải thuật xác định miền của map, nếu đã bị blur
    thì block không thể qua được.'''
    def __init__(self, isWeak = None, beforevalue = True):
        if isWeak is 1:
            self.weak = True
        elif isWeak is 2:
            self.weak = False
        elif isWeak is 0:
            self.weak = None
        else:
            self.weak = isWeak
        if beforevalue is 1:
            self.before = False
        elif beforevalue is 2:
            self.before = True
        else: beforevalue = beforevalue
        self.isBlur = False
    def canStand(self):
        return self.weak is not None and self.weak == False and self.isBlur == False
    def canLie(self):
        return self.weak is not None and self.isBlur == False
    def show(self):
        self.weak = None
    def hide(self):
        self.weak = self.before
    def isShow(self):
        return self.before == self.weak
    def toggle(self):
        if self.isShow():
            self.hide()
        else: self.show()
    def setBlur(self):
        self.isBlur = True
    def resetBlur(self):
        self.isBlur = False
    def __repr__(self): return "%s" % str(self.weak)

class Goal(Tiles):
    '''
    weak: nếu ô đó chỉ cho phép block nằm ngang thì True, nếu cho phép
        nằm dọc là False và nếu không cho phéo block đi qua thì None
    before: để lưu giá trị trước đó để thực hiện chức năng show/hide/toggle
    isBlur: để lưu giá trị của giải thuật xác định miền của map, nếu đã bị blur
    thì block không thể qua được.'''
    def __init__(self, isWeak = False, beforevalue = True):
        if isWeak is 1:
            self.weak = True
        elif isWeak is 2:
            self.weak = False
        elif isWeak is 0:
            self.weak = None
        else:
            self.weak = isWeak
        if beforevalue is 1:
            self.before = False
        elif beforevalue is 2:
            self.before = True
        else: beforevalue = beforevalue
        self.isBlur = False
    def canStand(self):
        return self.weak is not None and self.weak == False and self.isBlur == False
    def canLie(self):
        return self.weak is not None and self.isBlur == False
    def show(self):
        self.weak = None
    def hide(self):
        self.weak = self.before
    def isShow(self):
        return self.before == self.weak
    def toggle(self):
        if self.isShow():
            self.hide()
        else: self.show()
    def setBlur(self):
        self.isBlur = True
    def resetBlur(self):
        self.isBlur = False
    def isGoal(self, isStand):
        return isStand
    def __repr__(self): return "%s" % str(self.weak)

class Map:
    '''
    matrix: Ma trận tiles và button
    row, col: kích thước hàng và cột
    tiles: đếm số tiles có trong ma trận
    '''
    def __init__(self, matrix, rowSize, colSize):
        self.matrix = matrix
        self.row = rowSize
        self.col = colSize
        self.tiles = 0
        for i in self.matrix:
            for j in i:
                if j.weak != None: self.tiles += 1
    def isValid(self, row, col, stand = False):
        '''Kiển tra xem block nằm ở vị trí (row, col) có valid hay không.
        valid trong trường hợp vị trí thuộc ma trận và trạng thái (is stand)
        của block có phù hợp với tiles hiện tại không.'''
        if row < 0 or col < 0 or row > self.row or col > self.col:
            return False
        else:
            if stand == True: return self.matrix[row][col].canStand()
            else: return self.matrix[row][col].canLie()

    def isGoal(self, row, col, isStand = False):
        '''Kiểm tra xem có phải đích hay không '''
        try:
            return {self.matrix[row][col].isGoal(isStand), self.matrix[row][col]}
        except IndexError: return {False, None}

    def change(self, lsTiles):
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

    def setBlur(self, row, col):
        if row < 0 or col < 0 or row > self.row or col > self.col:
            self.matrix[row][col].setBlur()

    def resetBlur(self, row, col):
        if row < 0 or col < 0 or row > self.row or col > self.col:
            self.matrix[row][col].resetBlur()

    def __repr__(self): return "\n".join(str(i) for i in self.matrix)