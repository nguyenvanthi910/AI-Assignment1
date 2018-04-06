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
def get_textcase(i): return testcase + str(i)

map, block = file.readFrom(get_textcase(2))


UP = " -> move up "
DOWN = " -> move down "
LEFT = " -> move left "
RIGHT = " -> move right "

class State():
    "Trạng thái của trò chơi"
    def __init__(self, block):
        self.block = block
        self.parent = None
        self.move = None

    def isValid(self):
        return map.isValid(self.block)

    def isGoal(self):
        return map.isGoal(self.block)

    def __eq__(self, other):
        return self.block == other.block

    def __repr__(self):
        return str(self.block) + str(self.move)

print(map)
print(block)

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
        if newstate.isValid():
            newstate.parent = current
            children.append(newstate)
    return children

def breadth_first_search():
    initState = State(block)
    queue = list()
    explored = list()
    queue.append(initState)
    while queue:
        state = queue.pop(0)
        explored.append(state)
        if state.isGoal():
            print("Explored: " + str(len(explored)) + " state")
            print(state.block)
            return
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

breadth_first_search()
