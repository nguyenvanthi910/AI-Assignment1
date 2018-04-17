#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import deepcopy
try:
	from src import Elements
	import src.FileHandler as file
except ImportError:
	import Elements
	import FileHandler as file



testcase = "../testcase/"
mapweb = "../maps/web/"
def get_testcase(i): return testcase + str(i)
def get_web_map(i): return mapweb + str(i)

map, block = file.readFrom(get_web_map(1))


UP = " -----------> MOVE UP "
DOWN = " -----------> MOVE DOWN "
LEFT = " -----------> MOVE LEFT "
RIGHT = " -----------> MOVE RIGHT "

class State():
    "Trạng thái của trò chơi"
    def __init__(self, block):
        self.block = block
        self.parent = None
        self.move = None
        self.map = None
        self.mapChanged = False

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

    def isGoal(self):
        return self.getMap().isGoal(self.block)

    def __eq__(self, other):
        return self.block == other.block and self.getMap() == other.getMap()

    def __repr__(self):
        return str(self.move) + "\n" + str(self.getMap().__repr__(self.block)) + "\n" +\
          "\n".join("\t\t\t||" for i in range(2)) + "\n\t\t\t\\/\n"

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
        newstate = State(newblock)
        newstate.move = mv
        newstate.parent = current
        newstate.checkMapChange()
        if newstate.isValid():
            children.append(newstate)
    return children

def breadth_first_search():
    initState = State(block)
    initState.map = map
    initState.mapChanged = True
    
    queue = list()
    explored = list()
    queue.append(initState)
    while queue:
        state = queue.pop(0)
       # print state
        if state.isGoal():
            printSolution(state)
            return
        explored.append(state)
        children = nextState(state)
        for i in children:
            if i not in explored:
                queue.append(i)

def printSolution(state):
    root = []
    root.append(state)
    parent = state.parent
    while parent:
        root.append(parent)
        parent = parent.parent

    root = reversed(root)
    for i,t in enumerate(root):
        print(str(i) + '\t' + str(t))

print map
breadth_first_search()
