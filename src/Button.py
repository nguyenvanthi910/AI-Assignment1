#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from Map import Tiles
except ImportError:
    from src.Map import Tiles

class Button(Tiles):
    def __init__(self, weak, row, col, isEnable): raise NotImplementedError
    def enable(self, other): raise NotImplementedError
    def canStand(self):
        return self.weak is not None  and self.isBlur == False
    def canLie(self):
        return self.weak is not None and self.isBlur == False
    def setBlur(self):
            self.isBlur = True
    def resetBlur(self):
        self.isBlur = False

class Toggle(Button):
    def __init__(self, weak, row, col, lsRC, isEnable=False):
        self.row = row
        self.col = col
        self.weak = weak
        self.isEnable = isEnable
        self.lsShow = []
        self.lsHide = []
        self.isBlur = False
        self.goal = False
        for i, j  in lsRC:
            self.lsShow.append([i,j,False])
            self.lsHide.append([i, j, None])
    def enable(self, map):
        if self.isEnable:
            map.change(self.lsHide)
            self.isEnable = False
        else: 
            map.change(self.lsShow)
            self.isEnable = True
    def canStand(self):
        return self.weak is not None  and self.isBlur == False
    def canLie(self):
        return self.weak is not None and self.isBlur == False
    def setBlur(self):
        self.isBlur = True
    def resetBlur(self):
        self.isBlur = False
    def isGoal(self, isStand):
        if (self.weak == False and isStand == False):
            return False
        else: return self.goal

class Show(Button):
    def __init__(self, row, col, weak, lsRC, isEnable = False):
        self.row = row
        self.col = col
        self.weak = weak
        self.isEnable = isEnable
        self.lsShow = []
        self.lsHide = []
        self.isBlur = False
        self.goal = False
        for i, j  in lsRC:
            self.lsShow.append([i,j,False])
    def enable(self, map):
        if not self.isEnable:
            map.change(self.lsShow)
            self.isEnable = True
    def canStand(self):
        return self.weak is not None  and self.isBlur == False
    def canLie(self):
        return self.weak is not None and self.isBlur == False
    def setBlur(self):
        self.isBlur = True
    def resetBlur(self):
        self.isBlur = False
    def isGoal(self, isStand):
        if (self.weak == False and isStand == False):
            return False
        else: return self.goal

class Hide(Button):
    def __init__(self, row, col, weak, lsRC, isEnable = False):
        self.row = row
        self.col = col
        self.weak = weak
        self.isEnable = isEnable
        self.lsShow = []
        self.lsHide = []
        self.isBlur = False
        self.goal = False
        for i, j  in lsRC:
            self.lsHide.append([i,j,None])
    def enable(self, map):
        if not self.isEnable:
            map.change(self.lsHide)
            self.isEnable = True
    def canStand(self):
        return self.weak is not None  and self.isBlur == False
    def canLie(self):
        return self.weak is not None and self.isBlur == False
    def setBlur(self):
        self.isBlur = True
    def resetBlur(self):
        self.isBlur = False
    def isGoal(self, isStand):
        if (self.weak == False and isStand == False):
            return False
        else: return self.goal

class HideAndShow(Button):
    def __int__(self, row, col, weak, lsRCS, lsRCH, isEnable = False):
        self.show = Show(row, col, weak, lsRCS, isEnable)
        self.hide = Show(row, col, weak, lsRCH, isEnable)
        self.isBlur = True
        self.goal = False
    def enable(self, map):
        self.show.show(map)
        self.hide.hide(map)
    def canStand(self):
        return self.weak is not None  and self.isBlur == False
    def canLie(self):
        return self.weak is not None and self.isBlur == False
    def setBlur(self):
        self.isBlur = True
    def resetBlur(self):
        self.isBlur = False
    def isGoal(self, isStand):
        if (self.weak == False and isStand == False):
            return False
        else: return self.goal

class Split(Button):
    def __init__(self, row, col, weak, lsRC, isEnable = False):
        self.row = row
        self.col = col
        self.weak = weak
        self.isEnable = isEnable
        self.lsRC = lsRC
        self.isBlur = False
        self.goal = False
    def enable(self, block, control = 0):
        """Control == 0 is for A and 1 is for B"""
        a, b = self.lsRC
        block.split(a, b, control)
        if not self.isEnable:
            self.isEnable = True
    def canStand(self):
        return self.weak is not None  and self.isBlur == False
    def canLie(self):
        return self.weak is not None and self.isBlur == False
    def setBlur(self):
        self.isBlur = True
    def resetBlur(self):
        self.isBlur = False
    def isGoal(self, isStand):
        if (self.weak == False and isStand == False):
            return False
        else: return self.goal