#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from Elements import *
    import FileHandler as file
except ImportError:
    from src.Elements import  *
    import src.FileHandler as file
from queue import PriorityQueue
from math import *

testcase = "../testcase/"
mapweb = "../maps/web/"
def get_testcase(i): return testcase + str(i)
def get_web_map(i): return mapweb + str(i)

def getColor(index):
    index = index % 5
    return{
        0:'\033[95m',
        1:'\033[94m',
        2:'\033[92m',
        3:'\033[96m',
        4:'\033[91m',
        5:'\033[0m'}.get(index)

def getLsGoal(ls, map):
    lsGoal = []
    for i, j in ls:
        if i == -1 and j == -1:
            lsGoal.append(Button(CHANGECONTROL, 3, [], -1, -1))
        else:
            lsGoal.append(map.getElement(i, j))
    return lsGoal

UP = " --> U "
DOWN = " --> D "
LEFT = " --> L "
RIGHT = " --> R "

class State():
    "Trạng thái của trò chơi"
    def __init__(self, block ,value = 0,map = None, mapChanged = False):
        self.block = block
        self.parent = None
        self.move = None
        self.lsGoal = []
        self.map = map
        self.value = value
        self.mapChanged = mapChanged
        self.goalA = []
        self.goalB = []

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
        A = self.block.A
        B = self.block.B
        if self.block.control is None:
            if self.getMap().isGoal(self.block) or len(self.lsGoal) == 0:
                return [True, None]
            g = self.lsGoal[0]
            if g.w <= self.block.weight() and ((g.x == A.x and g.y == A.y) or (g.x == B.x and g.y == B.y)):
                self.lsGoal.pop(0)
                return [True, g]
            if self.parent is not None and self.parent.block.control is not None:
                if len(self.goalA) != 0:
                    g = self.goalA[0]
                    if g.x == A.x and g.y == A.y:
                        self.goalA.pop(0)
                        return [True, g]
                if len(self.goalB) != 0:
                    g = self.goalB[0]
                    if g.x == B.x and g.y == B.y:
                        self.goalB.pop(0)
                        return [True, g]
            return [False, None]
        elif self.block.control == self.block.A:
            if len(self.goalA) == 0:
                self.block.changeControl()
                return [False, None]
            g = self.goalA[0]
            if A.x == g.x and A.y == g.y:
                self.goalA.pop(0)
                if not self.goalA:
                    self.block.changeControl()
                else:
                    g = self.goalA[0]
                    if(g.type == CHANGECONTROL):
                        self.goalA.pop(0)
                        self.block.changeControl()
                        return [False, g]
                return [True, g]
        elif self.block.control == self.block.B:
            if len(self.goalB) == 0:
                self.block.changeControl()
                return [False, None]
            g = self.goalB[0]
            if B.x == g.x and B.y == g.y:
                self.goalB.pop(0)
                if not self.goalB:
                    self.block.changeControl()
                else:
                    g = self.goalB[0]
                    if(g.type == CHANGECONTROL):
                        self.goalB.pop(0)
                        self.block.changeControl()
                        return [False, g]
                return [True, g]
        return [False, None]

    def distance(self):
        A = self.block.A
        g = self.lsGoal[0]
        if self.block.control == A and self.goalA:
            g = self.goalA[0]
        elif self.block.control == self.block.B and self.goalB:
            A = self.block.B
            g = self.goalB[0]
        if g.type == CHANGECONTROL:
            g = self.lsGoal[0]
        vectorAG = [g.x - A.x, g.y - A.y]
        return sqrt(vectorAG[0]**2 + vectorAG[1]**2)
    def __eq__(self, other):
        return other != None and self.block == other.block and self.getMap() == other.getMap()

    def __lt__(self, other):
        return self.distance() < other.distance()

    def __repr__(self):
        return str(self.move) + "\r" + str(self.getMap().__repr__(self.block)) + "\r"
    def shortSol(self):
        return str(self.move)


def nextState(current):
    children = []
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

        newstate = State(newblock, current.value + 1)
        newstate.move = mv
        newstate.lsGoal = current.lsGoal
        newstate.goalA = current.goalA
        newstate.goalB = current.goalB
        newstate.parent = current
        newstate.checkMapChange()
        if newstate.isValid():
            children.append(newstate)
    return children

def breadth_first_search(initState):
    initState.getMap().name +="(breadth first search)"
    counter = 0
    queue = list()
    explored = list()
    queue.append(initState)
    while queue:
        state = queue.pop(0)
        check, value = state.isGoal()
        counter += 1
        explored.append(state)
        if check == True:
            queue.clear()
            explored.clear()
            if value == None:
                return [state, counter]
        children = nextState(state)
        for i in children:
            if i not in explored:
                queue.append(i)
    return [initState, -1]

def depth_first_search(initState, maxdepth = 50):
    initState.getMap().name +="(depth first search)"
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
                return [state, counter]
        explored.append(state)
        if state.value > maxdepth:
            continue
        children = nextState(state)
        for i in children:
            if i not in explored:
                stack.append(i)
    return [initState, -1]



def best_first_search(initState):
    initState.getMap().name += "(best first search)"
    counter = 0
    queue = PriorityQueue()
    explored = list()
    queue.put(initState)
    while not queue.empty():
        state = queue.get()
        check, value = state.isGoal()
        counter += 1
        if check == True:
            if value == None:
                return [state, counter]
        explored.append(state)
        children = nextState(state)
        for i in children:
            if i not in explored:
                queue.put(i)
    return [initState, -1]


def getMoveStep(state):
    root = []
    root.append(state)
    parent = state.parent
    while parent:
        root.append(parent)
        parent = parent.parent

    root = reversed(root)
    count = 0
    result = '%d.\t' % count
    for j, k in enumerate(root):
        if j == 0: continue
        if j % 5 != 0:
            result += str(k.shortSol())
        else:
            count += 1
            result += str(k.shortSol()) + ("\n%d.\t" % count)
    return result
