#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Button:
    def __init__(self, row, col, weak, isEnable): raise NotImplementedError
    def enable(self): raise NotImplementedError

class Toggle(Button):
    def __init__(self, row, col, weak, lsRC, isEnable = False):
        self.row = row
        self.col = col
        self.weak = weak
        self.isEnable = isEnable
        self.lsShow = []
        self.lsHide = []
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

class Show(Button):
    def __init__(self, row, col, weak, lsRC, isEnable = False):
        self.row = row
        self.col = col
        self.weak = weak
        self.isEnable = isEnable
        self.lsShow = []
        self.lsHide = []
        for i, j  in lsRC:
            self.lsShow.append([i,j,False])
    def enable(self, map):
        if not self.isEnable:
            map.change(self.lsShow)
            self.isEnable = True

class Hide(Button):
    def __init__(self, row, col, weak, lsRC, isEnable = False):
        self.row = row
        self.col = col
        self.weak = weak
        self.isEnable = isEnable
        self.lsShow = []
        self.lsHide = []
        for i, j  in lsRC:
            self.lsHide.append([i,j,None])
    def enable(self, map):
        if not self.isEnable:
            map.change(self.lsHide)
            self.isEnable = True

class Split(Button):
    def __init__(self, row, col, weak, lsRC, isEnable = False):
        self.row = row
        self.col = col
        self.weak = weak
        self.isEnable = isEnable
        self.lsRC = lsRC
    def enable(self, block, control = 0):
        """Control == 0 is for A and 1 is for B"""
        a, b = self.lsRC
        block.split(a, b, control)
        if not self.isEnable:
            self.isEnable = True