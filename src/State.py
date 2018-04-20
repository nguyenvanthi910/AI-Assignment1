#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import deepcopy
try:
    from State import *
    import FileHandler as file
except ImportError:
    from src.State import  *
    import src.FileHandler as file
import time
import curses




testcase = "../testcase/"
mapweb = "../maps/web/"
def get_testcase(i): return testcase + str(i)
def get_web_map(i): return mapweb + str(i)



def getLsGoal(ls, map):
    lsGoal = []
    for i, j in ls:
        lsGoal.append(map.getElement(i, j))
    return lsGoal

UP = " --> U "
DOWN = " --> D "
LEFT = " --> L "
RIGHT = " --> R "

class State():
    "Trạng thái của trò chơi"
    def __init__(self, block ,value = 1,map = None, mapChanged = False):
        self.block = block
        self.parent = None
        self.move = None
        self.lsGoal = None
        self.map = map
        self.value = value
        self.mapChanged = mapChanged

    def getMap(self):
        if(self.mapChanged == True):
            return self.map
        else:
            p = self.parent
            while p.mapChanged == False:
                p = p.parent
            return p.map


    def checkMapChange(self):
        m = deepcopy(self.getMap())
        check = m.enableButton(self.block)
        self.mapChanged = check
        if check == True:
            self.map = m

    def isValid(self):
        return self.getMap().isValid(self.block)

    def __cp__(self, g):
        A = self.block.A
        B = self.block.B
        return (g.x == A.x and g.y == A.y) or (g.x == B.x and g.y == B.y)

    def isGoal(self):
        if(self.getMap().isGoal(self.block)): return [True, None]
        if not self.lsGoal: return [True, None]
        g = self.lsGoal[0]
        if g.w <= self.block.weight() and self.__cp__(g):
            self.lsGoal.pop(0)
            return [True, g]
        else: return [False, g]


    def __eq__(self, other):
        return self.block == other.block and self.getMap() == other.getMap()

    def __repr__(self):
        return str(self.move) + "\r" + str(self.getMap().__repr__(self.block)) + "\r"
    def shortSol(self):
        return str(self.move)

def nextState(current):
    children = []
    step = 8
    if current.block.control == None:
        step = 4
    for i in range(step):
        newblock = deepcopy(current.block)
        mv = ""
        if i == 0:
            mv = UP + newblock.getCtrString()
            newblock.moveup()
        elif i == 1:
            mv = DOWN + newblock.getCtrString()
            newblock.movedown()
        elif i == 2:
            mv = LEFT + newblock.getCtrString()
            newblock.moveleft()
        elif i == 3:
            mv = RIGHT + newblock.getCtrString()
            newblock.moveright()
        else:
            newblock.changeControl()
            if i - 4 == 0:
                mv = UP + newblock.getCtrString()
                newblock.moveup()
            elif i - 4 == 1:
                mv = DOWN + newblock.getCtrString()
                newblock.movedown()
            elif i - 4 == 2:
                mv = LEFT + newblock.getCtrString()
                newblock.moveleft()
            elif i - 4 == 3:
                mv = RIGHT + newblock.getCtrString()
                newblock.moveright()
        newstate = State(newblock, current.value + 1)
        newstate.move = mv
        newstate.lsGoal = current.lsGoal
        newstate.parent = current
        newstate.checkMapChange()
        if newstate.isValid():
            children.append(newstate)
    return children

def breadth_first_search(initState):
    counter = 0
    queue = list()
    explored = list()
    queue.append(initState)
    while queue:
        state = queue.pop(0)
        check, value = state.isGoal()
        counter += 1
        if check == True:
            queue.clear()
            explored.clear()
            if value == None:
                print(initState)
                printShortSolution(state)
                print("\n\nMove %d steps\n" % state.value)
                print("Explored %d states\n\n" % counter)
                return state
        explored.append(state)
        children = nextState(state)
        for i in children:
            if i not in explored:
                queue.append(i)

def depth_first_search(initState, maxdepth = 10):
    counter = 0
    stack = list()
    explored = list()
    stack.append(initState)
    while stack:
        state = stack.pop()
        check, value = state.isGoal()
        counter += 1
        if check == True:
            if value == None:
                print(initState)
                printShortSolution(state)
                print("\n\nMove %d steps\n" % state.value)
                print("Explored %d states\n\n" % counter)
                return state
        explored.append(state)
        if state.value > maxdepth:
            continue
        children = nextState(state)
        for i in children:
            if i not in explored:
                stack.append(i)
    print("Don't have any solutions.")
    return initState

def printShortSolution(state):
    root = []
    root.append(state)
    parent = state.parent
    while parent:
        root.append(parent)
        parent = parent.parent

    root = reversed(root)
    result = ''
    for j, k in enumerate(root):
        if j % 5 != 0:
            result += str(k.shortSol())
        else: result += str(k.shortSol()) + "\n"
    print(result)


