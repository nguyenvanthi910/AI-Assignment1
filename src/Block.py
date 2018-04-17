#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def nextTo(self, other):
        return self.isLeft(other) or self.isRight(other) or self.isUp(other) or self.isDown(other)

    def isLeft(self, other): return self.col + 1 == other.col and self.row == other.row
    def isRight(self, other): return self.col - 1 == other.col and self.row == other.row
    def isUp(self, other): return self.row + 1 == other.row and self.col == other.col
    def isDown(self, other): return self.row - 1 == other.row and self.col == other.col

    def moveup(self, step = 1): self.row -= step
    def movedown(self, step = 1): self.row += step
    def moveleft(self, step = 1): self.col -= step
    def moveright(self, step = 1): self.col += step

    def __eq__(self, other): return other != None and self.isUp(other)
    def __ne__(self, other): return other == None or not self.isUp(other)
    def __repr__(self): return "(%d,%d)" % (self.row, self.col)

class Block:
    def __init__(self, node1, node2, control = None):
        self.A = node1
        self.B = node2
        self.control = control
        if self.A.nextTo(self.B) or self.A.isUp(self.B):
            self.control = None

    def ___split__(self, xA, yA, xB, yB, control):
        self.A.x = xA
        self.A.y = yA
        self.B.x = xB
        self.B.y = yB
        self.control = control
    
    def split(self, pointA, pointB, control = 0):
        '''Point A, Point B là vị trí sau khi spit với định dạng là array [row, col]'''
        xA, yA = pointA
        xB, yB = pointB
        if control == 0 or control == False or control == self.A:
            self.___split__(xA, yA, xB, yB, self.A)
        else: self.___split__(xA,yA,xB,yB, self.B)

    def setControl(self, row, col):
        if Node(row, col) == self.A: return self.A
        else: return self.B

    def toggleControl(self):
        if self.A.nextTo(self.B) or self.A.top(self.B):
            self.control = None
        elif self.control == self.A:
            self.control = self.B
        else: self.control = self.A

    def moveup(self):
        if self.control == None:
            if self.A.isLeft(self.B) or self.A.isRight(self.B):
                self.A.moveup()
                self.B.moveup()
            else: #2 khối nằm dọc
                if self.A.isUp(self.B): #A nằm phía trên B
                    self.A.moveup()
                    self.B.moveup(2)
                elif self.A.isDown(self.B):
                    self.A.moveup(2)
                    self.B.moveup()
                else:#Hai khối chông nhau
                    self.A.moveup(2)
                    self.B.moveup()
        else:
            if self.control == self.A: #Điều khiển cho A
                self.A.moveup()
            else: #Điều khiển cho B
                self.B.moveup()
            if self.A.nextTo(self.B) or self.A.isUp(self.B):
                self.control = None

    def movedown(self):
        if self.control == None:
            if self.A.isLeft(self.B) or self.A.isRight(self.B):#2 khối nằm ngang
                self.A.movedown()
                self.B.movedown()
            else: #2 khối nằm dọc
                if self.A.isUp(self.B): #A nằm phía trên B
                    self.A.movedown(2)
                    self.B.movedown()
                elif self.A.isDown(self.B):
                    self.A.movedown(1)
                    self.B.movedown(2)
                else:#2 khối chồng nhau
                    self.A.movedown(2)
                    self.B.movedown()
        else:
            if self.control == self.A: #Điều khiển cho A
                self.A.movedown()
            else: #Điều khiển cho B
                self.B.movedown()
            if self.A.nextTo(self.B) or self.A.isUp(self.B):
                self.control = None

    def moveleft(self):
        if self.control == None:
            if self.A.isUp(self.B) or self.A.isDown(self.B): #2 khối nằm dọc
                self.A.moveleft()
                self.B.moveleft()
            else: #2 khối nằm ngang
                if self.A.isLeft(self.B):
                    self.A.moveleft()
                    self.B.moveleft(2)
                elif self.A.isRight(self.B):
                    self.A.moveleft(2)
                    self.B.moveleft()
                else: #2 khối chồng nhau
                    self.A.moveleft(2)
                    self.B.moveleft()
        else:
            if self.control == self.A:
                self.A.moveleft()
            else:
                self.B.moveleft()
            if self.A.nextTo(self.B) or self.A.isUp(self.B):
                self.control = None

    def moveright(self):
        if self.control == None:
            if self.A.isUp(self.B) or self.A.isDown(self.B): #2 khối nằm dọc
                self.A.moveright()
                self.B.moveright()
            else: #2 khối nằm ngang
                if self.A.isLeft(self.B):
                    self.A.moveright(2)
                    self.B.moveright()
                elif self.A.isRight(self.B):

                    self.A.moveright()
                    self.B.moveright(2)
                else: #2 khối chồng nhau
                    self.A.moveright(2)
                    self.B.moveright()
        else:
            if self.control == self.A:
                self.A.moveright()
            else:
                self.B.moveright()
            if self.A.nextTo(self.B) or self.A.isUp(self.B):
                self.control = None

    def isStand(self):
        if self.A.top(self.B):
            return 2
        else: return 1

    def __eq__(self, other):
        return other != None and self.A == other.A and self.B == other.B

    def __repr__(self):
        return "[%s(%s %s)]" % (self.control, self.A, self.B)
