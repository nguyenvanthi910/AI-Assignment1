#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from Elements import *
    import FileHandler as file
except ImportError:
    from src.Elements import  *
    import src.FileHandler as file

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
    def __init__(self, block ,value = 0,map = None, mapChanged = False):
        self.block = block
        self.parent = None
        self.move = None
        self.lsGoal = None
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
        if(self.getMap().isGoal(self.block)): return [True, None]
        if self.block.control == None:
            if not self.lsGoal: return [True, None]
            g = self.lsGoal[0]
            if g.w <= self.block.weight() and self.__cp__(g):
                self.lsGoal.pop(0)
                return [True, g]
            else: return [False, g]
        if self.block.control == self.block.A:
            if not self.goalA:
                return [False, None]
            g = self.goalA[0]
            A = self.block.A
            if A.x == g.x and A.y == g.y:
                self.goalA.pop(0)
                if not self.goalA:
                    self.block.changeControl()
                return [True, g]
            else: return [False, g]
        if self.block.control == self.block.B:
            g = self.goalB[0]
            B = self.block.B
            if B.x == g.x and B.y == g.y:
                self.goalB.pop(0)
                if not self.goalB:
                    self.block.changeControl()
                return [True, g]
            else: return [False, g]
        return [False, None]

    def __eq__(self, other):
        return self.block == other.block and self.getMap() == other.getMap()

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
            else:
                print("Passed: " + str(value))
                print(state)
        explored.append(state)
        children = nextState(state)
        for i in children:
            if i not in explored:
                queue.append(i)
    print("Solution not found.")
    return initState

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

if __name__ == '__main__':
    m = '1'
    m = input("Input level: ")
    while(m != 'q'):
        try:
            map, block, ls, goalA, goalB = file.readFrom(get_web_map(int(m)))

            initState = State(block, 0, map, True)
            initState.lsGoal = getLsGoal(ls, map)
            if goalA:
                initState.goalA = goalA
            if goalB:
                initState.goalB = goalB
            t = "1"
            print("\nALGORITHM LIST:\n\t1. Breadth first search\n\t2. Depth first search\n\t3....\r")
            t = input("Please input algorithm(default 1):")
            stop = False
            if t == "1":
                state = breadth_first_search(initState)
            elif t == "2":
                depth = input("Input max depth (default 10): ")
                try: d = int(depth)
                except Exception: d = 10
                state = depth_first_search(initState, d)
            elif t == "3":
                t = "fail"
            else: state = breadth_first_search(initState)

            printShortSolution(state)
            m = input("Input another level (q for quit): ")
        except Exception as e:
            print(e)
            m = input("This level is error. Choose another level(q for quit): ")

