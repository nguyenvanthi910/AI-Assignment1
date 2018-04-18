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



def getLsGoal():
    lsGoal = []
    for i, j in ls:
        lsGoal.append(map.getElement(i, j))
    return lsGoal

UP = " ---> UP "
DOWN = " ---> DOWN "
LEFT = " ---> LEFT "
RIGHT = " ---> RIGHT "

class State():
    "Trạng thái của trò chơi"
    def __init__(self, block ,map = None, mapChanged = False):
        self.block = block
        self.parent = None
        self.move = None
        self.lsGoal = None
        self.map = map
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
        return str(self.move) + "\n" + str(self.getMap().__repr__(self.block)) + "\n" +\
          "\n".join("\t\t\t||" for i in range(2)) + "\n\t\t\t\\/\n"
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
        newstate = State(newblock)
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
            printShortSolution(state)
            if value == None:
                printSolution(state)
                printShortSolution(state)
                print("Explored %d states\n\n" % counter)
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

if __name__ == '__main__':
    m = '1'
    m = input("Input level: ")
    while(m != 'q'):
        try:
            map, block, ls = file.readFrom(get_web_map(int(m)))

            initState = State(block, map, True)
            initState.lsGoal = getLsGoal()

            print(map)

            breadth_first_search(initState)

            m = input("Input another level (q for quit): ")
        except Exception as e:
            print(e)
            m = input("This level is error. Choose another level(q for quit): ")